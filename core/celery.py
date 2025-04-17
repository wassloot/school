import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.setting")
app = Celery('config')

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'sender':{
        'task': 'apps.rooms.tasks.send_tg',
        'schedule': crontab(minute=0, hour=8)
    },
    'sender_2':{
        'task': 'app.rooms.tasks.send_tg',
        'schedule': 600
    }

}