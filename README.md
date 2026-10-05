# TP_Swann

Petit projet Python réalisé en binôme pour pratiquer le travail collaboratif avec Git et GitHub.
Il contient une calculatrice simple, des tests et une intégration continue.

## Fonctions disponibles

Les fonctions se trouvent dans `app/calculatrice.py` :

| Fonction | Rôle | Exemple |
|----------|------|---------|
| `addition(a, b)` | Additionne deux nombres | `addition(2, 3)` donne `5` |
| `soustraction(a, b)` | Soustrait `b` à `a` | `soustraction(5, 3)` donne `2` |
| `multiplication(a, b)` | Multiplie deux nombres | `multiplication(4, 3)` donne `12` |
| `division(a, b)` | Divise `a` par `b` | `division(10, 2)` donne `5.0` |
| `modulo(a, b)` | Reste de la division de `a` par `b` | `modulo(10, 3)` donne `1` |

Une division ou un modulo par zéro lève une `ValueError`.

Toutes les fonctions lèvent une `TypeError` si on leur passe autre chose qu'un nombre (texte, `None`, `True`...).

Exemple d'utilisation :

```python
from app.calculatrice import addition

print(addition(2, 3))  # 5
```

## Utiliser la calculatrice en ligne de commande

Depuis la racine du projet :

```bash
python -m app 2 + 3     # 5
python -m app 10 / 2    # 5.0
python -m app 10 % 3    # 1
```

Opérateurs disponibles : `+`, `-`, `*`, `/`, `%`.

En cas d'erreur (division par zéro, opérateur inconnu, texte au lieu d'un nombre),
un message clair s'affiche et la commande renvoie un code de sortie différent de 0.

Sous bash, il faut mettre `*` entre guillemets, sinon il est remplacé par la liste des fichiers :
`python -m app 4 "*" 3`. Sous Git Bash (Windows), `/` est aussi transformé en chemin :
utiliser PowerShell, ou lancer `MSYS_NO_PATHCONV=1 python -m app 10 / 2`.

## Installation

Il faut Python 3. Depuis la racine du projet :

```bash
pip install -r requirements-dev.txt
```

## Lancer les tests

```bash
pytest
```

## Vérifier le code (lint)

```bash
flake8 app tests
```

La CI GitHub lance ces deux vérifications à chaque push et à chaque Pull Request vers `main` ou `develop`.

## Contribuer

Le fonctionnement des branches, des commits et des Pull Requests est décrit dans [CONTRIBUTING.md](CONTRIBUTING.md).
