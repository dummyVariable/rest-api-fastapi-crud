from typing import Union

from api import rc as client

class CrudModel:

    @staticmethod
    def read_all() -> Union[dict, None]:
        keys = client.keys('*')
        
        if not keys:
            return None

        data = []
        for key in keys:
            data.append(client.get(key))

        return data
    
    @staticmethod
    def read(id: int) -> Union[dict, None]:

        data = client.get(id)

        if data:
            return data

        return None