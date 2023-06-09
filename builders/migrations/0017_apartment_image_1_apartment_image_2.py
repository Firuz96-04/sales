# Generated by Django 4.1.7 on 2023-04-27 11:09

import builders.utils
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0016_remove_apartment_image_1_remove_apartment_image_2'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='image_1',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=builders.utils.upload_block_apartment),
        ),
        migrations.AddField(
            model_name='apartment',
            name='image_2',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=builders.utils.upload_block_apartment),
        ),
    ]
