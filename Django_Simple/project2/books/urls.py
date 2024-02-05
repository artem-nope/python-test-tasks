from django.urls import path
from . import views


app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/all/', views.book_list, name='book-list'),
    path('book/<int:pk>/', views.book_detail, name='book-detail'),
    path('author/all/', views.author_list, name='author-list'),
    path('author/<slug:slug>/', views.author_detail, name='author-detail'),
    path('comment/<int:pk>/', views.add_comment, name='add-comment'),
    path('genre/all/', views.genre_list, name='genre-list'),
    path('api/book/all', views.BookListApiView.as_view(), name='api-book-list'),
    path('api/author/all', views.AuthorListApiView.as_view(), name='api-author-list'),
]

# api for author_list