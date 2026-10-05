def verifier_nombres(*valeurs):
    for valeur in valeurs:
        # True et False sont des int en Python, on les refuse aussi
        if isinstance(valeur, bool) or not isinstance(valeur, (int, float)):
            raise TypeError("Les paramètres doivent être des nombres")


def addition(a, b):
    verifier_nombres(a, b)
    return a + b


def soustraction(a, b):
    verifier_nombres(a, b)
    return a - b


def multiplication(a, b):
    verifier_nombres(a, b)
    return a * b


def division(a, b):
    verifier_nombres(a, b)
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b


def modulo(a, b):
    verifier_nombres(a, b)
    if b == 0:
        raise ValueError("Modulo par zéro impossible")
    return a % b


def puissance(a, b):
    verifier_nombres(a, b)
    if a == 0 and b < 0:
        raise ValueError("Puissance de zéro avec un exposant négatif impossible")
    return a ** b
