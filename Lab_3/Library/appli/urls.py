from .views import *
from django.urls import path

urlpatterns = [
 path('books', view_all_books, name="homepage"),
 path('books/customers', view_customers, name='customers'),
 path('books/customers/<int:id>', borrow, name='sort'),
 path('books/<int:bookid>', view_single_book, name='single_book'),
 path('books/year/<int:bookyear>', view_year, name='year'),
 path('books/category/<bookcategory>', view_pen, name='pen_book'),
 path('books/category/<bookcategory>/year/<int:bookyear>', view_pen_year, name='pen_year_book')
]

