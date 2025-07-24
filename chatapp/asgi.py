"""
ASGI config for chatapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application


from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

import app.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatapp.settings')




print("ASGI application is starting...")
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # initializes Django
    "websocket": AuthMiddlewareStack(
        URLRouter(
            app.routing.websocket_urlpatterns
        )
    ),
})
