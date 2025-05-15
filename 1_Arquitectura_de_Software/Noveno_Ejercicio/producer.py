import pika
import json

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='correos')

# Lista de correos masivos
correos = [
    {"to": "usuario1@example.com", "subject": "Promo 1", "body": "Hola 1"},
    {"to": "usuario2@example.com", "subject": "Promo 2", "body": "Hola 2"},
    {"to": "usuario3@example.com", "subject": "Promo 3", "body": "Hola 3"},
]

for correo in correos:
    channel.basic_publish(
        exchange='',
        routing_key='correos',
        body=json.dumps(correo)
    )
    print(f"[x] Enviado a cola: {correo['to']}")

connection.close()
