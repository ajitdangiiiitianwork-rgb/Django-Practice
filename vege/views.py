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
    
  return render(request, 'recipes.html') 