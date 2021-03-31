from django.contrib import admin
from .models import Person, BluetoothDevice


# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass

@admin.register(BluetoothDevice)
class BluetoothDeviceAdmin(admin.ModelAdmin):
    pass