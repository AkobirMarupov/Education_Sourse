import os
from django.core.wsgi import get_wsgi_application

# STATIC fayllarni serve qilish uchun dj-static qo‘shamiz
from dj_static import Cling, MediaCling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = Cling(MediaCling(get_wsgi_application()))
