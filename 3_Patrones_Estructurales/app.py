from tkinter import Tk
from element import Element
from conteiner import Container

ventana=Tk()
ventana.title("Interfaz grafica, con patron composite")
ventana.geometry("400x300")

boton_aceptar=Element("Boton", "Aceptar")
boton_cancelar=Element("Boton", "Cancelar")
campo_nombre=Element("Coton", "Nombre")

panel=Container("Formulario principal")
panel.agregar(campo_nombre)
panel.agregar(boton_aceptar)


subpanel=Container("Opciones")
subpanel.agregar(Element("Boton", "Cancelar"))
panel.agregar(subpanel)

panel.mostrar(ventana)

ventana.mainloop()
