from DBManager import DBManager

class ProductosManager:
    def __init__(self):
        self.db = DBManager()

    def obtener_productos(self):
        self.db.cursor.execute("SELECT * FROM producto")
        return [dict(row) for row in self.db.cursor.fetchall()]

    def crear_producto(self, nombre: str, precio: float, cantidad: int):
        self.db.cursor.execute(
            "INSERT INTO producto (nombre, precio, cantidad) VALUES (?, ?, ?)",
            (nombre, precio, cantidad)
        )
        self.db.connection.commit()
        return {"mensaje": "Producto creado"}
    
    def modificar_productos(self, id: int, nombre: str, precio: float, cantidad:int):
        self.db.cursor.execute(
            "UPDATE producto SET nombre = ?, precio = ?, cantidad = ? WHERE id = ?",
            (nombre, precio, cantidad, id))
        self.db.connection.commit()
        return {"mensaje": "Producto modificado"}
    
    def eliminar_producto(self, id: int):
        self.db.cursor.execute("DELETE FROM producto WHERE id = ?", (id,))
        self.db.connection.commit()
        return {"mensaje": "Producto eliminado"}