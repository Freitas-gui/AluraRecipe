from django.shortcuts import render

def home(request):
    data = {}
    name_of_recipes = {
        1:'bean',
        2:'rice',
        3:'meat'
    }


    return render(request,'home.html',{'name_of_recipes':name_of_recipes})

def recipes(request):
    return render(request,'recipes.html')

