tablas = [
    """
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS producto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER,
        producto_id INTEGER,
        cantidad INTEGER NOT NULL,
        FOREIGN KEY (cliente_id) REFERENCES cliente(id),
        FOREIGN KEY (producto_id) REFERENCES producto(id)
    );
    """
]