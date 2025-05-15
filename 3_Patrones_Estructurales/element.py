from composite_gui import ComponenteGUI
import tkinter as tk

class Element (ComponenteGUI):
    def __init__(self, tipo ,texto):
        self.tipo=tipo
        self.texto=texto
    def mostrar(self, padre):
        if self.tipo=="Boton":
            boton=tk.Button(padre, text=self.texto, width=20)
            boton.pack(pady=5)
        elif self.tipo=="Campo":
            contenedor=tk.Frame(padre)
            contenedor.pack(pady=5, fill="x")
            etiqueta=tk.Label(padre, text=self.texto)
            etiqueta.pack(side="left", padx=5)
            etiqueta.pack(pady=(10, 10))
            entrada=tk.Entry(contenedor)
            entrada.pack(side="left", expand=True, fill="x", pady=(5))