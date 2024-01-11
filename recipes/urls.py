from django.urls import path
from .views import RecipeListView, home_view, RecipeDetailView, search_view, add_recipe

# Specifying the app name
app_name = "recipes"

# Specifying the urls
urlpatterns = [
    path("", home_view, name="home"),
    path("recipes/", RecipeListView.as_view(), name="recipes-list"),
    path("recipes/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", search_view, name="search"),
    path("add_recipe/", add_recipe, name="add_recipe"),
]
