# Generated by Django 4.1.7 on 2023-04-29 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_apartmentstatus_options_and_more'),
        ('builders', '0019_alter_floor_image_1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.apartmentstatus'),
        ),
    ]
