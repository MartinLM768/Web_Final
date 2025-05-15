import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_driven_app.settings")
app = Celery("event_driven_app")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()    