# Generated by Django 4.1.7 on 2023-04-25 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_apartmenttype'),
        ('builders', '0008_alter_apartment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='decoration',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.apartmentdecoration', verbose_name='отделка'),
        ),
    ]