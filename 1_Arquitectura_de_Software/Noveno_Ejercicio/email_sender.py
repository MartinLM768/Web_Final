import time

def enviar_correo(destinatario, asunto, cuerpo):
    print(f"Enviando correo a {destinatario}...")
    time.sleep(2)  # Simula retraso
    print(f"Correo enviado a {destinatario} con asunto: {asunto}")
