# Generated by Django 3.1.7 on 2021-09-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_cvetable'),
    ]

    operations = [
        migrations.AddField(
            model_name='bluetoothdevice',
            name='location',
            field=models.CharField(default='Building1', max_length=100),
            preserve_default=False,
        ),
    ]
