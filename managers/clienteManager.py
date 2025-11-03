import psycopg
from models.models import Cliente

class ClientesManager:
    def obtener_clientes(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute("SELECT id , nombre FROM cliente").fetchall()
        return [{"id": row[0],"nombre": row[1]} for row in res]

    def obtener_cliente(self, id: int, cursor: psycopg.Cursor):
        print("aca", id, cursor)
        res = cursor.execute("SELECT * FROM cliente WHERE id = %s", (id,)).fetchone()
        if res:
            print(res)
            return {"id": res[0],"nombre":res[1]}
        return {"error": f"No se encontró cliente con id {id}"}

    def crear_cliente(self, cliente: Cliente, cursor: psycopg.Cursor):
        cursor.execute(
            "INSERT INTO cliente (nombre) VALUES (%s)",
            (cliente.nombre,),
        )
        return {"mensaje": "Cliente creado"}

    def modificar_cliente(self, id: int, updatedClient: str, cursor: psycopg.Cursor) -> str:
        cursor.execute(
            "UPDATE cliente SET nombre = %s WHERE id = %s",
            (updatedClient, id),
        )
        
        return {"mensaje": "Cliente modificado"}

    def eliminar_cliente(self, id: int, cursor: psycopg.Cursor) -> str:
        cursor.execute("DELETE FROM cliente WHERE id = %s", (id,))
        return {"mensaje": "Cliente eliminado"}