from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from django.http import Http404
# Create your views here.

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})

def view_single_book(request, bookid):
    single_book = get_object_or_404(Book, id=bookid)
    borrow = Borrow.objects.filter(book=single_book)
    return render(request, 'single_book.html', {'book':borrow})

def view_year(request, bookyear):
    single_book = Book.objects.filter(year=bookyear)
    return render(request, 'years.html', {'book':single_book})

def view_pen(request, bookcategory):
    single_book = Book.objects.filter(category=bookcategory)
    return render(request, 'years.html', {'book':single_book})

def view_pen_year(request, bookcategory, bookyear):
    single_book = Book.objects.filter(category=bookcategory, year=bookyear)
    return render(request, 'years.html', {'book':single_book})

def view_customers(request):
    all_customers = Customer.objects.all()
    return render(request, 'customer.html', {'customers':all_customers})

def borrow(request, id):
    cust = Customer.objects.get(id=id)
    borrowings = Borrow.objects.filter(cust=cust)
    return render(request, 'sorted_books.html', {'borrowings':borrowings})
