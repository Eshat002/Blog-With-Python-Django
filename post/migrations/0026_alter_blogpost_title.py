# Generated by Django 5.0 on 2024-01-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0025_alter_blogpost_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]