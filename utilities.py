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
    #services = bluetooth.discover_devices(lookup_names=True)
    services = [{'service-classes': ['1801'], 'profiles': [], 'name': None, 'description': None, 'provider': None, 'service-id': None, 'protocol': 'L2CAP', 'port': 31, 'host': '5C:49:7D:70:2B:F7'}, {'service-classes': ['1800'], 'profiles': [], 'name': None, 'description': None, 'provider': None, 'service-id': None, 'protocol': 'L2CAP', 'port': 31, 'host': '5C:49:7D:70:2B:F7'}, {'service-classes': ['110C'], 'profiles': [('110E', 261)], 'name': 'Samsung Smart TV Audio', 'description': None, 'provider': '00001', 'service-id': None, 'protocol': 'L2CAP', 'port': 23, 'host': '5C:49:7D:70:2B:F7'}, {'service-classes': ['110A'], 'profiles': [('110D', 258)], 'name': 'Advanced Audio Source', 'description': None, 'provider': None, 'service-id': None, 'protocol': 'L2CAP', 'port': 25, 'host': '5C:49:7D:70:2B:F7'}, {'service-classes': ['110E', '110F'], 'profiles': [('110E', 261)], 'name': None, 'description': None, 'provider': None, 'service-id': None, 'protocol': 'L2CAP', 'port': 23, 'host': '5C:49:7D:70:2B:F7'}, {'service-classes': ['00001101-0000-1000-8000-00805F9B3411'], 'profiles': [], 'name': ':1.00000000000000024841', 'description': None, 'provider': None, 'service-id': None, 'protocol': 'RFCOMM', 'port': 2, 'host': '5C:49:7D:70:2B:F7'}]
    print(services)
    return services