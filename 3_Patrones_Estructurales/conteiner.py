from composite_gui import ComponenteGUI
import tkinter as tk

class Container (ComponenteGUI):
    def __init__(self, nombre):
        self.nombre=nombre
        self.hijos=[]

    def agregar (self, componente):
        self.hijos.append(componente)

    def mostrar(self, padre):
        marco=tk.LabelFrame(padre, text=self.nombre, padx=10, pady=10)
        marco.pack(padx=10, pady=10, fill="both", expand=True)
        for hijo in self.hijos:
            hijo.mostrar(marco)