# Generated by Django 3.2.9 on 2021-11-21 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoshare', '0003_photo_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='customer',
        ),
    ]
