class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.descuento = False
        self.suscriptores = []

    def agregar_suscriptor(self, usuario):
        self.suscriptores.append(usuario)

    def quitar_suscriptor(self, usuario):
        if usuario in self.suscriptores:
            self.suscriptores.remove(usuario)
            print(f"Desafortunadamente, {usuario.nombre} se ha desuscrito.")
        else:
            print(f"Ups, {usuario.nombre} no estaba suscrito.")

    def aplicar_descuento(self):
        self.descuento = True
        self.notificar_suscriptores()

    def notificar_suscriptores(self):
        for usuario in self.suscriptores:
            usuario.recibir_notificacion(self.nombre)
