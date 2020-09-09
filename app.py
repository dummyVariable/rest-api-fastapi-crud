from fastapi import FastAPI

from api import crud

app = FastAPI()

app.include_router(crud.router, prefix='/crud')