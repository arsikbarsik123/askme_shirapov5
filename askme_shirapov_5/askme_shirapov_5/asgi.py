import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askme_shirapov_5.settings')

application = get_asgi_application()
