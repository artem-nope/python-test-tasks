from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import generics

from .models import *
from .forms import *
from .serializers import *


# Create your views here.
def index(request):
    return render(
        request,
        template_name='books/index.html',
        context={
            'book_count': Book.objects.count(),
            'author_count': Author.objects.count(),
            'genre_count': Genre.objects.count(),

        }
    )


def book_list(request):
    object_list = Book.objects.select_related('author').annotate(num_comments=Count("comments")).order_by('title')
    # print(object_list[0].__dict__)
    return render(
        request,
        template_name='books/book_list.html',
        context={
            'object_list': object_list,
        }
    )


def book_detail(request, pk):
    return render(
        request,
        template_name='books/book_detail.html',
        context={
            'object': Book.objects.get(id__exact=pk),
            'comment_form': CommentForm()
        }
    )


def author_list(request):
    return render(
        request,
        template_name='books/author_list.html',
        context={
            'object_list': Author.objects.all(),
        }
    )


def author_detail(request, slug):
    return render(
        request,
        template_name='books/author_detail.html',
        context={
            'object': Author.objects.get(slug__exact=slug),
            'comments': Comment.objects.filter(book__author__slug__exact=slug).select_related('book'),
        }
    )


# def add_comment(request, pk):
#     book = Book.objects.get(id__exact=pk)
#     print(request.POST)
#     Comment.objects.create(
#         username=request.POST['username'],
#         text=request.POST.get('text'),
#         book=book
#     )
#     return HttpResponseRedirect(book.get_absolute_url())

def add_comment(request, pk):
    book = Book.objects.get(id__exact=pk)
    # print(request.POST)
    form = CommentForm(request.POST)
    new_comment = form.save(commit=False)
    new_comment.book = book
    new_comment.save()
    # print(new_comment)
    return HttpResponseRedirect(book.get_absolute_url())


def genre_list(request):
    return render(
        request,
        template_name='books/genre_list.html',
        context={
            'object_list': Genre.objects.prefetch_related('books__author'),
        }
    )


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListApiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer