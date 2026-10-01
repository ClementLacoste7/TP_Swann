# Organisation de l'équipe

Ce document explique comment l'équipe suit le travail (labels et board) et qui est responsable de chaque livrable.

Équipe : **Clément** ([@ClementLacoste7](https://github.com/ClementLacoste7)) et **Ilyas** ([@ilyaskehili](https://github.com/ilyaskehili)).

## Labels

Les labels sont définis dans [`.github/labels.yml`](../.github/labels.yml). Le workflow [`labels.yml`](../.github/workflows/labels.yml) les crée automatiquement sur GitHub dès que ce fichier change. Pour ajouter un label, on modifie le fichier, on ne le crée pas à la main.

| Catégorie | Labels | Usage |
|-----------|--------|-------|
| Type | `bug`, `enhancement`, `documentation`, `tests`, `ci` | Nature du travail. Les modèles d'issue ajoutent `bug` ou `enhancement` automatiquement. |
| Priorité | `priorité: haute`, `priorité: moyenne`, `priorité: basse` | Ordre de traitement. |
| Autres | `bloqué`, `question` | Signaler un blocage ou un besoin de discussion. |

Chaque issue a **un label de type** et **un label de priorité**.

## Board

Le suivi se fait dans un **GitHub Project** (onglet *Projects* du dépôt) en vue *Board*, avec 4 colonnes :

| Colonne | Signification | Quand y passer |
|---------|---------------|----------------|
| **À faire** | Issue créée, personne ne travaille dessus | À la création de l'issue |
| **En cours** | Quelqu'un travaille dessus | Quand on s'assigne l'issue et qu'on crée sa branche |
| **En review** | Une Pull Request est ouverte et attend une relecture | À l'ouverture de la PR |
| **Terminé** | La PR est mergée, l'issue est fermée | Automatiquement au merge (`Closes #numéro`) |

Le statut d'une tâche est donné par **sa colonne**, pas par un label.

## Qui produit, qui valide, où stocker

| Livrable | Qui produit | Qui valide | Où stocker |
|----------|-------------|------------|------------|
| Code de l'application | Clément et Ilyas | L'autre membre (relecture de PR) + CI | `app/` |
| Tests | Clément et Ilyas (avec le code qu'ils ajoutent) | Ilyas (code owner) + CI | `tests/` |
| CI (workflows) | Clément | Ilyas (relecture de PR) | `.github/workflows/` |
| CODEOWNERS, labels, modèles d'issue et de PR | Clément | Ilyas (relecture de PR) | `.github/` |
| Documentation (README, CONTRIBUTING, ce fichier) | Clément et Ilyas | L'autre membre (relecture de PR) | Racine du dépôt et `docs/` |
| Issues (bugs, fonctionnalités) | N'importe quel membre | Triées par l'équipe (labels + priorité) | Onglet *Issues* de GitHub |
| Suivi des tâches | Celui qui travaille sur la tâche | L'équipe, au point d'avancement | Board du GitHub Project |
| Pull Requests | L'auteur de la branche | Code owner de la zone + CI verte | Onglet *Pull requests* de GitHub |
| Mise en production (`develop` → `main`) | Clément ou Ilyas | Les deux membres | Branche `main` |
