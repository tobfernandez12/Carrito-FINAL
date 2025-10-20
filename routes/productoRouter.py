from fastapi import APIRouter
from models.models import Producto
from managers.productoManager import ProductosManager

router = APIRouter()
manager = ProductosManager()

@router.get("/obtener_productos")
def obtener_productos():
    return manager.obtener_productos()

@router.post("/crear_producto")
def crear_producto(producto: Producto):
    return manager.crear_producto(producto.nombre, producto.precio, producto.cantidad)

@router.put("/modificar_productos/{id}")
def modifcar_productos(id: int, producto: Producto):
    return manager.modificar_productos(id, producto.nombre, producto.precio, producto.cantidad)

@router.delete("/eliminar_producto/{id}")
def eliminar_cliente(id: int):
    return manager.eliminar_cliente(id)