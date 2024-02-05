from django.db import models
import datetime


# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=256)
    views = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.datetime.now)
    # answers - field

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.CharField(max_length=256)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)  # SET_NULL

    def __str__(self):
        return self.text

