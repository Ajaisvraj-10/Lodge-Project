# Generated by Django 4.2.3 on 2023-07-26 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10, unique=True)),
                ('rent_per_hour', models.DecimalField(decimal_places=2, max_digits=10)),
                ('booking_details', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
