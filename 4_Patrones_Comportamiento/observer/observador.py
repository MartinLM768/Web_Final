class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre

    def recibir_notificacion(self, producto):
        print(f"{self.nombre}, el producto '{producto}' tiene un 40% de descuento hoy. ¡Aprovecha!")
