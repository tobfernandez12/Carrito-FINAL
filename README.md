RUTAS CLIENTES:
GET obtener_clientes http://127.0.0.1:8000/obtener_clientes
GET obtener_cliente http://127.0.0.1:8000/obtener_cliente/2
POST crear_cliente http://127.0.0.1:8000/crear_cliente {"nombre": "tiara"}
PUT modificar_cliente http://127.0.0.1:8000/modificar_cliente/1 {"nombre": "tiara"}
DELETE eliminar_cliente http://127.0.0.1:8000/eliminar_cliente/1

RUTAS PRODUCTOS:
GET obtener_productos http://127.0.0.1:8000/obtener_productos
POST crear producto http://127.0.0.1:8000/crear_producto {"nombre": "tiara", "precio": 10000,"cantidad":5}

RUTAS PEDIDOS:
GET obtener_pedidos http://127.0.0.1:8000/obtener_pedidos
GET obtener_pedido http://127.0.0.1:8000/obtener_pedido/2
GET obtener pedido por cliente http://127.0.0.1:8000/obtener_pedido_por_cliente/1
POST crear pedido http://127.0.0.1:8000/crear_pedido {"cliente_id": 1,"producto_id": 1,"cantidad": 2}
PUT modificar_producto http://127.0.0.1:8000/modificar_producto {"nombre": "tiara", "precio": 200}