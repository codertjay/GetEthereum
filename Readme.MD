# Celery with Django

## Introduction

This project is just to demonstrate how celery can be integrated with django project to call task asynchronously as well
as synchronously if required. Tasks can also be executed on schedule as well as periodically.

## Process

- Celery configuration
- Write celery task in django app
- Call task asynchronously
- Execute task periodically
- Rabbitmql for Task server

The current project is made using django and Django RestFramework (API)

## setup

- Install Rabbitmql on windows or Linux (https://www.rabbitmq.com/download.html)
- Create a virtualenv
- pip install virtualenv
- virtualenv venv

- Windows
    - venv/Scripts/activate.bat
- Mac
    - Source venv/bin/activate

- pip install -r requirements.txt
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver

## start Rabbitmql server

- rabbitmq-server start

## Run celery for task

- (If on Mac ) celery -A GetEthereum worker --loglevel=info
- (If on Windows) celery -A GetEthereum worker -l info --pool=solo 
- open a new tab then run the command below  for the scheduler
- celery -A GetEthereum beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler


