from DBManager import DBManager

class PedidosManager:
    def __init__(self):
        self.db = DBManager()

    def obtener_pedidos(self):
        self.db.cursor.execute("""
        SELECT pedido.id, cliente.nombre AS cliente, producto.nombre AS producto, pedido.cantidad
        FROM pedido
        JOIN cliente ON pedido.cliente_id = cliente.id
        JOIN producto ON pedido.producto_id = producto.id
        """)
        return [dict(row) for row in self.db.cursor.fetchall()]

    def obtener_pedido(self, id: int):
        self.db.cursor.execute("""
        SELECT pedido.id, cliente.nombre AS cliente, producto.nombre AS producto, pedido.cantidad
        FROM pedido
        JOIN cliente ON pedido.cliente_id = cliente.id
        JOIN producto ON pedido.producto_id = producto.id
        WHERE pedido.id = ?
        """, (id,))
        row = self.db.cursor.fetchone()
        return dict(row) if row else  {"error": f"No se encontró pedido con id {id}"}
    
    def obtener_pedido_por_cliente(self, cliente_id: int):
        query = """
        SELECT pedido.id, cliente.nombre AS cliente, producto.nombre AS producto, pedido.cantidad
        FROM pedido
        JOIN cliente ON pedido.cliente_id = cliente.id
        JOIN producto ON pedido.producto_id = producto.id
        WHERE pedido.cliente_id = ?
        """
        res = self.db.cursor.execute(query, (cliente_id,)).fetchall()
        return [dict(row) for row in res]

    def crear_pedido(self, cliente_id: int, producto_id: int, cantidad: int):
        self.db.cursor.execute(
            "INSERT INTO pedido (cliente_id, producto_id, cantidad) VALUES (?, ?, ?)",
            (cliente_id, producto_id, cantidad)
        )
        self.db.connection.commit()
        return {"mensaje": "Pedido creado"}
