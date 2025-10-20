from DBManager import DBManager

class ClientesManager:
    def __init__(self):
        self.db = DBManager()

    def obtener_clientes(self):
        res = self.db.cursor.execute("SELECT * FROM cliente").fetchall()
        return [dict(row) for row in res]

    def obtener_cliente(self, id: int):
        res = self.db.cursor.execute("SELECT * FROM cliente WHERE id = ?", (id,)).fetchone()
        if res:
            return dict (res)
        return {"error": f"No se encontró cliente con id {id}"}

    def crear_cliente(self, nombre: str):
        self.db.cursor.execute("INSERT INTO cliente (nombre) VALUES (?)", (nombre,))
        self.db.connection.commit()
        return {"mensaje": "Cliente creado"}

    def modificar_cliente(self, id: int, nombre: str):
        self.db.cursor.execute("UPDATE cliente SET nombre = ? WHERE id = ?", (nombre, id))
        self.db.connection.commit()
        return {"mensaje": "Cliente modificado"}

    def eliminar_cliente(self, id: int):
        self.db.cursor.execute("DELETE FROM cliente WHERE id = ?", (id,))
        self.db.connection.commit()
        return {"mensaje": "Cliente eliminado"}