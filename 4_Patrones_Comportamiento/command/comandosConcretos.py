from comando import Comando

class AgregarTexto(Comando):
    def __init__(self, editor, texto):
        self.editor = editor
        self.texto = texto

    def ejecutar(self):
        self.editor.agregar(self.texto)

    def deshacer(self):
        self.editor.borrar(len(self.texto))

class BorrarTexto(Comando):
    def __init__(self, editor, cantidad):
        self.editor=editor
        self.cantidad=cantidad
        self.texto_borrado=""

    def ejecutar(self):
        self.texto_borrado=self.editor.texto[-self.cantidad:]
        self.editor.borrar(self.cantidad)

    def deshacer(self):
        self.editor.agregar(self.texto_borrado)
