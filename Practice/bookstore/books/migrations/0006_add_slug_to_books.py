# Generated by Django 5.0.1 on 2024-02-06 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_add_book_num_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=300, null=True),
        ),
    ]