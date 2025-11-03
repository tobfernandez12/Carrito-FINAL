import psycopg
from models.models import Pedido

class PedidosManager:
    def obtener_pedidos(self, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            "SELECT Producto.nombre, Producto.precio, Cliente.nombre FROM Pedido INNER JOIN Cliente ON Pedido.cliente_id = Cliente.id INNER JOIN Producto ON Pedido.producto_id = Producto.id"
        ).fetchall()
        return [
            {"Producto": row[0], "Precio": row[1], "Cliente": row[2]} for row in res
        ]

    def obtener_pedido(self, id: int, cursor: psycopg.Cursor) -> list:
        cursor.execute(
            "SELECT Producto.nombre, Producto.precio, Cliente.nombre FROM Pedido INNER JOIN Cliente ON Pedido.cliente_id = Cliente.id INNER JOIN Producto ON Pedido.producto_id = Producto.id WHERE Pedido.cliente_id = %s",
            (id,),
        )
        res = cursor.fetchall()
        return [
            {"Producto": row[0], "Precio": row[1], "Cliente": row[2]} for row in res
        ]
    
    def obtener_pedido_por_cliente(self, nombre : str, cursor : psycopg.Cursor) -> list | str:
        clienteId = cursor.execute(
            "SELECT Cliente.id FROM Cliente WHERE nombre = (%s)", (nombre,)
        ).fetchone()
        if clienteId:
            res = cursor.execute(
                "SELECT Producto.nombre, Producto.precio, Cliente.nombre FROM pedido INNER JOIN Cliente ON pedido.cliente_id = Cliente.id INNER JOIN Producto ON Pedido.producto_id = Producto.id WHERE Pedido.cliente_id = %s",
            (clienteId[0],),
            ).fetchall()
            return [
                {"Producto": row[0], "precio": row[1], "Cliente": row[2]}for row in res
            ]
        else:
            return{"mensaje":"No se encontro ningun usuario"}
        
    def crear_pedido(self, pedido: Pedido, cursor : psycopg.Cursor):
        cursor.execute (
            "INSERT INTO pedido (producto_id, cliente_id) VALUES (%s,%s)",
            (pedido.producto_id, pedido.cliente_id,),
        )
        return {"mensaje": "Pedido creado"}
