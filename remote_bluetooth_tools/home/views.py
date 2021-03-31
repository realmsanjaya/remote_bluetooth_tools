from django.shortcuts import render
from .models import BluetoothDevice
#from django.http import HttpResponse

# Create your views here.

def index(request):
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