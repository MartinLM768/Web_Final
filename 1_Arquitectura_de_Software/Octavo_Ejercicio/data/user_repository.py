# Simula una base de datos en memoria
_users = {}

def save_user(user):
    if user.username in _users:
        raise ValueError("El usuario ya existe")
    _users[user.username] = user

def get_user_by_username(username):
    return _users.get(username)
