from fastapi import FastAPI
from uvicorn import run

from api import crud

app = FastAPI()

@app.get('/')
def home():
    return {'message' : 'crud app'}

app.include_router(crud.router, prefix='/crud')

