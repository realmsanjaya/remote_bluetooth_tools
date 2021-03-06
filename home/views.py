from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import BluetoothDevice, BluetoothService, CVETable, VulnerableTable
from rest_framework import viewsets
from .serializers import BluetoothDeviceSerializer, BluetoothServiceSerializer
from .datascraper import Scraper
from .backgroundscraper import BackgroundScraper
from .forms import DeviceForm
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse

# Create your views here.

@login_required
def index(request): #Function based view
    devices = BluetoothDevice.objects.all()
    vulnerabilities_list = VulnerableTable.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(vulnerabilities_list, 5)
    try:
        vulnerabilities = paginator.page(page)
    except PageNotAnInteger:
        vulnerabilities = paginator.page(1)
    except EmptyPage:
        vulnerabilities = paginator.page(paginator.num_pages)
    context = {'devices': devices, 'vulnerabilities': vulnerabilities}
    return render(request, 'home/index.html', context )

@login_required
def vulnerabilities(request):
    vulns = CVETable.objects.all() #Added this
    # data = Scraper()
    # vulns = data.get_cves_details()
    count = len(vulns)
    return render(request, 'home/vulnerabilities.html',
    {'vulns':vulns,'count':count})

@login_required
def about(request):
    return render(request, 'home/about.html')

@login_required
def debug(request):
    return render(request, 'home/debug.html')

@login_required
def playground(request):
    devices = BluetoothDevice.objects.all()
    return render(request, 'home/playground.html', 
    {'devices':devices})

@login_required
def api(request):
    message = {'message': 'Hello World'}
    return render(request, context=message)

@login_required
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
        # Create a query for VulnerableTable for the particular device
        #vuln = VulnerableTable.objects.filter(device=1)
        #2 vuln = )
        #print(devices) # TODO: Setup Devices
        #2 print(vuln)
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

@login_required
def update_bluetooth_database(request):
    data = BackgroundScraper()
    data.pull_cve_bluetooth()
    return redirect('vulnerabilities')

def add_device(request):
    form = DeviceForm()
    if request.method == 'POST':
        f = DeviceForm(request.POST)
        if f.is_valid():
            device_name = request.POST.get("device_name")
            f.save()
            device = BluetoothDevice.objects.latest('creation_date')
            cves = CVETable.objects.filter(cve_description__contains=device_name)
            for cve in cves:
                vuln = VulnerableTable(device=device, cve_vulnerability=cve)
                vuln.save()
        # Add data to the database
           
        return redirect('index')
    else:
        context = {'form': form}
        return render(request, 'home/add_device.html', context)

@login_required
def search(request):
    if request.method == "POST":
        q = request.POST.get("search")
        #print(f"DATA: {q}")
        cves = CVETable.objects.filter(cve_description__contains=q)
        count = len(cves)
        context = {"cves":cves, "count":count}
        return render(request, 'home/search.html', context)
    return render(request, 'home/search.html')


class PaginateListView(ListView):
    paginate_by=5
    model = CVETable
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context