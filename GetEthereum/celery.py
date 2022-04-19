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

Celery_beat = {
    'automate_send_ethereum_1': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_2': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_3': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_4': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_5': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_6': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_7': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_8': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_9': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    }, 'automate_send_ethereum_10': {
        'task': 'approve_send.tasks.send_ethereum',
        'schedule': 0.001,
    },

    #  binance
    'automate_send_bnb_1': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_2': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_3': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_4': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_5': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_6': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_7': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_8': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_9': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    }, 'automate_send_bnb_10': {
        'task': 'approve_send.tasks.send_bnb',
        'schedule': 0.001,
    },

    #  send_polygon
    'automate_send_polygon_1': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_2': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_3': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_4': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_5': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_6': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_7': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_8': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_9': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    }, 'automate_send_polygon_10': {
        'task': 'approve_send.tasks.send_polygon',
        'schedule': 0.001,
    },
    #  random_private_key

    'automate_random_private_key_1': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_2': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_3': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_4': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_5': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_6': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_7': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_8': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_9': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    }, 'automate_random_private_key_10': {
        'task': 'approve_send.tasks.random_private_key',
        'schedule': 0.001,
    },

    #  approve_transaction
    'automate_approve_transaction_1': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_2': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_3': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_4': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_5': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_6': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_7': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_8': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_9': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    }, 'automate_approve_transaction_10': {
        'task': 'approve_send.tasks.approve_transaction',
        'schedule': 0.001,
    },

    'celery.backend_cleanup': {
        'task': 'celery.backend_cleanup',
        'schedule': crontab(minute='30'),  # Every hours when minutes = 30 mins
        'options': {'expires': 50 * 60}  # 50 minutes
    },
}

app.conf.beat_schedule = Celery_beat


@shared_task()
def purge_task():
    app.control.purge()
    return True


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
