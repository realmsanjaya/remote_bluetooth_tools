from django.urls import path

from .consumers import WSConsumer


ws_urlpatterns = [
    path('ws/app/', WSConsumer.as_asgi())
]