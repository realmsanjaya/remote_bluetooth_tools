from rest_framework import serializers
from .models import BluetoothDevice, BluetoothService

class BluetoothDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BluetoothDevice
        fields = ['sensor', 'device_name', 'device_mac', 'creation_date']
        # fields = '__all__'


# testing Bluetooth Service Serializer
class BluetoothServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BluetoothService
        fields = ['host', 'name', 'description', 'provider', 'protocol', 'port', 'service_classes', 'profiles', 'service_id']
        # fields = '__all__'