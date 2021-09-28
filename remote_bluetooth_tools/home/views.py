from django.shortcuts import render
from django.http import JsonResponse
from .models import BluetoothDevice, BluetoothService, CVETable
from rest_framework import viewsets
from .serializers import BluetoothDeviceSerializer, BluetoothServiceSerializer
from .datascraper import Scraper

#from django.http import HttpResponse

# Create your views here.

def index(request): #Function based view
    devices = BluetoothDevice.objects.all()
    return render(request, 'home/index.html', {'devices': devices})

def vulnerabilities(request):
    #vulns = CVETable.objects.all() #Added this
    data = Scraper()
    vulns = data.get_cves_details()
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
    # data = {'nodes':[
    #     {
    #         "id": 1,
    #         "name": "A"
    #     },
    #     {
    #         "id": 2,
    #         "name": "B"
    #     }
    # ], 'links':[
    #     {"source": 1},
    #     {"target": 2}
    # ]}
    device_name = []
    sensor = []
    building = []
    links = []
    devices = BluetoothDevice.objects.all()
    for device in devices:
        d = {}
        d["id"] = device.id
        d["sensor"] = device.sensor
        d["location"] = device.location
        d["name"] = device.device_name
        d["device_mac"] = device.device_mac
        d["creation_date"] = device.creation_date
        device_name.append(d)
        sensor.append(device.sensor)
        building.append(device.location)
    # Associate the Building with the Sensor
    for device in devices:
        if device.location in building:
            l = {}
            l['sensor'] = device.sensor
            print(set(l))

    # Deduplicates the data
    # TODO: Take each node, building, and sensor and output the JSON needed.
    unique_building = set(building)
    unique_sensor = set(sensor)
    total_nodes = device_name
    data = {"nodes": total_nodes, "sensor": list(unique_sensor), "building": list(unique_building), "links": [] }
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
