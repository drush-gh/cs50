from seasons import validate
import pytest

def test_validateJanuary():
    assert validate("2000-01-01") == True
    assert validate("2000-01-12") == True
    assert validate("2000-01-29") == True
    assert validate("2000-01-30") == True
    assert validate("2000-01-31") == True
    assert validate("2000-01-00") == False
    assert validate("2000-01-32") == False

def test_validateFebruary():
    assert validate("2000-02-01") == True
    assert validate("2000-02-13") == True
    assert validate("2000-02-28") == True
    assert validate("2000-02-29") == True
    assert validate("2000-02-00") == False
    assert validate("2000-02-30") == False
    assert validate("2000-02-31") == False
    assert validate("2001-02-29") == False
    assert validate("2001-02-30") == False
    assert validate("2001-02-31") == False

def test_validateMarch():
    assert validate("2000-03-01") == True
    assert validate("2000-03-14") == True
    assert validate("2000-03-29") == True
    assert validate("2000-03-30") == True
    assert validate("2000-03-31") == True
    assert validate("2000-03-00") == False
    assert validate("2000-03-32") == False

def test_validateApril():
    assert validate("2000-04-01") == True
    assert validate("2000-04-15") == True
    assert validate("2000-04-29") == True
    assert validate("2000-04-30") == True
    assert validate("2000-04-00") == False
    assert validate("2000-04-31") == False

def test_validateYear():
    assert validate("0-01-01") == False
    assert validate("1-01-01") == False
    assert validate("00-01-01") == False
    assert validate("01-01-01") == False
    assert validate("10-01-01") == False
    assert validate("000-01-01") == False
    assert validate("001-01-01") == False
    assert validate("100-01-01") == False
    assert validate("0000-01-01") == False
    assert validate("0001-01-01") == True
    assert validate("0010-01-01") == True
    assert validate("0100-01-01") == True
    assert validate("1000-01-01") == True

def test_validateInvalidMonth():
    assert validate("2000-00-01") == False
    assert validate("2000-1-01") == False
    assert validate("2000-9-01") == False
    assert validate("2000-0-01") == False
    assert validate("2000-13-01") == False
    assert validate("2000-001-01") == False
    assert validate("2000-111-01") == False


def test_validateInvalidDay():
    assert validate("2000-01-00") == False
    assert validate("2000-01-001") == False
    assert validate("2000-01-1") == False
    assert validate("2000-01-111") == False
