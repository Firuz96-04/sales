# Generated by Django 4.1.7 on 2023-04-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0012_alter_floor_image_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='residentcomplex',
            name='latitude',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='residentcomplex',
            name='longitude',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
