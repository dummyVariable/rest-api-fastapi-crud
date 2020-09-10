from typing import Union
import json

from api import rc as client


class CrudModel:
    ModelCounter = 0



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
    def flushit():
        client.flushall()