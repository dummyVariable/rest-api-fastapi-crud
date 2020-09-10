
from api.model import CrudModel as db

def test_for_emptyness():

    assert db.read() == None
    assert db.read(1) == None
    