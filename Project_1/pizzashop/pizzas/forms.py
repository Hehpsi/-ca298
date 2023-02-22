from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['size', 'crust_type', 'sauce', 'cheese', 'toppings']
        widgets = {
            'toppings': forms.CheckboxSelectMultiple,
        }
