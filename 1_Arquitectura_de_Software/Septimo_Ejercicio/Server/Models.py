from django.db import models

class Viaje(models.Model):
    pasajero_id = models.IntegerField()
    conductor_id = models.IntegerField()
    estado = models.CharField(max_length=50, default="solicitado")