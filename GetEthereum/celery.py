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

response = app.control.enable_events(reply=True)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(settings.INSTALLED_APPS)
app.control.inspect().active()

Second = {
    'add-every-30-private_transaction_2_dollardd': {
        'task': 'fetch_api.tasks.private_transaction_05_dollar',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-every-30-private_transaction_2_dollar': {
        'task': 'fetch_api.tasks.private_transaction_2_dollar',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-everpy-30-private_transaction_4_dollar': {
        'task': 'fetch_api.tasks.private_transaction_4_dollar',
        'schedule': 0.00000000000000000000000000000001,
    }, 'ladd-every-30-private_transaction': {
        'task': 'fetch_api.tasks.private_transaction',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-every-30-private_transaction_2': {
        'task': 'fetch_api.tasks.private_transaction_2',
        'schedule': 0.00000000000000000000000000000001,
    },
    'add-every-30-seconds1__h': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-every-30-seconds1_0_': {
        'task': 'fetch_api.tasks.send_eth',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-every-30-seconds1_j__': {
        'task': 'fetch_api.tasks.send_eth2',
        'schedule': 0.00000000000000000000000000000001,
    }, 'add-every-30-secjjonds1_j__': {
        'task': 'fetch_api.tasks.send_eth2_second',
        'schedule': 0.00000000000000000000000000000001,
    },
    'celery.backend_cleanup': {
        'task': 'celery.backend_cleanup',
        'schedule': crontab(minute='30'),  # Every hours when minutes = 30 mins
        'options': {'expires': 50 * 60}  # 50 minutes
    },
}
# app.conf.beat_schedule = Second
#
#
# @shared_task()
# def purge_task():
#     app.control.purge()
#     return True
#
#
# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
