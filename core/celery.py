

import os
from celery import Celery

# Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# This is the line you were trying to run!
# It tells Celery to look inside the 'tasks_app' folder for a 'tasks.py' file.
app.autodiscover_tasks(['tasks_app'])

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')