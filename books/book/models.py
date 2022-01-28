from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    img = models.CharField(max_length=100, null=True)
    date_birth = models.DateField()
    date_death = models.DateField(blank=True, null=True)


class Genre(models.Model):
    name = models.CharField(max_length=150)


class Print(models.Model):
    name = models.CharField(max_length=150)


class Book(models.Model):
    name = models.CharField(max_length=100)
    author_id = models.ManyToManyField(Author)
    description = models.TextField()
    print_id = models.ForeignKey(Print, on_delete=models.SET_NULL, null=True)
    year_of_release = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2022)])
    genre_id = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=14)
    image = models.CharField(max_length=100, null=True)
    language_id = models.ManyToManyField(Language)


class BookInstance(models.Model):
    id_book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50)
    date_back = models.DateField(blank=True, null=True)
