from ordenBuilder import OrdenBuilder

builder = OrdenBuilder()
orden = (builder
         .set_id(101)
         .set_cliente("Johan Rico")
         .set_fecha("2025-05-13")
         .agregar_producto("Computador")
         .agregar_producto("Teclado")
         .set_descuento(5)
         .incluir_envio(False)
         .construir())

orden.mostrar()
