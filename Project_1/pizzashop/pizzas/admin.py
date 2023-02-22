from django.contrib import admin
from .models import Pizza, PizzaSize, Cheese, Sauce, Topping

admin.site.register(Pizza)
admin.site.register(PizzaSize)
admin.site.register(Cheese)
admin.site.register(Sauce)
admin.site.register(Topping)
