# Generated by Django 3.1.7 on 2021-03-30 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BluetoothDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=100)),
                ('device_type', models.CharField(max_length=100)),
                ('device_mac', models.CharField(max_length=100)),
            ],
        ),
    ]
