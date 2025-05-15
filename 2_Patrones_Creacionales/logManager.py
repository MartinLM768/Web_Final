class GestorLogs:
    def __init__(self):
        self._prototipos={}

    def registrar(self, nombre, log):
        self._prototipos[nombre]=log

    def obtener (self, nombre):
        prototipo=self._prototipos.get(nombre)
        return prototipo.clonar() if prototipo else None