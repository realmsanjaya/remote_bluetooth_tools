# Generated by Django 3.1.7 on 2021-04-26 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_bluetoothservice_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bluetoothdevice',
            name='device_type',
        ),
    ]
