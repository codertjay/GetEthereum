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

Second = {
    'add-every-30-seconds1__h': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.0000000000000000001,
    }, 'add-every-30-seconds1_0_': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.0000000000000000001,
    }, 'add-every-30-seconds1_j__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.0000000000000000001,
    }, 'add-every-30-seconds1_hj__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.0000000000000000001,
    }, 'add-every-30-secondsg1_j__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.0000000000000000001,
    },
    'add-every-30-seconds1': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.0000000000000001,
    }, 'add-every-30-seconds1__0': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.0000000000000001,
    }, 'add-every-30-seconds1_': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.000000000000000001,
    }, 'add-every-30-seconds1___': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.000000000000000001,
    },
}
app.conf.beat_schedule = Second


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
