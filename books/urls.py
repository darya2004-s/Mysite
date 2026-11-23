from django.urls import path
from . import views

urlpatterns = [
    path("", views.BookListView.as_view(), name="book_list"),
    path("add/", views.BookCreateView.as_view(), name="book_add"),
    path("<int:pk>/edit/", views.BookUpdateView.as_view(), name="book_edit"),
    path("<int:pk>/delete/", views.BookDeleteView.as_view(), name="book_delete"),
]