from django.forms import ModelForm
from home.models import BluetoothDevice

class DeviceForm(ModelForm):
    class Meta:
        model = BluetoothDevice
        fields = ['sensor', 'device_name', 'device_mac', 'location']