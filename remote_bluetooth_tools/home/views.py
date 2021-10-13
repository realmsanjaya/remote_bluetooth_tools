from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BluetoothDevice, BluetoothService, CVETable, VulnerableTable
from rest_framework import viewsets
from .serializers import BluetoothDeviceSerializer, BluetoothServiceSerializer
from .datascraper import Scraper
from .backgroundscraper import BackgroundScraper
from .forms import DeviceForm

#from django.http import HttpResponse

# Create your views here.

def index(request): #Function based view
    devices = BluetoothDevice.objects.all()
    vulnerabilities = VulnerableTable.objects.all()
    context = {'devices': devices, 'vulnerabilities': vulnerabilities}
    return render(request, 'home/index.html', context )

def vulnerabilities(request):
    vulns = CVETable.objects.all() #Added this
    # data = Scraper()
    # vulns = data.get_cves_details()
    count = len(vulns)
    return render(request, 'home/vulnerabilities.html',
    {'vulns':vulns,'count':count})


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

def vulnerability_detail(request, cveid):
    cve = cveid
    data = Scraper()
    vuln = data.vulnerability_detail(cveid=cve)
    return render(request, 'home/vulnerabilities_detail.html',
    {'vuln':vuln})

def devices(request):
    # Empty lists
    all_devices = []
    location = []
    sensor = []
    nodes = []
    links = []


    # Database Query
    devices = BluetoothDevice.objects.all()
    # Logic
    ## Query devices to populate our lists
    for device in devices:
        location.append(device.location)
        sensor.append(device.sensor)
        all_devices.append(device.device_name)

    ## Unique data (Location, Sensors)
    unique_location = list(set(location))
    unique_sensor = list(set(sensor))

    ### Populate node list with the unique location
    for location in unique_location:
        all_devices.append(location)

    ## Populate node list with the unique sensor
    for sensor in unique_sensor:
        all_devices.append(sensor)

    ## Populatine node list with all devices
    for device in all_devices:
        n = {}
        n["name"] = device
        nodes.append(n)

    # Create the Links
    for device in devices:
        # Building to Sensor
        source_node_building = all_devices.index(device.location)
        target_node_sensor = all_devices.index(device.sensor)
        b = {}
        b["source"] = source_node_building
        b["target"] = target_node_sensor
        links.append(b)

        # Sensor to Devices
        source_node_sensor = all_devices.index(device.sensor)
        target_node_device = all_devices.index(device.device_name)
        s = {}
        s["source"] = source_node_sensor
        s["target"] = target_node_device
        links.append(s)
 
    # Export JSON Feed
    data = {"nodes": nodes, "links": links, "location":  unique_location, "sensor": unique_sensor, "all_devices": all_devices }
    return JsonResponse(data)

class BlueToothDeviceViewSet(viewsets.ModelViewSet):
    """ This will allow the view of bluetooth devices """
    queryset = BluetoothDevice.objects.all()
    serializer_class = BluetoothDeviceSerializer

# testing Bluetooth Device Service View
class BlueToothServiceViewSet(viewsets.ModelViewSet):
    """ This will allow the view of bluetooth services on a device """
    queryset = BluetoothService.objects.all()
    serializer_class = BluetoothServiceSerializer


def update_bluetooth_database(request):
    data = BackgroundScraper()
    data.pull_cve_bluetooth()
    return redirect('vulnerabilities')

def add_device(request):
    form = DeviceForm()
    context = {'form': form}
    return render(request, 'home/add_device.html', context)