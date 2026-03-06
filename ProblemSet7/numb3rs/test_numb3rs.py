from numb3rs import validate

def test_validIpAddress():
    assert validate("10.10.10.10") == True
    assert validate("172.16.100.100") == True
    assert validate("192.168.1.1") == True
    assert validate("255.255.255.255") == True

def test_zeroCheck():
    assert validate("000.168.1.1") == False
    assert validate("00.168.1.1") == False
    assert validate("0.168.1.1") == True
    assert validate("192.000.1.1") == False
    assert validate("192.00.1.1") == False
    assert validate("192.0.1.1") == True
    assert validate("192.68.000.1") == False
    assert validate("192.168.00.1") == False
    assert validate("192.168.0.1") == True
    assert validate("192.168.1.000") == False
    assert validate("192.168.1.00") == False
    assert validate("192.168.1.0") == True
    assert validate("0.0.0.0") == True

def test_invalidIpAddress():
    assert validate("256.1.1.1") == False
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("1") == False
    assert validate("1.") == False
    assert validate("1..") == False
    assert validate("1...") == False
    assert validate(".1") == False
    assert validate("..1") == False
    assert validate("...1") == False
    assert validate(".1.") == False
    assert validate(".1..") == False
    assert validate("..1.") == False
    assert validate(" . . . ") == False
    assert validate("255.255.255.255.255") == False
    assert validate("cat") == False
