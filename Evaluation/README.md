# Exercice 2 Test AdmCo
## I. Objectif du projet
L'objectif est de crée unjeu du morpion en python. Il doitpouvoir placer, afficher et detecter des coups prohibés ou la victoire.
## II. Organisation du projet
---
Voici l'arborescence du projet :
```
.
├── Morpion
│   └──MorpionGame
│      ├── __init__.py
│      └── MorpionTools.py
│
├── test
│   ├── test_morpion.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── setup.py
```
Le projet est composé des fichiers README.md, requirements.txt (qui indique les packages à avoir) et le fichier setup.py (qui renseigne les informations à fournir au package lors de l'exportation). Et des fichiers Morpion (qui contient le package des fonctions) et test (qui contient tout les tests des fonctions).
### Package Morpion
Nous avons une grille sur la quel on dispos tout le smouvement au fur et à mesure les coup des joueur jsuqu'a ce qu'il y est une victoire ou match nul.
### Package test
On réalise toute les victoire possible et tout les positionnement possible

### Fichier setup.py

Il renseigne les informations qui seront transmise dans le package ainsi qui l'endroie ou le trouver lors du build.

## III. Importation de package
---
### PYTHONPATH
Pour pemettre l'importation du package, il a fallu faire la commande PYTHONPATH pour que le fichier de test puisse voir le package du calculator : 
```bash
export PYTHONPATH=$PYTHONPATH:'.'
```
### requirements.txt 
Pour réaliser le requirements.txt il fallais utiliser la commande :
```bash
python3 -m pipreqs.pipreqs .
```
Pour cela il fallait telecharger le package avec la commande :
```bash
pip3 install pipreqs
```
## IV. Test
Les test sont réaliser directement sur GitLab viales PipeLine et sont correcte.
## V. Intégration Continue
On a la mise a jour et le test du packet mis a disposition via lesPipeline sur GitLab