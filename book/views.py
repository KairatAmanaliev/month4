from django.shortcuts import render
from book.models import Book


# Create your views here.

def book_view(request):
    if request.method == "GET":
        books = Book.objects.all()
        data = {
            'book_object': books
        }
        return render(request, 'book.html', context=data)
