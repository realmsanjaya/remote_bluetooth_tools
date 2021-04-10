import bluetooth
from faker import Faker

# Shows us bluetooth devices nearby
def find_bluetooth():
    """ This function finds the nearby bluetooth devices """
    devices = bluetooth.discover_devices(lookup_names=True)
    print(devices)


# find_bluetooth()


# Generate Random Bluetooth Devices
def gen_devices():
    """ This function generates the desired number of fake devices """
    fake_data = Faker()
    DEVICE_TYPE = ['BS', 'PH', 'HS', 'IOT']
    device_name = fake_data.android_platform_token()
    device_type = 'BS'
    device_mac = fake_data.mac_address()
    device = {'device_name': device_name, 'device_type': device_type, 'device_mac': device_mac}
    return device