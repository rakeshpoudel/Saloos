# Generated by Django 3.1.5 on 2021-05-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Barber', '0002_remove_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]