import fuel
import pytest

def test_gaugeEmpty():
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(0) == "E"

def test_gaugeFull():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(100) == "F"

def test_gauge():
    assert fuel.gauge(25) == "25%"
    assert fuel.gauge(50) == "50%"
    assert fuel.gauge(75) == "75%"
    assert fuel.gauge(33) == "33%"
    assert fuel.gauge(66) == "66%"

def test_convertInt():
    with pytest.raises(ValueError):
        fuel.convert("cat/4")
    with pytest.raises(ValueError):
        fuel.convert("4/dog")
    with pytest.raises(ValueError):
        fuel.convert("3.5/4")
    with pytest.raises(ValueError):
        fuel.convert("4/4.5")

def test_convertNeg():
    with pytest.raises(ValueError):
        fuel.convert("-2/4")
    with pytest.raises(ValueError):
        fuel.convert("2/-4")
    with pytest.raises(ValueError):
        fuel.convert("-4/-4")

def test_convertGreaterThan():
    with pytest.raises(ValueError):
        fuel.convert("5/4")

def test_convertZero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")

def test_convert():
    assert fuel.convert("3/4") == 75
    assert fuel.convert("0/4") == 0
    assert fuel.convert("99/100") == 99
    assert fuel.convert("1/100") == 1
    assert fuel.convert("4/4") == 100

