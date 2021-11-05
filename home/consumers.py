import json
from random import randint
from time import sleep
from random import choice
from channels.generic.websocket import WebsocketConsumer
from .models import BluetoothDevice

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            message = {'message': randint(1,100)}
            self.send(json.dumps(message))
            sleep(1)


class DeviceConsumer(WebsocketConsumer):
    """ This consumer will be used to stream devices from database """
    
    
    def connect(self):
        self.accept()
        devices = [device.device_name for device in BluetoothDevice.objects.all()]

        for i in range(1000):
            device = choice(devices)
            message = {'device': device, 'message': 'You connected' }
            self.send(json.dumps(message))
            sleep(1)