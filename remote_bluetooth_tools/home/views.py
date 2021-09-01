from django.shortcuts import render
from .models import BluetoothDevice, BluetoothService
from rest_framework import viewsets
from .serializers import BluetoothDeviceSerializer, BluetoothServiceSerializer

#from django.http import HttpResponse

# Create your views here.

def index(request): #Function based view
    devices = BluetoothDevice.objects.all()
    return render(request, 'home/index.html', {'devices': devices})

def vulnerabilities(request):
    return render(request, 'home/vulnerabilities.html')


def about(request):
    return render(request, 'home/about.html')


def debug(request):
    return render(request, 'home/debug.html')

def playground(request):
    devices = BluetoothDevice.objects.all()
    return render(request, 'home/playground.html', 
    {'devices':devices})

def api(request):
    message = {'message': 'Hello World'}
    return render(request, context=message)

class BlueToothDeviceViewSet(viewsets.ModelViewSet):
    """ This will allow the view of bluetooth devices """
    queryset = BluetoothDevice.objects.all()
    serializer_class = BluetoothDeviceSerializer

# testing Bluetooth Device Service View
class BlueToothServiceViewSet(viewsets.ModelViewSet):
    """ This will allow the view of bluetooth services on a device """
    queryset = BluetoothService.objects.all()
    serializer_class = BluetoothServiceSerializer