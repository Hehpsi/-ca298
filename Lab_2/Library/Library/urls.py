from django.urls import path
from . import views
from .views import *

urlpatterns = [
   path('', views.index, name="base"),
   path('books', view_all_books, name='all_books'),
   path('books/<int:bookid>', view_single_book, name='single_book'),
]

