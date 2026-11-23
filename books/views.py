from django.views import View
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.shortcuts import render, redirect, get_object_or_404



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
    
class BookUpdateView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, "books/book_form.html", {"form": form})
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
        return render(request, "books/book_form.html", {"form": form}) 
    
class BookDeleteView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, "books/book_confirm_delete.html", {"book": book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return redirect("book_list")