# Generated by Django 4.1.7 on 2023-04-29 06:47

import builders.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0018_alter_manager_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to=builders.utils.upload_block_floor),
        ),
    ]
