# Generated by Django 4.2.9 on 2024-01-15 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
