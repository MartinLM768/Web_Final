from celery import shared_task
import redis

redis_client = redis.Redis()

@shared_task
def notificar_pasajero(trip_id, pasajero_id):
    mensaje = f"Tu viaje {trip_id} ha sido aceptado"
    redis_client.publish(f"notificaciones_{pasajero_id}", mensaje)
    print(f"Notificación enviada al pasajero {pasajero_id}")
