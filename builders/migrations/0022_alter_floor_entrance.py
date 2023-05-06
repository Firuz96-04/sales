# Generated by Django 4.1.7 on 2023-05-01 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builders', '0021_alter_apartment_floor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='entrance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='floors', to='builders.entrance'),
        ),
    ]