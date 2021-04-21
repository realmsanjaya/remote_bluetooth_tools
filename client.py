import json
import requests
from utilities import gen_devices, list_services
import bluetooth


class Client:
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name
        self.server = "http://127.0.0.1:8000/api/"

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

    def start_scan(self):
        """ Used to start a scan for bluetooth device """
        # enable bluetooth
        # scan for devices
        # return device information in a json format
        devices = bluetooth.discover_devices(lookup_names=True)
        for addr, name in devices:
            print(f"Address: {addr}, Name: {name}")
        return f'make something cool {self.device_name}'

    def find_services(self):
        """ This method is used to find bluetooth services """
        URL = self.server
        ENDPOINT = 'bluetoothservices/'
        API = URL + ENDPOINT
        for service in list_services():
            data = {
                "host": service['host'],
                "name": "devicename",
                "description": service['description'],
                "provider": service['provider'],
                "protocol": service['protocol'],
                "port": service['port'],
                "service_classes": str(service['service-classes']),
                "profiles": str(service['profiles']),
                "service_id": service['service-id']
            }
            r = requests.post(API, data = json.dumps(data))
            print(r.status_code)
            print(json.dumps(data))
        return "Success!"

if __name__ == '__main__':
    #test_server()
    device = Client(sensor_name="raspberry")
    device.find_services()
