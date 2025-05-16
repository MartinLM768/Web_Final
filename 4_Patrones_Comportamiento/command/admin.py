class AdministradorComandos:
    def __init__(self):
        self.historial=[]
        self.rehacer_pila=[]

    def ejecutar(self, comando):
        comando.ejecutar()
        self.historial.append(comando)
        self.rehacer_pila.clear()

    def deshacer(self):
        if self.historial:
            comando=self.historial.pop()
            comando.deshacer()
            self.rehacer_pila.append(comando)
        else:
            print(" No nay nada que se pueda deshacer.")

    def rehacer(self):
        if self.rehacer_pila:
            comando=self.rehacer_pila.pop()
            comando.ejecutar()
            self.historial.append(comando)
        else:
            print("No hay nada que se pueda rehacer.")
