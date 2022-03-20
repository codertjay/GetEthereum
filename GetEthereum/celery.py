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

First = {
    'add-every-30-seconds1': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.02,
    },
    'add-every-30-seconds2': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.02,
    },
    'add-every-30-seconds3': {
        'task': 'fetch_api.tasks.send_eth3',
        'schedule': 0.02,
    },
    'add-every-30-seconds4': {
        'task': 'fetch_api.tasks.send_eth4',
        'schedule': 0.02,
    }
}

Second = {
    'add-every-30-seconds1': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.00001,
    }, 'add-every-30-seconds1_': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.00001,
    },
}
app.conf.beat_schedule = Second


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
