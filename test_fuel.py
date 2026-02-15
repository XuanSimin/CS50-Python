from fuel import convert
from fuel import gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("1/3") == 33
    assert convert("1/1") == 100


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(100) == "F"
    assert gauge(33) == "33%"
