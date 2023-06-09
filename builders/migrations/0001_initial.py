# Generated by Django 4.1.7 on 2023-04-23 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('square', models.DecimalField(decimal_places=1, default=1, max_digits=3)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('rented', models.BooleanField(default=False, verbose_name='сдан или не сдан')),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.SmallAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
