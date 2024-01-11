from django.test import TestCase
from .models import Recipe


# Create your tests here.
class RecipeModelTest(TestCase):
    def setUpTestData(cls):
        Recipe.objects.create(
            name="Tea",
            ingredients="Tea leaves, Water, Sugar",
            cooking_time=5,
            description="When water is boiling add the tea leaves and sugar (optional). Let it rest for 2 minutes.",
        )

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_max_length = recipe._meta.get_field("name").max_length
        self.assertEqual(recipe_name_max_length, 120)

    def test_cooking_time(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cooking_time = recipe._meta.get_field("cooking_time").help_text
        self.assertEqual(recipe_cooking_time, "in minutes")

    def test_get_absolute_url(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.get_absolute_url(), "/recipes/1")
