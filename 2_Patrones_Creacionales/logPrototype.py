import copy

class Log:
    def __init__(self, tipo, mensaje, origen):
        self.tipo=tipo
        self.mensaje=mensaje
        self.origen=origen

    def clonar(self):
        return copy.deepcopy(self)
    
    def mostrar(self):
        print(f"[{self.tipo}] - {self.origen}: {self.mensaje}")