# Book Management (Django)

A small Django project for managing books and their authors.

## Features

- List all books with their author and year
- Add a new book
- Edit an existing book
- Delete a book (with a confirmation page)
- Manage authors and books from the Django admin panel

## Tech

- Python 3.14
- Django 6.1
- SQLite

## Setup

```powershell
git clone https://github.com/darya2004-s/Mysite.git
cd Mysite
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

Then open:

- http://127.0.0.1:8000/books/ for the book list
- http://127.0.0.1:8000/admin/ for the admin panel

## Project structure

```
mysite/
├── manage.py
├── requirements.txt
├── mysite/          # project settings and main urls
└── books/           # the books app
    ├── models.py    # Author and Book models
    ├── forms.py     # BookForm
    ├── views.py     # list, create, update, delete views
    ├── urls.py
    └── templates/books/
```

## Models

- **Author**: name
- **Book**: title, year, price, author (ForeignKey to Author)
