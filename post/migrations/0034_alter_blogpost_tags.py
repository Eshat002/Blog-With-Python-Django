# Generated by Django 5.0 on 2024-01-27 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0033_alter_blogpost_related_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, to='post.tag'),
        ),
    ]