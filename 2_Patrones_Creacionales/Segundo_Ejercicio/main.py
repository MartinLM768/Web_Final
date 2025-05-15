from factory_usuarios import UsuarioFactory

usuario1 = UsuarioFactory.crear_usuario("cliente", "Ana")
usuario2 = UsuarioFactory.crear_usuario("administrador", "Luis")
usuario3 = UsuarioFactory.crear_usuario("operador", "María")

print(usuario1.mostrar_perfil())
print(usuario1.hacer_pedido())

print(usuario2.mostrar_perfil())
print(usuario2.ver_reportes())

print(usuario3.mostrar_perfil())
print(usuario3.coordinar_envio())
