from twttr import shorten
import pytest

def test_singleword():
    assert shorten("sequoia") == "sq"

def test_multiword():
    assert shorten("Equations produce dialogue and euphoria") == "qtns prdc dlg nd phr"

def test_uppercase():
    assert shorten("SEQUOIA") == "SQ"

def test_mixedcase():
    assert shorten("SeqUoIa") == "Sq"

def test_includingnonaplha():
    assert shorten("s3q0!a") == "s3q0!"
