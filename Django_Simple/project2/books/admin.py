from django.contrib import admin
from .models import *


# Register your models here.
class BookInline(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    prepopulated_fields = {"slug": ["first", "last"]}
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'summary']
    list_filter = ['author']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['username', 'text', 'book']
    list_filter = ['book']
