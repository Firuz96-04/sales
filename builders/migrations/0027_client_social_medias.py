# Generated by Django 4.1.7 on 2023-05-03 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0026_client_action_client_info_apartment'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='social_medias',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
