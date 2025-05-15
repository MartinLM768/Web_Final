import pika
import json
from email_sender import enviar_correo

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='correos')

def callback(ch, method, properties, body):
    data = json.loads(body)
    enviar_correo(data['to'], data['subject'], data['body'])
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='correos', on_message_callback=callback)

print("[*] Esperando mensajes. Presiona Ctrl+C para salir")
channel.start_consuming()
