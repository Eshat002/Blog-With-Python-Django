# Generated by Django 5.0 on 2024-01-09 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
