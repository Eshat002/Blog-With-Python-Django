# Generated by Django 5.0 on 2024-01-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faq',
            options={'ordering': ['-id']},
        ),
    ]
