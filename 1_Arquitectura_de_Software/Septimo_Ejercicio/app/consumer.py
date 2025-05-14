import redis

redis_client = redis.Redis()
pubsub = redis_client.pubsub()
pasajero_id = 45
canal = f"notificaciones_{pasajero_id}"

pubsub.subscribe(canal)
print(f"Escuchando notificaciones en {canal}...")

for mensaje in pubsub.listen():
    if mensaje['type'] == 'message':
        print(f"[Pasajero {pasajero_id}] {mensaje['data'].decode()}")
