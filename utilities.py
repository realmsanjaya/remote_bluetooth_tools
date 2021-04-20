import bluetooth
from faker import Faker
from random import choice

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
    SENSORS = ['TEST-SENSOR001', 'TEST-SENSOR002', 'TEST-SENSOR003', 'TEST-SENSOR004',]
    DEVICE_TYPE = ['BS', 'PH', 'HS', 'IOT']
    sensor = choice(SENSORS)
    device_name = fake_data.android_platform_token()
    device_type = choice(DEVICE_TYPE)
    device_mac = fake_data.mac_address()
    device = {'sensor': sensor, 'device_name': device_name, 'device_type': device_type, 'device_mac': device_mac}
    return device

# testing this function that uses pybluez bluetooth.find_service
def list_services():
    """  This function lists Bluetooth services found for a device """
    services = bluetooth.discover_devices(lookup_names=True)
    print(services)
    pass