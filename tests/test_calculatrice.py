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


@pytest.mark.parametrize(
    "fonction", [addition, soustraction, multiplication, division]
)
@pytest.mark.parametrize("a, b", [("2", 3), (2, "3"), (None, 1), (True, 2)])
def test_parametres_pas_nombres(fonction, a, b):
    with pytest.raises(TypeError, match="Les paramètres doivent être des nombres"):
        fonction(a, b)


def test_decimaux_acceptes():
    assert addition(1.5, 2) == 3.5
