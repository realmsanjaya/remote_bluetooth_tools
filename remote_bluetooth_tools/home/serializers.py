from rest_framework import serializers
from .models import BluetoothDevice

class BluetoothDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BluetoothDevice
        fields = ['sensor', 'device_name', 'device_type', 'device_mac', 'creation_date']
        # fields = '__all__'

