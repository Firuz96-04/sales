# Generated by Django 4.1.7 on 2023-04-27 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_apartmentstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartmentstatus',
            options={'verbose_name': 'статус квартиры'},
        ),
        migrations.AlterModelTable(
            name='apartmentstatus',
            table='apartment_status',
        ),
    ]
