from django.shortcuts import render , redirect
from vege.models import *
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
