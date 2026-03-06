from bank import value

def test_lowerhello():
    assert value("hello there") == 0

def test_upperhello():
    assert value("HELLO") == 0

def test_mixedhello():
    assert value("heLLo, how's it going?") == 0

def test_startswithh():
    assert value("heya") == 20
    assert value("How's it going?") == 20

def test_startswithspace():
    assert value("            HeLLo there") == 0
    assert value("      heya       buddy     ") == 20
    assert value("       wow what a great community") == 100

def test_incorrectgreeting():
    assert value("Who are you?") == 100
    assert value("What are you doing here?") == 100

def test_nonalpha():
    assert value("123hello there") == 100
    assert value("!Hello!") == 100
    assert value("     h3y th3r3") == 20
