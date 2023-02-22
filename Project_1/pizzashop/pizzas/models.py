from django.db import models


class Pizza(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]
    CRUST_CHOICES = [
        ('N', 'Normal'),
        ('T', 'Thin'),
        ('TH', 'Thick'),
        ('GF', 'Gluten Free'),
    ]
    SAUCE_CHOICES = [
        ('T', 'Tomato'),
        ('BBQ', 'Barbecue'),
    ]
    CHEESE_CHOICES = [
        ('M', 'Mozzarella'),
        ('V', 'Vegan'),
        ('LF', 'Low Fat'),
    ]
    size = models.CharField(max_length=1, choices=SIZE_CHOICES)
    crust = models.CharField(max_length=2, choices=CRUST_CHOICES)
    sauce = models.CharField(max_length=3, choices=SAUCE_CHOICES)
    cheese = models.CharField(max_length=2, choices=CHEESE_CHOICES)

    def __str__(self):
        return f"{self.size} {self.crust} pizza with {self.sauce} sauce and {self.cheese} cheese"


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PizzaOrder(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    card_expiry_month = models.CharField(max_length=2)
    card_expiry_year = models.CharField(max_length=4)
    card_cvv = models.CharField(max_length=3)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return f"{self.name}'s order"
