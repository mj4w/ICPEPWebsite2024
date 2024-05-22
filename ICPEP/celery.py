import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ICPEP.settings')

app = Celery('ICPEP')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()