from django import forms


class IngredientSearchForm(forms.Form):
    ingredient = forms.CharField(label="Search by Ingredient", max_length=100)
    chart_type = forms.ChoiceField(
        choices=[
            ("#1", "Bar Chart"),
            ("#2", "Pie Chart"),
            ("#3", "Line Chart"),
        ],
        label="Select Chart Type",
        initial="#1",
        widget=forms.RadioSelect(),
    )
