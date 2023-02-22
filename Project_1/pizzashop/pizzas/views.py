from django.shortcuts import render, redirect
from .models import Pizza, PizzaOrder

def create_pizza(request):
    if request.method == 'POST':
        size = request.POST.get('size')
        crust_type = request.POST.get('crust_type')
        sauce = request.POST.get('sauce')
        cheese = request.POST.get('cheese')
        toppings = request.POST.getlist('toppings')
        pizza = Pizza(size=size, crust_type=crust_type, sauce=sauce, cheese=cheese)
        pizza.save()
        for topping in toppings:
            pizza.toppings.add(topping)
        return redirect('order', pizza.id)
    context = {'toppings': ['Pepperoni', 'Chicken', 'Ham', 'Pineapple', 'Peppers', 'Mushrooms', 'Onions']}
    return render(request, 'create_pizza.html', context)

def order(request, pizza_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        card_number = request.POST.get('card_number')
        expiry_month = request.POST.get('expiry_month')
        expiry_year = request.POST.get('expiry_year')
        cvv = request.POST.get('cvv')
        pizza = Pizza.objects.get(pk=pizza_id)
        order = PizzaOrder(name=name, address=address, card_number=card_number, expiry_month=expiry_month,
                           expiry_year=expiry_year, cvv=cvv, pizza=pizza)
        order.save()
        return redirect('order_confirmation', order.id)
    context = {'pizza': Pizza.objects.get(pk=pizza_id)}
    return render(request, 'order.html', context)

def order_confirmation(request, order_id):
    context = {'order': PizzaOrder.objects.get(pk=order_id)}
    return render(request, 'order_confirmation.html', context)
