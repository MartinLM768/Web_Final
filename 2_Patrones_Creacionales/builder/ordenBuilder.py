from ordenCompra import OrdenCompra
class OrdenBuilder:
    def __init__(self):
        self.id = None
        self.cliente = None
        self.fecha = None
        self.productos = []
        self.descuento = 0
        self.envio = False

    def set_id(self, id):
        self.id = id
        return self

    def set_cliente(self, cliente):
        self.cliente = cliente
        return self

    def set_fecha(self, fecha):
        self.fecha = fecha
        return self

    def agregar_producto(self, producto):
        self.productos.append(producto)
        return self

    def set_descuento(self, descuento):
        self.descuento = descuento
        return self

    def incluir_envio(self, envio):
        self.envio = envio
        return self

    def construir(self):
        return OrdenCompra(self.id, self.cliente, self.fecha, self.productos, self.descuento, self.envio)
