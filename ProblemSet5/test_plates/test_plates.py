from plates import is_valid

def test_notstartwith2letters():
    assert is_valid("C50") == False
    assert is_valid("555555") == False
    assert is_valid("0000") == False

def test_lessthan2char():
    assert is_valid("C") == False

def test_morethan6char():
    assert is_valid("HARVA50") == False
    assert is_valid("HARVARD") == False

def test_numberinmiddle():
    assert is_valid("CS50CS") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("AAAA00") == False
    assert is_valid("CS50") == True

def test_alphanum():
    assert is_valid("~!@#%") == False
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50.") == False

def test_acceptable():
    assert is_valid("CS50") == True
    assert is_valid("AAAA22") == True
    assert is_valid("CS") == True
    assert is_valid("CS5000") == True
