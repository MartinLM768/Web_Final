from proxy import ProxyBaseDeDatos

print("Usuario invitado:")
invitado=ProxyBaseDeDatos("invitado")
invitado.leer_datos()
invitado.insertar_datos("Juanita")
invitado.eliminar_datos(1)

print("Usuario admin:")
admin=ProxyBaseDeDatos("admin")
admin.leer_datos()
admin.insertar_datos("Petrico")
admin.eliminar_datos(0)

print("Búsqueda con invitado:")
invitado.buscar_dato("Johan")

print("Búsqueda con admin:")
admin.buscar_dato("Petrico")
