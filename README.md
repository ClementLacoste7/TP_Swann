# TP_Swan

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

Une division par zéro lève une `ValueError`.

Exemple d'utilisation :

```python
from app.calculatrice import addition

print(addition(2, 3))  # 5
```

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
