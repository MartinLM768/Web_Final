from basededatos import BaseDeDatos

class BaseDeDatosReal(BaseDeDatos):
    def __init__(self):
        self.datos=["Johan", "Martín", "Breimar", "Santiago Q.", "Santiago I." ]

    def leer_datos(self):
        print("Datos actuales ya existentes:")
        for d in self.datos:
            print(f"- {d}")

    def insertar_datos(self, dato):
        self.datos.append(dato)
        print(f"Dato insertado: {dato}")

    def eliminar_datos(self, indice):
        if 0<=indice<len(self.datos):
            eliminado=self.datos.pop(indice)
            print(f"Dato eliminado: {eliminado}")
        else:
            print("Índice fuera de rango.")

    def buscar_dato(self, palabra_clave):
        print(f"Buscando '{palabra_clave}' en la base de datos...")
        encontrados = [d for d in self.datos if palabra_clave.lower() in d.lower()]
        if encontrados:
            print("Resultados encontrados:")
            for d in encontrados:
                print(f"- {d}")
        else:
            print("No se encontró ningún dato que coincida.")
