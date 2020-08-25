from django.shortcuts import render
from .models import Recipe

def home(request):
    recipes = Recipe.objects.all()
    return render(request,'home.html',{'recipes':recipes})

def show_recipe(request, id_recipe):
    context = Recipe.objects.filter(id=id_recipe)
    return render(request,'recipe.html',{'context':context})

def show_recipe_all(request):
    context = Recipe.objects.all()
    return render(request,'recipe.html',{'context':context})

