import pytest

from app.calculatrice import (
    addition,
    division,
    modulo,
    multiplication,
    puissance,
    soustraction,
)


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
    "fonction",
    [addition, soustraction, multiplication, division, modulo, puissance],
)
@pytest.mark.parametrize("a, b", [("2", 3), (2, "3"), (None, 1), (True, 2)])
def test_parametres_pas_nombres(fonction, a, b):
    with pytest.raises(TypeError, match="Les paramètres doivent être des nombres"):
        fonction(a, b)


def test_decimaux_acceptes():
    assert addition(1.5, 2) == 3.5


def test_modulo():
    assert modulo(10, 3) == 1


def test_modulo_par_zero():
    with pytest.raises(ValueError, match="Modulo par zéro impossible"):
        modulo(10, 0)


def test_puissance():
    assert puissance(2, 3) == 8


def test_puissance_exposant_zero():
    assert puissance(5, 0) == 1


def test_puissance_exposant_negatif():
    assert puissance(2, -1) == 0.5


def test_puissance_zero_exposant_negatif():
    with pytest.raises(
        ValueError, match="Puissance de zéro avec un exposant négatif impossible"
    ):
        puissance(0, -1)
