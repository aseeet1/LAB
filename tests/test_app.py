from app import add, kobeitu, alu, bolu


def test_add():
    assert add(2, 3) == 5

def test_kobeitu():
    assert kobeitu(4, 5) == 20

def test_alu():
    assert alu(7, 6) == 3

def test_bolu():
    assert bolu(15, 3) == 5
