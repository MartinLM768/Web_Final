from admin import Producto
from observador import Usuario

laptop = Producto("Teclado pórtatil.")
Johan=Usuario("Johan")
Juanita=Usuario("Juanita")
Santiago=Usuario("Santiago")
laptop.agregar_suscriptor(Johan)
laptop.agregar_suscriptor(Juanita)
laptop.agregar_suscriptor(Santiago)
laptop.quitar_suscriptor(Santiago)
laptop.aplicar_descuento()
