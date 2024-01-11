from django.shortcuts import render
from recipes.models import Recipe
from .forms import IngredientSearchForm

# Data Visualisation
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt
import base64

# Protecting Function-based View
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile_view(request):
    # User's details being rendered
    username = request.user.username
    email = request.user.email

    user_context = {"username": username, "email": email}

    # Handling the form submission
    if request.method == "POST":
        form = IngredientSearchForm(request.POST)
        if form.is_valid():
            ingredient = form.cleaned_data.get("ingredient")
            recipes_with_ingredient = Recipe.objects.filter(
                ingredients__icontains=ingredient
            )

            # Creating a pandas DataFrame
            df = {
                "Recipe Name": [recipe.name for recipe in recipes_with_ingredient],
                "Cooking Time": [
                    recipe.cooking_time for recipe in recipes_with_ingredient
                ],
            }
            recipes_df = pd.DataFrame(df)

            # Generating the plot image based on user's selection
            chart_type = form.cleaned_data.get("chart_type")
            plt.switch_backend("AGG")
            fig = plt.figure(figsize=(8, 6))

            if chart_type == "#1":
                custom_colors = ["#3a4750", "#bbe4e9", "#ffebbb", "#42b883", "#dde0ab"]
                plt.bar(
                    recipes_df["Recipe Name"],
                    recipes_df["Cooking Time"],
                    color=custom_colors,
                )
                plt.xlabel("Recipe Name", fontsize=10)
                plt.ylabel("Cooking Time", fontsize=10)
                plt.xticks(fontsize=8)
                plt.yticks(fontsize=8)

            elif chart_type == "#2":
                plt.pie(
                    recipes_df["Cooking Time"],
                    labels=recipes_df["Recipe Name"],
                    colors=["#3a4750", "#bbe4e9", "#ffebbb", "#42b883", "#dde0ab"],
                    textprops={"fontsize": 9},
                )

            elif chart_type == "#3":
                plt.plot(
                    recipes_df["Recipe Name"],
                    recipes_df["Cooking Time"],
                    color="#3a4750",
                )
                plt.xlabel("Recipe Name", fontsize=10)
                plt.ylabel("Cooking Time", fontsize=10)
                plt.xticks(fontsize=8)
                plt.yticks(fontsize=8)

            else:
                plt.text(0.5, 0.5, "Unknown chart type", ha="center", va="center")

            plt.tight_layout()

            # Convert the plot to a base64-encoded image
            buffer = BytesIO()
            plt.savefig(buffer, format="png")
            buffer.seek(0)
            chart_image = base64.b64encode(buffer.getvalue()).decode("utf-8")
            plt.close()

            context = {"form": form, "chart_image": chart_image, **user_context}
            return render(request, "profile/profile_view.html", context)
    else:
        form = IngredientSearchForm()

    context = {"form": form, "chart_image": None, **user_context}

    return render(request, "profile/profile_view.html", context)


def about_me_view(request):
    return render(request, "profile/about_view.html")
