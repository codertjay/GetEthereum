celery -A GetEthereum worker --loglevel=info
celery -A GetEthereum beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler