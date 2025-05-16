from producto import Producto
from newStrategys import OrdenarPorPrecio, OrdenarPorPopularidad, OrdenarPorFecha

productos = [
    Producto("Manzana", 2000, 205, "08/05/2025"),
    Producto("Pera", 800, 146, "10/05/2025"),
    Producto("Sandía", 5000, 353, "14/05/2025")
]

def mostrar_ordenados(productos, estrategia):
    if isinstance(estrategia, OrdenarPorPrecio):
        print("\n Ordenando productos por precio (del más barato al más caro): ")
    elif isinstance(estrategia, OrdenarPorPopularidad):
        print("\n Ordenando productos por popularidad (de mayor popularidad a menor popularidad): ")
    elif isinstance(estrategia, OrdenarPorFecha):
        print("\n Ordenando productos por fecha (de más antigua a más reciente): ")

    ordenados = estrategia.ordenar(productos)
    for p in ordenados:
        print(p)

mostrar_ordenados(productos, OrdenarPorPrecio())
mostrar_ordenados(productos, OrdenarPorPopularidad())
mostrar_ordenados(productos, OrdenarPorFecha())
