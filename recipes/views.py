from django.shortcuts import render
from .models import Recipe
from django.views.generic.list import ListView

class home(ListView):
    model = Recipe
    template_name = "home.html"

def show_recipe(request, id_recipe):
    context = Recipe.objects.filter(id=id_recipe)
    return render(request,'recipe.html',{'context':context})

def show_recipe_all(request):
    context = Recipe.objects.all()
    return render(request, 'recipe.html', {'context':context})

