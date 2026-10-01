import pytest

from app.calculatrice import addition, division, multiplication, soustraction


def test_addition():
    assert addition(2, 3) == 5


def test_soustraction():
    assert soustraction(5, 3) == 2


def test_multiplication():
    assert multiplication(4, 3) == 12


def test_division():
    assert division(10, 2) == 5


def test_division_par_zero():
    with pytest.raises(ValueError):
        division(1, 0)
