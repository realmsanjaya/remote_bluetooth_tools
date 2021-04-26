from django.contrib import admin
from .models import Person, BluetoothDevice, BluetoothService


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(BluetoothDevice)
class BluetoothDeviceAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'device_name', 'device_mac', 'creation_date']
    # pass

@admin.register(BluetoothService)
class BluetoothServiceAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'name', 'description', 'host']
    # pass