import os

from celery import Celery, shared_task
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GetEthereum.settings')

app = Celery('GetEthereum')

app.config_from_object('django.conf:settings')

# response = app.control.enable_events(reply=True)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
app.control.inspect().active()

# Task settings
app.conf.task_serializer = settings.CELERY_TASK_SERIALIZER
app.conf.task_acks_late = settings.CELERY_TASK_ACKS_LATE
app.conf.task_reject_on_worker_lost = settings.CELERY_TASK_REJECT_ON_WORKER_LOST
app.conf.task_time_limit = settings.CELERY_TASK_TIME_LIMIT
app.conf.task_soft_time_limit = settings.CELERY_TASK_SOFT_TIME_LIMIT
app.conf.task_always_eager = settings.CELERY_TASK_ALWAYS_EAGER

# Event settings
app.conf.event_queue_ttl = settings.CELERY_EVENT_QUEUE_EXPIRES
app.conf.event_queue_expires = settings.CELERY_EVENT_QUEUE_TTL

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
    }, 'purge_task': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.000000000000000001,
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
