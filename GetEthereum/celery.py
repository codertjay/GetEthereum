import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GetEthereum.settings')

app = Celery('GetEthereum')

app.config_from_object('django.conf:settings')
response = app.control.enable_events(reply=True)
# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
app.control.inspect().active()

app.conf.beat_schedule = {
    'add-every-60-seconds': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 1,
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
