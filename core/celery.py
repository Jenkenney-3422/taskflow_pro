import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('taskflow_pro')

# Read config from Django settings using the 'CELERY' namespace
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically find tasks.py in your apps
app.autodiscover_tasks()