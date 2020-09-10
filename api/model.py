from typing import Union
import json

from api import rc as client


class CrudModel:
    ModelCounter = 0

    @staticmethod
    def create(message: dict) -> Union[dict, None]:
        if not message:
            return None

        if not message.get('message'):
            return None

        CrudModel.ModelCounter += 1

        client.set(CrudModel.ModelCounter, json.dumps(message))
        
        return {'message' : 'created'}

    @staticmethod
    def read_all() -> Union[dict, None]:
        keys = client.keys('*')
        
        if not keys:
            return None

        data = []
        for key in keys:
            message = client.get(key)
            data.append(json.loads(message))

        return data
    
    @staticmethod
    def read(id: int) -> Union[dict, None]:

        data = client.get(id)

        if data:
            return json.loads(data)

        return None

    @staticmethod
    def update(id: int, message: dict) -> Union[dict, None]:
        
        if not client.get(id):
            return None
        
        if not message.get('message'):
            return None

        client.set(id, json.dumps(message))

        return {'message' : 'updated'}
        
    @staticmethod
    def delete(id: int) -> Union[dict, None]:
        
        if not client.get(id):
            return None
        
        client.delete(id)
        return {'message' : 'deleted'}

    @staticmethod
    def flushit():
        client.flushall()