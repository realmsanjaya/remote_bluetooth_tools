import json
from random import randint
from time import sleep
from channels.generic.websocket import WebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        for i in range(1000):
            message = {'message': randint(1,100)}
            self.send(json.dumps(message))
            sleep(1)