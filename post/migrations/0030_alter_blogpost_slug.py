# Generated by Django 5.0 on 2024-01-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0029_alter_blogpost_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
