# Generated by Django 4.1.7 on 2023-04-26 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0010_alter_block_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floor',
            name='image_2',
        ),
    ]