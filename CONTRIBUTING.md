# Guide de contribution

Ce document explique comment on travaille avec Git sur ce projet.

## Workflow des branches

On utilise un **Git Flow simplifié** avec deux branches permanentes et des branches temporaires.

### Branches permanentes

| Branche   | Rôle                                                              |
|-----------|-------------------------------------------------------------------|
| `main`    | Version stable du projet. On ne travaille **jamais** directement dessus. |
| `develop` | Branche d'intégration : on y regroupe les fonctionnalités terminées.     |

### Branches temporaires

Elles partent toujours de `develop` et y reviennent une fois le travail fini.

| Préfixe      | Usage                         | Exemple                    |
|--------------|-------------------------------|----------------------------|
| `feature/`   | Nouvelle fonctionnalité       | `feature/page-connexion`   |
| `fix/`       | Correction de bug             | `fix/erreur-formulaire`    |
| `docs/`      | Documentation uniquement      | `docs/maj-readme`          |

Nommage : en minuscules, mots séparés par des tirets, nom court et explicite.

```
main     ●─────────────────────────●──────
          \                       /
develop    ●──────●──────────●───●────────
                   \        /
feature/xxx         ●──●──●
```

## Étapes pour contribuer

1. **Se mettre à jour**
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. **Créer sa branche**
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```

3. **Travailler et commiter**
   ```bash
   git add .
   git commit -m "feat: ajoute la page de connexion"
   ```

4. **Pousser sa branche**
   ```bash
   git push -u origin feature/nom-de-la-fonctionnalite
   ```

5. **Ouvrir une Pull Request** vers `develop` sur GitHub.
   - Au moins **un autre membre** de l'équipe doit relire et approuver.
   - Une fois validée, on merge puis on supprime la branche.

6. **Mise en production** : quand `develop` est stable, on ouvre une Pull Request de `develop` vers `main`.

## Messages de commit

On suit la convention [Conventional Commits](https://www.conventionalcommits.org/fr/) :

| Préfixe     | Signification                          |
|-------------|----------------------------------------|
| `feat:`     | Nouvelle fonctionnalité                |
| `fix:`      | Correction de bug                      |
| `docs:`     | Documentation                          |
| `style:`    | Mise en forme (sans changer le code)   |
| `refactor:` | Réorganisation du code                 |
| `test:`     | Ajout ou modification de tests         |

Exemples :
```
feat: ajoute le formulaire d'inscription
fix: corrige l'affichage du menu sur mobile
docs: complète le README
```

## Règles

- Pas de push direct sur `main` ni sur `develop`.
- Une branche = une fonctionnalité ou une correction.
- Toujours faire un `git pull` de `develop` avant de créer une branche.
- Si conflit : le résoudre en local sur sa branche avant de merger.
