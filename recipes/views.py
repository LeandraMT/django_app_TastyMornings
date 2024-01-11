from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Recipe
from .forms import RecipeAddForm


# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = "recipes/recipes_home.html"


def home_view(request):
    return render(request, "recipes/main_home.html")


def search_view(request):
    query = request.GET.get("q")
    object_list = Recipe.objects.filter(
        Q(name__icontains=query) | Q(ingredients__icontains=query)
    )
    return render(request, "recipes/recipes_list.html", {"object_list": object_list})


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/detail_page.html"


def add_recipe(request):
    if request.method == "POST":
        form = RecipeAddForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the form data of the Recipe
            name = form.cleaned_data["name"]
            pic = form.cleaned_data["pic"]
            ingredients = form.cleaned_data["ingredients"]
            cooking_time = form.cleaned_data["cooking_time"]
            description = form.cleaned_data["description"]

            # Create a new Recipe instance
            new_recipe = Recipe.objects.create(
                name=name,
                pic=pic,
                ingredients=ingredients,
                cooking_time=cooking_time,
                description=description,
            )
            new_recipe.save()

            # Adding a success message
            messages.success(
                request, "Recipe has been successfully added!", extra_tags="success"
            )

            # Redirect to profile view with newly added recipe
            return redirect("recipes:recipes-list")
    else:
        form = RecipeAddForm()

    context = {"form": form}
    return render(request, "recipes/add_recipe.html", context)
