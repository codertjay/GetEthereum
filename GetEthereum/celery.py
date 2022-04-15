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
    'automate_send_eth_and_approve_1': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_1',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_2': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_2',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_3': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_3',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_4': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_4',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_5': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_5',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_6': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_6',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_7': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_7',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_8': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_8',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_9': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_9',
        'schedule': 0.00000000000000000000000000000001,
    },'automate_send_eth_and_approve_10': {
        'task': 'approve_send.tasks.automate_send_eth_and_approve_10',
        'schedule': 0.00000000000000000000000000000001,
    },
    'celery.backend_cleanup': {
        'task': 'celery.backend_cleanup',
        'schedule': crontab(minute='30'),  # Every hours when minutes = 30 mins
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
