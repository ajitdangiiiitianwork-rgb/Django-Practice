from django.shortcuts import render , redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def recipe(request):
  if request.method == 'POST':
    data = request.POST
    recipe_image = request.FILES.get('recipe_image')
    recipe_name = data.get('recipe_name')
    recipe_desc = data.get('recipe_desc')

    Recipe.objects.create(
      recipe_image = recipe_image,
      recipe_desc = recipe_desc,
      recipe_name = recipe_name
    )

    return redirect('/recipes/')
  
  querySet = Recipe.objects.all()

  if(request.GET.get('search')):
    querySet = querySet.filter(recipe_name__icontains = request.GET.get('search'))

  context = {'recipes' : querySet}
  return render(request, 'recipes.html', context) 

def delete_recipes(request, id):
  queryset = Recipe.objects.get(id = id)
  queryset.delete()
  return redirect('/recipes/')

def update_recipes(request, id):
  queryset = Recipe.objects.get(id = id)

  if request.method == 'POST':
    data = request.POST
    recipe_image = request.FILES.get('recipe_image')
    recipe_name = data.get('recipe_name')
    recipe_desc = data.get('recipe_desc')

    queryset.recipe_name = recipe_name
    queryset.recipe_desc = recipe_desc
    
    if queryset.recipe_image:
      queryset.recipe_image = recipe_image

    queryset.save()
    return redirect('/recipes/')
  
  context = {'recipe' : queryset}
  return render(request, 'update_recipes.html', context)

def login_page(request):
  return render(request, 'login_page.html')

def register_page(request):
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username = username)
    if user.exists():
      messages.info(request, 'Username Already exists!')
      return redirect('/register_page/')

    user = User.objects.create(
      first_name = first_name,
      last_name = last_name,
      username = username,
    )

    user.set_password(password)
    user.save()
    messages.info(request, 'Account created Successfully!!')
    return redirect('/register_page/')
  return render(request, 'register_page.html')
