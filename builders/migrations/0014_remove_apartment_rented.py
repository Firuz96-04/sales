# Generated by Django 4.1.7 on 2023-04-27 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0013_residentcomplex_latitude_residentcomplex_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='rented',
        ),
    ]
