from fastapi import APIRouter
from models.models import Pedido
from managers.pedidosManager import PedidosManager

router = APIRouter()
manager = PedidosManager()

@router.get("/obtener_pedidos")
def obtener_pedidos():
    return manager.obtener_pedidos()

@router.get("/obtener_pedido/{id}")
def obtener_pedido(id: int):
    return manager.obtener_pedido(id)

@router.get("/obtener_pedido_por_cliente/{cliente_id}")
def obtener_pedido_por_cliente(cliente_id: int):
    return manager.obtener_pedido_por_cliente(cliente_id)

@router.post("/crear_pedido")
def crear_pedido(pedido: Pedido):
    return manager.crear_pedido(pedido.cliente_id, pedido.producto_id, pedido.cantidad)
