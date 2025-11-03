from fastapi import APIRouter, Depends
import psycopg
from models.models import Pedido
from managers.conexionManagerSupabase import getCursor
from managers.pedidosManager import PedidosManager

router = APIRouter()
manager = PedidosManager()
getCursor()

@router.get("/obtener_pedidos")
def obtener_pedidos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.obtener_pedidos(cursor)
    return {"pedidos": res}

@router.get("/obtener_pedido/{id}")
def obtener_pedido(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.obtener_pedido(id, cursor)
    return {"pedidos" : res}

@router.get("/obtener_pedido_por_cliente/{nombre}")
def obtener_pedido_por_cliente(nombre: str, cursor : psycopg.Cursor = Depends(getCursor)):
    res =  manager.obtener_pedido_por_cliente(nombre, cursor)
    return res

@router.post("/crear_pedido")
def crear_pedido(pedido: Pedido, cursor: psycopg.Cursor = Depends(getCursor),):
    res = manager.crear_pedido(pedido, cursor)
    return {"mensage": res}
