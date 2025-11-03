import psycopg
from DBManager import DBManager
from models.models import Producto

class ProductosManager:
    def obtener_productos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT * FROM Producto").fetchall()
        return [
            {"id_producto": row[0], "nombre": row[1], "precio": row[2], "cantidad": row[3]} for row in res
            ]
    
    def crear_producto(self, producto: Producto,cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO producto (nombre, precio, cantidad) VALUES (%s,%s,%s)",
            (producto.nombre, producto.precio, producto.cantidad)
            
        )
        return {"Producto creado"}
    
