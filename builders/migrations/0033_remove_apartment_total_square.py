# Generated by Django 4.1.7 on 2023-05-06 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0032_client_apartment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='total_square',
        ),
    ]