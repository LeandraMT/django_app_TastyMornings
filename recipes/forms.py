from django import forms


class RecipeAddForm(forms.Form):
    name = forms.CharField(max_length=120)
    pic = forms.ImageField()
    ingredients = forms.CharField(max_length=400)
    cooking_time = forms.FloatField(help_text="in minutes")
    description = forms.CharField(widget=forms.Textarea)
