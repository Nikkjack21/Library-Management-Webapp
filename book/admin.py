from django.contrib import admin

from book.models import Book, BookBorrow, BookReturn

# Register your models here.

admin.site.register(Book)
admin.site.register(BookBorrow)
admin.site.register(BookReturn)