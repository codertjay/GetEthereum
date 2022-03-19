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
    'add-every-30-seconds1': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.2,
    },
    'add-every-30-seconds2': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.2,
    },
    'add-every-30-seconds3': {
        'task': 'fetch_api.tasks.send_eth3',
        'schedule': 0.2,
    },
    'add-every-30-seconds4': {
        'task': 'fetch_api.tasks.send_eth4',
        'schedule': 0.5,
    },
    'add-every-30-seconds4_1': {
        'task': 'fetch_api.tasks.send_eth2_test1',
        'schedule': 0.2,
    }, 'add-every-30-seconds4_2': {
        'task': 'fetch_api.tasks.send_eth2_test2',
        'schedule': 0.2,
    }, 'add-every-30-seconds4_2_3': {
        'task': 'fetch_api.tasks.send_eth3_test',
        'schedule': 0.2,
    },'add-every-30-seconds4a_2_3': {
        'task': 'fetch_api.tasks.send_eth4_2',
        'schedule': 0.2,
    },
}


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
