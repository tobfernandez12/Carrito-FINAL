from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str

class Producto(BaseModel):
    nombre: str
    precio: float
    cantidad: int 

class Pedido(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int