"""remote_bluetooth_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from home import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'bluetoothdevices', views.BlueToothDeviceViewSet)
router.register(r'bluetoothservices', views.BlueToothServiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('debug/', views.debug, name='debug'),
    path('playground/', views.playground, name='playground'),
    path('devices/', views.devices, name='devices'),
    path('vulnerabilities/', views.vulnerabilities, name='vulnerabilities'),
    path('vulnerability_detail/<str:cveid>', views.vulnerability_detail, name='vulnerability_detail'),
    # path('api/', views.api, name='api')
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_api'))
]
