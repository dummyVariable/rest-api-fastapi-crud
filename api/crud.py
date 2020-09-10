from typing import List, Union

from fastapi import APIRouter

from api.model import CrudModel as db

router = APIRouter()

@router.get('/')
def read_all() -> Union[dict, List[dict]]:
    data = db.read_all()

    if data is None:
        return {'message' : 'no items found'}

    return data

@router.get('/{id}')
def read(id: int) -> dict:
    data = db.read(id)

    if data is None:
        return {'message' : 'item not found'}
    
    return data