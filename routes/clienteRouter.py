from fastapi import APIRouter
from models.models import Cliente
from managers.clienteManager import ClientesManager

router = APIRouter()
manager = ClientesManager()

@router.get("/obtener_clientes")
def obtener_clientes():
    return manager.obtener_clientes()

@router.get("/obtener_cliente/{id}")
def obtener_cliente(id: int):
    return manager.obtener_cliente(id)

@router.post("/crear_cliente")
def crear_cliente(cliente: Cliente):
    return manager.crear_cliente(cliente.nombre)

@router.put("/modificar_cliente/{id}")
def modificar_cliente(id: int, cliente: Cliente):
    return manager.modificar_cliente(id, cliente.nombre, cliente)

@router.delete("/eliminar_cliente/{id}")
def eliminar_cliente(id: int):
    return manager.eliminar_cliente(id)