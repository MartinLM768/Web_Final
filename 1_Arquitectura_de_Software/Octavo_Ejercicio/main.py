from services.auth_service import register_user, login_user

def mostrar_menu():
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        ok, msg = register_user(user, pwd)
        print(msg)

    elif opcion == "2":
        user = input("Usuario: ")
        pwd = input("Contraseña: ")
        ok, msg = login_user(user, pwd)
        print(msg)

    elif opcion == "3":
        break

    else:
        print("Opción inválida")
