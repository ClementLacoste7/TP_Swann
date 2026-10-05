import sys

from app.calculatrice import addition, division, modulo, multiplication, soustraction

OPERATIONS = {
    "+": addition,
    "-": soustraction,
    "*": multiplication,
    "/": division,
    "%": modulo,
}

USAGE = "Usage : python -m app <nombre> <opérateur> <nombre> (opérateurs : + - * / %)"


def lire_nombre(texte):
    try:
        return int(texte)
    except ValueError:
        pass
    try:
        return float(texte)
    except ValueError:
        raise ValueError(f"« {texte} » n'est pas un nombre")


def main(arguments):
    if len(arguments) != 3:
        print(USAGE, file=sys.stderr)
        return 2

    texte_a, operateur, texte_b = arguments
    if operateur not in OPERATIONS:
        print(f"Erreur : opérateur inconnu « {operateur} »", file=sys.stderr)
        print(USAGE, file=sys.stderr)
        return 2

    try:
        a = lire_nombre(texte_a)
        b = lire_nombre(texte_b)
        resultat = OPERATIONS[operateur](a, b)
    except (ValueError, TypeError) as erreur:
        print(f"Erreur : {erreur}", file=sys.stderr)
        return 1

    print(resultat)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
