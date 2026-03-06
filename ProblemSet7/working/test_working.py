from working import convert
import pytest

def test_formatOne():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"

def test_formatTwo():
    assert convert("9 AM to 5 AM") == "09:00 to 05:00"

def test_formatThree():
    assert convert("9:00 PM to 5 AM") == "21:00 to 05:00"

def test_formatFour():
    assert convert("9 PM to 5:00 PM") == "21:00 to 17:00"

def testBadInput():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
    with pytest.raises(ValueError):
        convert("13:00 PM to 1 AM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("0:00 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")
