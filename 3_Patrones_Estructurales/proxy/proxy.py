from basededatos import BaseDeDatos
from basededatosadmin import BaseDeDatosReal

class ProxyBaseDeDatos(BaseDeDatos):
    def __init__(self, usuario):
        self.usuario = usuario
        self.bd_real = BaseDeDatosReal()

    def leer_datos(self):
        self.bd_real.leer_datos()

    def insertar_datos(self, dato):
        if self.usuario == "admin":
            self.bd_real.insertar_datos(dato)
        else:
            print("No tienes acceso para añadir datos nuevos.")

    def eliminar_datos(self, indice):
        if self.usuario == "admin":
            self.bd_real.eliminar_datos(indice)
        else:
            print("No tienes acceso para eliminar datos.")
     
    def buscar_dato(self, palabra_clave):
        self.bd_real.buscar_dato(palabra_clave)