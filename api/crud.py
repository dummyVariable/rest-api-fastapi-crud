from typing import List, Union

from fastapi import APIRouter
from pydantic import BaseModel

from api.model import CrudModel as db

router = APIRouter()

class Message(BaseModel):
    message: str

@router.get('/')
def read_all() -> Union[dict, List[dict]]:
    data = db.read_all()

    if data is None:
        return {'message' : 'no items found'}

    return data

@router.get('/{id}')
def read(id: int) -> dict:
    print(id)
    data = db.read(id)

    if data is None:
        return {'message' : 'item not found'}
    
    return data

@router.post('/')
def create(message: Message) -> dict:
    data = {}
    data['message'] = message.message
    resp = db.create(data)

    if not resp:
        return {'message' : 'something went wrong'}
    
    return resp

