from django.db import models


# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=32)
    rating = models.FloatField(default=5.0)
    year = models.IntegerField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<{self.name} {self.rating} {self.year}>'
