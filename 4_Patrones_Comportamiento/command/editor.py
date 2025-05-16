
class EditorTexto:
    def __init__(self):
        self.texto=""

    def agregar(self, nuevo_texto):
        self.texto+=nuevo_texto

    def borrar(self, cantidad):
        self.texto=self.texto[:-cantidad]

    def mostrar(self):
        print("", self.texto)
