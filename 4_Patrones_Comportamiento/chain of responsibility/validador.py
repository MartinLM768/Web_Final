class Validador:
    def __init__(self):
        self.siguiente=None

    def enlazar(self, siguiente):
        self.siguiente=siguiente
        return siguiente

    def manejar(self, datos):
        if self.siguiente:
            return self.siguiente.manejar(datos)
        return True
