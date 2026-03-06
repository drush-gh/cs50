from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    assert jar1.size == 0
    jar2 = Jar(20)
    assert jar2.capacity == 20
    assert jar2.size == 0
    jar1.size = 10
    jar2.size = 5
    assert jar1.capacity == 12
    assert jar1.size == 10
    assert jar2.capacity == 20
    assert jar2.size == 5


def test_str():
    jar1 = Jar()
    assert str(jar1) == ""
    jar1.deposit(1)
    assert str(jar1) == "🍪"
    jar1.deposit(11)
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar1 = Jar()
    jar1.deposit(5)
    assert jar1.capacity == 12
    assert jar1.size == 5
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.deposit(0)
    assert jar1.capacity == 12
    assert jar1.size == 5
    assert str(jar1) == "🍪🍪🍪🍪🍪"
    jar1.deposit(7)
    assert jar1.capacity == 12
    assert jar1.size == 12
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        jar1.deposit(1)


def test_withdraw():
    jar1 = Jar(20, 20)
    assert jar1.capacity == 20
    assert jar1.size == 20
    jar1.withdraw(5)
    assert jar1.capacity == 20
    assert jar1.size == 15
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar1.withdraw(0)
    assert jar1.capacity == 20
    assert jar1.size == 15
    assert str(jar1) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar1.withdraw(15)
    assert jar1.capacity == 20
    assert jar1.size == 0
    assert str(jar1) == ""
    with pytest.raises(ValueError):
        jar1.withdraw(1)
