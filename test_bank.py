from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("h") == 20

def test_others():
    assert value("baby") == 100
    assert value("welcome") == 100
