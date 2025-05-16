class Formulario:
    def __init__(self, Nombre, Correo):
        self.nombre=Nombre
        self.correo=Correo

    def obtener_datos(self):
        return {
            "Nombre":self.nombre,
            "Correo":self.correo
        }
