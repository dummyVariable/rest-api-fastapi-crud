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

    resp1 = req.post(URL, data={'message' : 'Im batman'})
    assert resp1.json() == {'message' : 'created'}
    
    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'Im batman'}
    
    resp3 = req.post(URL, data={'message' : 'Michael Scorn'})
    assert resp3.json() == {'message' : 'created'}

    resp4 = req.get(URL + '/2')
    assert resp4.json() == {'message' : 'Michael Scorn'}

    resp5 = req.get(URL)
    assert len(resp5.json()) == 2