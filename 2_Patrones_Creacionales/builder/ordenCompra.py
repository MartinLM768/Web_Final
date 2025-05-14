class OrdenCompra:
    def __init__(self, id, cliente, fecha, productos, descuento=0, envio=False):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
        self.productos = productos
        self.descuento = descuento
        self.envio = envio

    def mostrar(self):
        print("Orden de Compra")
        print(f"ID: {self.id}")
        print(f"Cliente: {self.cliente}")
        print(f"Fecha: {self.fecha}")
        print(f"Productos: {self.productos}")
        print(f"Descuento: {self.descuento}%")
        print(f"¿Envío incluido? {'Sí' if self.envio else 'No'}")
