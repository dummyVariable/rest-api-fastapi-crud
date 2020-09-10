
from api.model import CrudModel as db

def test_for_emptyness():
    db.flushit()
    assert db.read_all() == None
    assert db.read(1) == None

def test_for_create():

    assert db.create({'message' : 'pizza'}) == {'message' : 'created'}
    assert db.read(1) == {'message' : 'pizza'}
    assert db.read_all() == [{'message' : 'pizza'}]

    assert db.create({'message' : 'Im batman'}) == {'message' : 'created'}
    assert db.read(2) == {'message' : 'Im batman'}
    assert len(db.read_all()) == 2

    assert db.create({'bla':1}) == None

def test_for_update():

    assert db.update(1, {'message' : 'ice cream'}) == {'message' : 'updated'}
    assert db.read(1) == {'message' : 'ice cream'}
    
def test_for_delete():

    assert db.delete(1) == {'message' : 'deleted'}
    assert len(db.read_all()) == 1
    assert db.read(1) == None
    assert db.delete(42) == None