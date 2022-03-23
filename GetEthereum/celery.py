import os

from celery import Celery, shared_task
from celery.schedules import crontab
from decouple import config
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GetEthereum.settings')

if config('BROKER_URL') == 'EXIST':
    app = Celery('GetEthereum', broker_url='redis://127.0.0.1:6379/0')
else:
    app = Celery('GetEthereum')

app.config_from_object('django.conf:settings')

# response = app.control.enable_events(reply=True)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
app.control.inspect().active()

# Task settings
app.conf.task_time_limit = 90

# Event settings
app.conf.event_queue_ttl = 60

Second = {
    'add-every-30-seconds1__h': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.01,
    }, 'add-every-30-seconds1_0_': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.01,
    }, 'add-every-30-seconds1_j__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.01,
    }, 'add-every-30-seconds1_hj__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.01,
    }, 'add-every-30-secondsg1_j__': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.01,
    },
    'add-every-30-seconds1': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.01,
    }, 'add-every-30-seconds1__0': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.01,
    }, 'add-every-30-seconds1_': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.01,
    }, 'add-every-30-seconds1___': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.01,
    }, 'purge_task': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.01,
    },

    'celery.backend_cleanup': {
        'task': 'celery.backend_cleanup',
        'schedule': crontab(minute='10'),  # Every hours when minutes = 30 mins
        'options': {'expires': 50 * 60}  # 50 minutes
    },
}
app.conf.beat_schedule = Second


@shared_task()
def purge_task():
    app.control.purge()
    return True


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
