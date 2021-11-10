import json
import requests
# from utilities import gen_devices, list_services
import bluetooth

# Constants
SERVER = 'https://remotebluetoothtools.herokuapp.com/'

class Client:
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name
        self.server = f'{SERVER}api/'

    def test_server(self):
        """ This method is used to simulate a client  """
        # Set constants
        URL = self.server
        ENDPOINT = 'bluetoothdevices'
        DEVICE = gen_devices()
        API = URL + ENDPOINT
        r = requests.post(API, data = DEVICE)
        print(r.status_code)
        return f"Success"

    def test_bluetoothservices(self):
        """ This method is used to find bluetooth services """
        URL = self.server
        ENDPOINT = 'bluetoothservices/'
        API = URL + ENDPOINT
        for service in list_services():
            data = {
                "sensor": self.sensor_name,
                "host": service['host'],
                "name": service['name'],
                "description": service['description'],
                "provider": service['provider'],
                "protocol": service['protocol'],
                "port": service['port'],
                "service_classes": str(service['service-classes']),
                "profiles": str(service['profiles']),
                "service_id": service['service-id']
            }
            # r = requests.post(API, data = json.dumps(data))
            r = requests.post(API, data = data)
            print(r.status_code)
            print(json.dumps(data))
        return "Success!"

    def start_scan(self):
        """ Used to start a scan for bluetooth device """
        # enable bluetooth
        # scan for devices
        # return device information in a json format
        devices = bluetooth.discover_devices(lookup_names=True)
        
        for addr, name in devices:
            data = {
                "sensor": self.sensor_name,
                "device_name": name,
                "device_mac": addr,
            }
            URL = self.server
            ENDPOINT = 'bluetoothdevices/'
            API = URL + ENDPOINT
            r = requests.post(API, data = data)
            print(f"Address: {addr}, Name: {name}")
        return f'Success'

    def find_services(self):
        """ This method is used to find bluetooth services """
        URL = self.server
        ENDPOINT = 'bluetoothservices/'
        API = URL + ENDPOINT
        devices = bluetooth.find_service()
        for service in devices:
            data = {
                "sensor": self.sensor_name,
                "host": service['host'],
                "name": service['name'],
                "description": service['description'],
                "provider": service['provider'],
                "protocol": service['protocol'],
                "port": service['port'],
                "service_classes": str(service['service-classes']),
                "profiles": str(service['profiles']),
                "service_id": service['service-id']
            }
            # r = requests.post(API, data = json.dumps(data))
            r = requests.post(API, data = data)
            print(r.status_code)
            print(json.dumps(data))
        return "Success!"

    def add_bluetooth_device(self, device_name, device_mac, location):
        """ This method will add a device to the bluetooth device database """
        sensor = self.sensor_name
        device_name = device_name
        device_mac = device_mac
        location = location
        device = {'sensor':sensor, 'device_name':device_name, 'device_mac':device_mac, 'location':location, 'creation_date':None}
        api_url = f"{self.server}bluetoothdevices/"
        data = requests.post(api_url, data=device)
        return data


if __name__ == '__main__':
    #test_server()
    device = Client(sensor_name="raspberry")
    # device.test_bluetoothservices()
    # device.start_scan()
    # device.find_services()
    device.add_bluetooth_device(device_name='Zephyr', device_mac='20:20:20:20', location='building01')
