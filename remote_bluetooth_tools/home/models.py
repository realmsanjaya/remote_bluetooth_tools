import datetime
from django.db import models
from django.utils import timezone


# Create your models here.
# first_name, last_name, age, is_attending

DEVICE_TYPE = [
    ('BS', 'Bluetooth Speakers'),
    ('PH', 'Phone'),
    ('HS', 'Headset'),
    ('IOT', 'Internet of Things'),
]

class Person(models.Model):
    """ This will store people in the database """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    is_attending = models.BooleanField(default=True)

    def __str__(self):
        #return self.first_name
        #return f"First Name: {self.first_name} Last Name: {self.last_name}"
        return f"{self.first_name} {self.last_name}"

class BluetoothDevice(models.Model):
    """ This table will store the bluetooth devices """
    sensor = models.CharField(max_length=100)
    device_name = models.CharField(max_length=100)
    # device_type = models.CharField(max_length=3, choices=DEVICE_TYPE)
    device_mac = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.device_name


class BluetoothService(models.Model):
    """ This table will store discovered bluetooth services """
    sensor = models.CharField(max_length=100, default="laptopsensor")
    host = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    provider = models.CharField(max_length=100, blank=True, null=True)
    protocol = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    service_classes = models.CharField(max_length=100, blank=True, null=True)
    profiles = models.CharField(max_length=100, blank=True, null=True)
    service_id = models.CharField(max_length=100, blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.host

class CVETable(models.Model):
    cvename = models.CharField(max_length=100, blank=False, null=False)
    data = models.JSONField()

    def __str__(self):
        return self.cvename

