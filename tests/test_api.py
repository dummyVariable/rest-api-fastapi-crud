import json 

import requests as req

from api.model import CrudModel as db

URL = 'http://localhost:8000/crud'

def test_for_home():
    resp = req.get('http://localhost:8000')
    assert resp.json() == {'message' : 'crud app'}
    db.flushit()

def test_for_emptyness():

    resp1 = req.get(URL)
    assert resp1.json() == {'message' : 'no items found'}
    
    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'item not found'}

def test_for_create():

    data = json.dumps({'message' : 'Im batman'})
    resp1 = req.post(URL, data=data)
    assert resp1.json() == {'message' : 'created'}  
    
    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'Im batman'}

    data = json.dumps({'message' : 'Michael Scorn'})
    resp3 = req.post(URL, data=data)
    assert resp3.json() == {'message' : 'created'}

    resp4 = req.get(URL + '/2')
    assert resp4.json() == {'message' : 'Michael Scorn'}

    resp5 = req.get(URL)
    assert len(resp5.json()) == 2

def test_for_update():

    data = json.dumps({'message' : 'Im Scotch'})
    resp1 = req.put(URL + '/1', data=data)
    assert resp1.json() == {'message' : 'updated'}

    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'Im Scotch'}

def test_for_delete():

    resp1 = req.delete(URL + '/1')
    assert resp1.json() == {'message' : 'deleted'}

    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'item not found'}

    resp3 = req.get(URL)
    assert len(resp3.json()) == 1