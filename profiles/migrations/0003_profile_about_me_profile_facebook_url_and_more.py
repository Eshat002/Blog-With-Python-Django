# Generated by Django 5.0 on 2023-12-30 18:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about_me',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='facebook_url',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
