# Generated by Django 3.1.7 on 2021-04-21 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_bluetoothservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bluetoothservice',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='host',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='port',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='profiles',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='protocol',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='provider',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='service_classes',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bluetoothservice',
            name='service_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
