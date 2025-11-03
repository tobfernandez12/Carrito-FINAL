from fastapi import FastAPI
from DBManager import DBManager
from routes import clienteRouter, productoRouter, pedidoRouter

app = FastAPI()
db = DBManager()

app.include_router(clienteRouter.router)
app.include_router(productoRouter.router)
app.include_router(pedidoRouter.router)

print("DB creada y API iniciada")

