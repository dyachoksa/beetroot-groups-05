# Generated by Django 5.0.1 on 2024-02-06 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_add_slug_to_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=models.SlugField(max_length=150, null=True),
        ),
    ]