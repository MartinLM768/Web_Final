from celery import Celery

app = Celery('uber_event_app', broker='redis://localhost:6379/0')

app.conf.task_routes = {
    'app.tasks.notificar_pasajero': {'queue': 'notificaciones'}
}
