from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pizzashop.pizzas.urls')),
    path('admin/', admin.site.urls),
]
