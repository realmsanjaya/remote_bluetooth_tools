"""
ASGI config for remote_bluetooth_tools project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from home.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'remote_bluetooth_tools.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(URLRouter(ws_urlpatterns))
    }
)