import os
import subprocess
import sys
from pathlib import Path

import pytest

from app.__main__ import main


@pytest.mark.parametrize(
    "arguments, attendu",
    [
        (["2", "+", "3"], "5"),
        (["5", "-", "8"], "-3"),
        (["4", "*", "3"], "12"),
        (["10", "/", "2"], "5.0"),
        (["10", "%", "3"], "1"),
        (["1.5", "+", "2"], "3.5"),
    ],
)
def test_operations(capsys, arguments, attendu):
    assert main(arguments) == 0
    assert capsys.readouterr().out.strip() == attendu


@pytest.mark.parametrize(
    "arguments, message",
    [
        (["1", "/", "0"], "Division par zéro impossible"),
        (["7", "%", "0"], "Modulo par zéro impossible"),
        (["abc", "+", "1"], "« abc » n'est pas un nombre"),
        (["1", "+", "abc"], "« abc » n'est pas un nombre"),
    ],
)
def test_erreurs_de_calcul(capsys, arguments, message):
    assert main(arguments) == 1
    sortie = capsys.readouterr()
    assert sortie.out == ""
    assert message in sortie.err
    assert "Traceback" not in sortie.err


def test_operateur_inconnu(capsys):
    assert main(["2", "^", "3"]) == 2
    assert "opérateur inconnu « ^ »" in capsys.readouterr().err


@pytest.mark.parametrize("arguments", [[], ["1", "+"], ["1", "+", "2", "3"]])
def test_mauvais_nombre_d_arguments(capsys, arguments):
    assert main(arguments) == 2
    assert "Usage" in capsys.readouterr().err


def test_lancement_avec_python_m():
    resultat = subprocess.run(
        [sys.executable, "-m", "app", "1", "/", "0"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        cwd=Path(__file__).parents[1],
    )
    assert resultat.returncode == 1
    assert "Division par zéro impossible" in resultat.stderr
    assert "Traceback" not in resultat.stderr
