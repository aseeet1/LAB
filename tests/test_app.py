from app import add
from app import kobeitu

def test_add():
    assert add(2, 3) == 5

def test_kobeitu():
    assert kobeitu(4, 5) == 20
