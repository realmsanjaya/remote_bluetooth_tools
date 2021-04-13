import json
import requests
from utilities import gen_devices
import bluetooth


class Client:
    def __init__(self, sensor_name):
        self.sensor_name = sensor_name
        self.server = "http://127.0.0.1:8000/api/bluetoothdevices/"

    def test_server(self):
        """ This method is used to simulate a client  """
        # Set constants
        URL = self.server
        DEVICE = gen_devices()
        r = requests.post(URL, data = DEVICE)
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


# if __name__ == '__main__':
#     test_server()
