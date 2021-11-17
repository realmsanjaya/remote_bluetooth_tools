import datetime
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    cve_id = models.CharField(max_length=100, blank=False, null=False)
    cve_description = models.TextField(max_length=500, blank=False, null=False)
    data = models.JSONField()

    def __str__(self):
        return self.cve_id


class VulnerableTable(models.Model):
    device = models.ForeignKey(BluetoothDevice, on_delete=models.CASCADE, null=True)
    cve_vulnerability = models.ForeignKey(CVETable, on_delete=models.CASCADE, null=True)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Device: {self.device}-- Vulnerability: {self.cve_vulnerability}"

@receiver(post_save, sender=BluetoothDevice)
def search_vulnerabilities(sender, instance, **kwargs):
    # Logic goes here
    print(f"Instance: {instance.device_name}")
    # Code that does the query to find vulnerabilities based on name
    device_name = instance
    cves = CVETable.objects.filter(cve_description__contains=device_name)
    for cve in cves:
        vuln = VulnerableTable(device=device_name, cve_vulnerability=cve)
        vuln.save()
