from django.urls import path
from . import views

urlpatterns = [
    path('templayes/create_pizza/', views.create_pizza, name='create_pizza'),
    path('templates/order/', views.order, name='order'),
    path('templates/order_confirmation/', views.order_confirmation, name='order_confirmation'),
]
