from datetime import datetime

class Producto:
    def __init__(self, nombre, precio, popularidad, fecha):
        self.nombre = nombre
        self.precio = precio
        self.popularidad = popularidad
        self.fecha = datetime.strptime(fecha, "%d/%m/%Y")

    def __str__(self):
        fecha_str = self.fecha.strftime("%d/%m/%Y")
        return f"{self.nombre} - ${self.precio} - Popularidad: {self.popularidad} - Fecha: {fecha_str}"
