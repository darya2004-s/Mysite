from django.views import View
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm




class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/book_list.html", {"books": books})

class BookCreateView(View): 
    def get(self, request):
        # فرم خالی می‌سازد (بدون هیچ داده)، از روی BookForm که در forms.py
        form = BookForm()
        return render(request, "books/book_form.html", {"form": form})
    
    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        return render(request, "books/book_form.html", {"form": form})