from django.shortcuts import render
from .models import BluetoothDevice
from rest_framework import viewsets
from .serializers import BluetoothDeviceSerializer

#from django.http import HttpResponse

# Create your views here.

def index(request): #Function based view
    devices = BluetoothDevice.objects.all()
    return render(request, 'home/index.html', {'devices': devices})


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