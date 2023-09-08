import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
from channels.routing import ProtocolTypeRouter, URLRouter
from stats import routing




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings')

django_asgi_application = get_asgi_application()


application = ProtocolTypeRouter(
    {
        'http': django_asgi_application,
        'websocket': AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
        )
    }
)
