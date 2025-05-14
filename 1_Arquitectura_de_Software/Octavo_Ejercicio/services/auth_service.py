import bcrypt
from models.user import User
from data.user_repository import save_user, get_user_by_username

def register_user(username, password):
    if get_user_by_username(username):
        return False, "Usuario ya existe"
    
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    user = User(username, hashed)
    save_user(user)
    return True, "Registro exitoso"

def login_user(username, password):
    user = get_user_by_username(username)
    if not user:
        return False, "Usuario no encontrado"

    if bcrypt.checkpw(password.encode(), user.password_hash):
        return True, "Inicio de sesión exitoso"
    else:
        return False, "Contraseña incorrecta"
