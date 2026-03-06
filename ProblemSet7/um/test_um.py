from um import count

def test_onlyUm():
    assert count("um") == 1
    assert count("um um um um um") == 5
    assert count("Um um UM uM") == 4

def test_punctuation():
    assert count("Um!") == 1
    assert count("Um, hello um... there") == 2
    assert count("(um) well this is [um] interesting") == 2

def test_otherUmWords():
    assert count("Heya um, how's it...um going yummy album btw") == 2
    assert count("Um well ya know, ummmm... um yea that's not UM too good") == 3
