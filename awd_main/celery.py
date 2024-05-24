import os
from celery import Celery

#Set the defaut settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE','awd_main.settings')

#new celery app for awd_main app
app = Celery('awd_main')

#configuration key should have 'CELERY_' prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

#load task modules from all apps
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

