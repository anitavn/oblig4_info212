# Generated by Django 4.1.2 on 2022-11-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_remove_car_status_car_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='availability',
        ),
        migrations.AddField(
            model_name='car',
            name='car_status',
            field=models.CharField(default='available', max_length=50),
        ),
    ]