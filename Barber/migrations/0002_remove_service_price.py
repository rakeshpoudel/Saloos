# Generated by Django 3.1.5 on 2021-05-20 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Barber', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
    ]
