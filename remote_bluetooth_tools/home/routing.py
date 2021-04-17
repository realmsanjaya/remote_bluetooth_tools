from django.urls import path

from .consumers import WSConsumer, DeviceConsumer


ws_urlpatterns = [
    path('ws/app/', WSConsumer.as_asgi()),
    path('ws/devices/', DeviceConsumer.as_asgi())
]