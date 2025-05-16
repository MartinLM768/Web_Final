from abc import ABC, abstractmethod

class BaseDeDatos(ABC):
    @abstractmethod
    def leer_datos(self):
        pass

    @abstractmethod
    def insertar_datos(self, dato):
        pass

    @abstractmethod
    def eliminar_datos(self, indice):
        pass

    @abstractmethod
    def buscar_dato(self, palabra_clave):
        pass