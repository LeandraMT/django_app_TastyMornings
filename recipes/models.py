from django.db import models
from django.shortcuts import reverse


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=120)
    pic = models.ImageField(upload_to="recipes", default="")
    ingredients = models.CharField(max_length=400)
    cooking_time = models.FloatField(help_text="in minutes")
    description = models.TextField()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})
