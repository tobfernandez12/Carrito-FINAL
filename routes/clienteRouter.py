import psycopg
from fastapi import APIRouter, Depends
from models.models import Cliente
from managers.conexionManagerSupabase import getCursor
from managers.productoManager import ProductosManager
from managers.clienteManager import ClientesManager

router = APIRouter(prefix="/clientes", tags=["Clientes Rutas"])
clientManager = ClientesManager()

router = APIRouter()
manager = ClientesManager()
getCursor ()
@router.get("/obtener_clientes")
def obtener_clientes(cursor: psycopg.Cursor = Depends (getCursor)):
    res = manager.obtener_clientes(cursor)
    return res

@router.get("/obtener_cliente/{id}")
def obtener_cliente(id: int, Cursor:psycopg.Cursor = Depends (getCursor)):
    return manager.obtener_cliente(id, Cursor)

@router.post("/crear_cliente")
def crear_cliente(cliente: Cliente, Cursor: psycopg.Cursor = Depends (getCursor)):
    return manager.crear_cliente(cliente, Cursor)

@router.put("/modificar_cliente/{id}")
def modificar_cliente(id: int, updatedClient: Cliente, Cursor: psycopg.Cursor = Depends(getCursor)
):

    return manager.modificar_cliente(id, updatedClient.nombre, Cursor)

@router.delete("/eliminar_cliente/{id}")
def eliminar_cliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    return manager.eliminar_cliente(id, cursor)