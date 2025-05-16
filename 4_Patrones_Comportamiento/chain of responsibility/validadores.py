# validadores.py
import re
from validador import Validador

correos_registrados = ["juanita@gmail.com", "johan@gmail.com", "santiago@gmail.com"]

class ValidarCamposVacios(Validador):
    def manejar(self, datos):
        if not datos["Nombre"] or not datos["Correo"]:
            print("Error: Tienes que completar los campos para continuar.")
            return False
        return super().manejar(datos)

class ValidarFormatoCorreo(Validador):
    def manejar(self, datos):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", datos["Correo"]):
            print("Error: Formato de correo inválido.")
            return False
        return super().manejar(datos)

class ValidarDuplicado(Validador):
    def manejar(self, datos):
        if datos["Correo"] in correos_registrados:
            print("Error: Este correo ya existe.")
            return False
        return super().manejar(datos)
