from abc import ABC, abstractmethod

class Estrategia(ABC):
    @abstractmethod
    def ordenar(self, productos):
        pass

class OrdenarPorPrecio(Estrategia):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.precio)

class OrdenarPorPopularidad(Estrategia):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.popularidad, reverse=True)

class OrdenarPorFecha(Estrategia):
    def ordenar(self, productos):
        return sorted(productos, key=lambda p: p.fecha)

    def set_estrategia(self, estrategia):
        self.estrategia = estrategia

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        ordenados = self.estrategia.ordenar(self.productos)
        for p in ordenados:
            print(p)
