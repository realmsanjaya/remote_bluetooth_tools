import json
import requests
from utilities import gen_devices

def test_server():
    """ This function is used to simulate a client  """
    # Set constants
    URL = "http://127.0.0.1:8000/api/bluetoothdevices/"
    DEVICE = gen_devices()
    r = requests.post(URL, data = DEVICE)
    print(r.status_code)
    return f"Success"

if __name__ == '__main__':
    test_server()


# """
# import bluetooth

# class Client:
#     def __init__(self, device_name):
#         self.device_name = device_name

#     def start_scan(self):
#         """ Used to start a scan for bluetooth device """
#         # enable bluetooth
#         # scan for devices
#         # return device information in a json format
#         devices = bluetooth.discover_devices(lookup_names=True)
#         for addr, name in devices:
#             print(f"Address: {addr}, Name: {name}")
#         return f'make something cool {self.device_name}'

# # Data Structure
# data = {'device_id': 'raspberrypi', 'devices': [('E0:D1:E6:04:F4:F9', 'MINIJAMBOX by Jawbone')] }

# # Run program
# client1 = Client(device_name="raspberrypi")
# client1.start_scan()

# """