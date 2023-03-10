# Exercice 0
## Explication de code

Le code est en deux parties : le main, qui va être executé et réalisé les actions voulu; la fonction "add", qui va réaliser l'action d'additionner deux valeurs.
Le main fait saisir deux valeurs à l'utilisateur et les fait s'additionner en appelant la fonction "add", affiche le resultat et indque qu'il est fini.
## A quoi sert requirments.txt ?
Ce fichier sert à indiquer les versions des outils nécessaire au bon fonctionnement du programme.
## A quoi ressemble un module en python ?
C'est un fichier Python, qui contient et/ou des classes, des fonctions et des variables. Elles peuvent etre importées depuis un autre fichier.
## A quoi ressemble un package ?
C'est un fichier qui contint plusieurs modules.
## Code "addition.py" sous forme de module

```python
import addition

num_1 = 5
num_2 = 7
res = addition.add(num_1, num_2)
print(num_1, "+", num_2, "=", res)
```
## A quoi sert pip ?
Cette fonction sert à importer des packages en Python.
## A quoi sert PYTHON PATH ?
On l'utilise lorqu'on import des modules sur Python. Il indique dans quel dossier se trouve le module utilisé
## Ou sont stockées les paquets installé par pip ?
En utilisant la commande sys.path, on obtient : "/opt/python/spyder/lib/python3.6/site-packages".
## A quoi sert pip install –user ?   
Cela permet d'installer le package seulement à l'utilisateur en cours.
## A quoi sert venv ?
C'est un module utilisé pour créer et gérer des environnements virtuels.
## Comment utiliser venv ?
Il faut utiliser la commande "python -m venv <nom de l'environnement>". Cela crée un dossier au nom de l'environnement virtuel. Puis, on l'active en entrant la commande "<nom de l'environnement>/bin/activate". Et, on le désactive en utilisant la commande "deactivate".