# Generated by Django 5.0 on 2024-01-03 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0002_ad_show'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['-id']},
        ),
    ]
