from abc import ABC, abstractmethod

# Clase base abstracta
class Usuario(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def mostrar_perfil(self):
        pass

# Clase Cliente
class Cliente(Usuario):
    def mostrar_perfil(self):
        return f"[Cliente] {self.nombre}: puede hacer pedidos."

    def hacer_pedido(self):
        return f"{self.nombre} está haciendo un pedido."

# Clase Administrador
class Administrador(Usuario):
    def mostrar_perfil(self):
        return f"[Administrador] {self.nombre}: puede gestionar el sistema."

    def ver_reportes(self):
        return f"{self.nombre} está viendo los reportes del sistema."

# Clase Operador
class Operador(Usuario):
    def mostrar_perfil(self):
        return f"[Operador] {self.nombre}: puede coordinar entregas."

    def coordinar_envio(self):
        return f"{self.nombre} está coordinando un envío."

# Fábrica de usuarios
class UsuarioFactory:
    @staticmethod
    def crear_usuario(tipo, nombre):
        if tipo == "cliente":
            return Cliente(nombre)
        elif tipo == "administrador":
            return Administrador(nombre)
        elif tipo == "operador":
            return Operador(nombre)
        else:
            raise ValueError(f"Tipo de usuario desconocido: {tipo}")

