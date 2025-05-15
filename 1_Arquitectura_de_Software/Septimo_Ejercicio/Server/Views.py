from django.shortcuts import render
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def aceptar_viaje(request, trip_id):
    layer = get_channel_layer()
    async_to_sync(layer.group_send)(
        f"viajes_{trip_id}",
        {"type": "send_notification", "mensaje": "El conductor aceptó tu viaje"}
    )
    return render(request, "index.html")