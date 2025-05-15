import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, db_path):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    print("Creando nueva conexión a la base de datos...")
                    cls._instance = super(DatabaseConnection, cls).__new__(cls)
                    cls._instance.connection = sqlite3.connect(db_path, check_same_thread=False)
        return cls._instance

    def get_connection(self):
        return self.connection
