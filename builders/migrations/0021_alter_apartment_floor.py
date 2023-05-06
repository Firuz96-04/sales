# Generated by Django 4.1.7 on 2023-05-01 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0020_alter_apartment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='floor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='apartments', to='builders.floor'),
        ),
    ]
