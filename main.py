from fastapi import FastAPI
from models import *
from routes import heroes

app = FastAPI()
app.include_router(heroes.router)

@app.get("/")
async def read_root():
    return {"msg": "Hello World"}

