from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'base.html')

def view_all_books(request):
    all_books = Book.objects.all()
    return render(request, 'all_books.html', {'books':all_books})


def view_single_book(request, bookid):
	single_book = get_object_or_404(Book, id=bookid)
	return render(request, 'single_book.html', {'book':single_book})
