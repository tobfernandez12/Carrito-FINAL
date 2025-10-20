import sqlite3
import os
from tablas import tablas

class DBManager:
    def __init__(self):
        self.db_name = "basedatos.db"
        self.connection = sqlite3.connect(self.db_name, check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        self.initDB()
        print("Base de datos usada:", os.path.abspath(self.db_name))
    
    def initDB(self):
        for tabla in tablas:
            self.cursor.execute(tabla)
        self.connection.commit()