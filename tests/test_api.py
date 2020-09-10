import requests as req

URL = 'http://localhost:8000/crud'

def test_for_home():
    resp = req.get('http://localhost:8000')
    assert resp.json() == {'message' : 'crud app'}

def test_for_emptyness():

    resp1 = req.get(URL)
    assert resp1.json() == {'message' : 'no items found'}
    
    resp2 = req.get(URL + '/1')
    assert resp2.json() == {'message' : 'item not found'}