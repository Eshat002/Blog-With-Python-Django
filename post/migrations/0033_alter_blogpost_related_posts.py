# Generated by Django 5.0 on 2024-01-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0032_alter_blogpost_related_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='related_posts',
            field=models.ManyToManyField(blank=True, to='post.blogpost'),
        ),
    ]
