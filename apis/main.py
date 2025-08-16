from fastapi import FastAPI

app = FastAPI()
# Ruta raíz
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Ruta de saludo
@app.get("/saludo/{nombre}")

async def get_saludo(nombre: str):
    return {"message": f"Hola, {nombre}!"}