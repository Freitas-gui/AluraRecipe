from django.urls import path
from . import views

urlpatterns = [
    path('', views.home.as_view(), name='home' ),
    path('recipes/', views.show_recipe_all, name='show_recipe_all'),
    path('recipes/<int:id_recipe>', views.show_recipe, name='show_recipe'),

]