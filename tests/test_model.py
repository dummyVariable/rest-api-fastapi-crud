
from api.model import CrudModel as db

def test_for_emptyness():

    assert db.read_all() == None
    assert db.read(1) == None
