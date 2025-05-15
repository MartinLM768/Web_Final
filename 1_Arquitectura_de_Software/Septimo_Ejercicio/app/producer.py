from .tasks import notificar_pasajero

def aceptar_viaje(trip_id, pasajero_id):
    # Simula lógica del backend cuando el conductor acepta
    print(f"Conductor aceptó el viaje {trip_id}")
    notificar_pasajero.delay(trip_id, pasajero_id)
