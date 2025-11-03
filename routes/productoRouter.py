import psycopg
from fastapi import APIRouter, Depends
from models.models import Producto
from managers.conexionManagerSupabase import getCursor
from managers.productoManager import ProductosManager

router = APIRouter()
manager = ProductosManager()

router = APIRouter(prefix="/productos", tags=["Productos router"])

getCursor()

@router.get("/obtener_productos")
def obtener_productos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.obtener_productos(cursor)
    return res

@router.post("/crear_producto")
def crear_producto(Producto: Producto, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.crear_producto(Producto, cursor)
    return{"mensaje":"res"}
    
