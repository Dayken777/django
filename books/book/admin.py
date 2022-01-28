from django.contrib import admin
from .models import *
admin.site.register(Language)
admin.site.register(Author)
admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Print)
admin.site.register(Book)
