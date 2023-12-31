# Generated by Django 5.0 on 2023-12-19 19:09

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='post.category'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=models.ImageField(blank=True, default='featured_images/default_image.png', null=True, upload_to='featured_images/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg', 'gif'])]),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='post.tag'),
        ),
    ]
