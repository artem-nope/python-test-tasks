from django.db import models
from django.urls import reverse
from django.utils.timezone import now


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=32)
    # books

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Author(models.Model):
    first = models.CharField(max_length=32)
    last = models.CharField(max_length=32)
    portrait = models.URLField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    # books

    def __str__(self):
        return f'{self.first} {self.last}'

    # def get_genres(self):
    #     genres = []
    #     for book in self.books.all():
    #         for genre in book.genres.all():
    #             genres.append(genre)
    #     return set(genres)
    def get_genres(self):
        return Genre.objects.filter(books__author=self).distinct()

    class Meta:
        ordering = ['last', 'first']

    def get_absolute_url(self):
        return reverse(
            'books:author-detail',
            kwargs= {
                'slug': self.slug
            }
        )


class Book(models.Model):
    title = models.CharField(max_length=256)
    summary = models.TextField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.SET_NULL, blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    # comments

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'books:book-detail',
            kwargs={
                'pk': self.id
            }
        )


class Comment(models.Model):
    username = models.CharField(max_length=64)
    text = models.CharField(max_length=256)
    published = models.DateTimeField(default=now)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-published']
