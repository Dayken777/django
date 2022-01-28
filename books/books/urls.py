"""books URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from urllib import request

from django.contrib import admin, auth
from django.urls import path
from django.contrib.auth import views as authViews
from authuser.views import auth_get_page, registration_get_page, profile_get_page
from book.views import main, catalog_get_page, book_get_page, author_get_page, authors_get_page, sold_book_get_page, \
    filter_book_name_get_page, filter_author_name_get_page, filter_language_name_get_page, filter_genre_name_get_page

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('catalog/', main, name='main'),
    path('registration/', registration_get_page, name='registration'),
    path('auth/', auth_get_page, name='auth'),
    path('exit/', authViews.LogoutView.as_view(next_page='auth'), name='exit'),
    path('profile/', profile_get_page, name='profile'),
    path('catalog/books', catalog_get_page, name='catalog'),
    path('catalog/book/<id>', book_get_page, name='book'),
    path('catalog/authors/', authors_get_page, name='author'),
    path('catalog/author/<id>', author_get_page, name='book'),
    path('catalog/sold_books/<id>', sold_book_get_page, name="sold_book"),
    path('catalog/filter/book/<id>', filter_book_name_get_page, name="book_filter_name"),
    path('catalog/filter/author/<id>', filter_author_name_get_page, name="book_filter_author_name"),
    path('catalog/filter/language/<id>', filter_language_name_get_page, name="book_filter_language_name"),
    path('catalog/filter/genre/<id>', filter_genre_name_get_page, name="book_filter_genre_name"),
    # path('personal_cabinet/', registration_post_data, name='personal_cabinet'),

]
