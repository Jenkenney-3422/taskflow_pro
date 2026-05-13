import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Get the broker URL from environment variables
broker_url = os.environ.get('CELERY_BROKER_URL', '')

# Logic to handle Render's secure Valkey/Redis connection
if broker_url.startswith('rediss://'):
    app.conf.update(
        broker_use_ssl={'ssl_cert_reqs': 'none'},
        redis_backend_use_ssl={'ssl_cert_reqs': 'none'},
    )

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(['tasks_app'])