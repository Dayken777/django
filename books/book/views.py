import re

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from book.models import Book, Author, Print, BookInstance, Language, Genre


def main(request):
    books = Book.objects.all()
    return render(request, 'main.html', context={'books': books})


def catalog_get_page(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    languages = Language.objects.all()
    genres = Genre.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog.html', context={'books': books,
                                                        'authors': authors,
                                                        'languages': languages,
                                                        'genres': genres})
    return redirect('auth')


def authors_get_page(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    str(books)
    str(authors)
    if request.user.is_authenticated:
        return render(request, 'authors.html', context={'books': books, 'authors': authors})
    return redirect('auth')


def book_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    bookinstance_all = BookInstance.objects.all().filter(id_book=id)
    bookinstance_in_stock = BookInstance.objects.all().filter(id_book=id, status="На складе")
    bookinstance_order = BookInstance.objects.all().filter(id_book=id, status="Заказана")
    bookinstance_sold = BookInstance.objects.all().filter(id_book=id, status="Продана")
    count_all = len(bookinstance_all)
    count_in_stock = len(bookinstance_in_stock)
    count_order = len(bookinstance_order)
    count_sold = len(bookinstance_sold)
    book = Book.objects.all().get(pk=id)
    print = Print.objects.all()
    return render(request, 'book.html',
                  {'id': id, 'book': book, 'print': print, 'count_in_stock': count_in_stock,
                   'count_all': count_all, 'count_order': count_order, 'count_sold': count_sold})


def author_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    author = Author.objects.all().get(pk=id)
    print = Print.objects.all()
    return render(request, 'author.html', {'id': id, 'author': author, 'print': print})


def sold_book_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    bookinstance_all = BookInstance.objects.all().filter(id_book=id)
    bookinstance_in_stock = BookInstance.objects.all().filter(id_book=id, status="На складе")
    bookinstance_order = BookInstance.objects.all().filter(id_book=id, status="Заказана")
    bookinstance_sold = BookInstance.objects.all().filter(id_book=id, status="Продана")
    count_all = len(bookinstance_all)
    count_in_stock = len(bookinstance_in_stock)
    count_order = len(bookinstance_order)
    count_sold = len(bookinstance_sold)
    books = Book.objects.all().filter()
    book = Book.objects.all().get(pk=id)
    print = Print.objects.all()
    return render(request, 'sold_book_back_date.html',
                  {'bookinstance_sold': bookinstance_sold, 'id': id, 'books': books, 'book': book, 'print': print,
                   'count_in_stock': count_in_stock,
                   'count_all': count_all, 'count_order': count_order, 'count_sold': count_sold})


def filter_book_name_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    books = Book.objects.all().filter(id=id)
    authors = Author.objects.all()
    languages = Language.objects.all()
    genres = Genre.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog.html', context={'books': books,
                                                        'authors': authors,
                                                        'languages': languages,
                                                        'genres': genres})
    return redirect('auth')


def filter_author_name_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    books = Book.objects.all().filter(id=id)
    authors = Author.objects.all()
    languages = Language.objects.all()
    genres = Genre.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog.html', context={'books': books,
                                                        'authors': authors,
                                                        'languages': languages,
                                                        'genres': genres})
    return redirect('auth')


def filter_language_name_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    books = Book.objects.all().filter(id=id)
    authors = Author.objects.all()
    languages = Language.objects.all()
    genres = Genre.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog.html', context={'books': books,
                                                        'authors': authors,
                                                        'languages': languages,
                                                        'genres': genres})
    return redirect('auth')


def filter_genre_name_get_page(request, id):
    id = re.findall('\d+', str(request.get_full_path))
    id = id[0]
    books = Book.objects.all().filter(id=id)
    authors = Author.objects.all()
    languages = Language.objects.all()
    genres = Genre.objects.all()
    if request.user.is_authenticated:
        return render(request, 'catalog.html', context={'books': books,
                                                        'authors': authors,
                                                        'languages': languages,
                                                        'genres': genres})
    return redirect('auth')
