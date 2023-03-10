# Rendu Admin Système et Gestion de Code - Amaury CHRONOWSKI

## I. Objectif du projet
---
L'objectif est de crée un calculateur pour complxe pour les opérations d'arithmétiques basiques en python (+, -, *, /). Il a aussi pour but de nous apprendre à utiliser les différentes fonctionnalités de pypi et gitlab pour l'integration de package. Et enfin, nous familiariser avec le test de code avec le package unitest.

## II. Organisation du projet
---
Voici l'arborescence du projet :
```
.
├── Calculator
│   ├── __init__.py
│   └── calculator.py
│
├── Test
│   ├── test_calculator.py
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── setup.py
```

Le projet est composé des fichiers README.md, requirements.txt (qui indique les packages à avoir) et le fichier setup.py (qui renseigne les informations à fournir au package lors de l'exportation). Et des fichiers Calculator (qui contient le package des fonctions) et test_calculator.py (qui contient tout les tests des fonctions) .

### Package calculator 

Nous travaillons avec des tuples pour representer les nombres complexes (Rel, Ima).
Voici une portion du package, toutes les fonctions, dans un premier temps verifient si les variables d'entrées sont bien des nombres puis réalisent les opérations. De plus lors d'une division il y a vérification si le denominateur n'est pas nul. En cas d'erreur, le programme renvoie 'ERROR'. il a fallu importer le package numbers, present de base, pour réaliser les vérifications. 
```python
class SimpleComplexCalculator:
    """Cette classe a pour role de réaliser les opérations arthimetiques basiques
    pour des nombres complexes (+, -, *, /)"""

    def isanumber(self, num):
        """Cette fonction vérifie si on a bien des nombres dans nos tuples. Et renvoi True si ils sont bien des nombres sinon False"""
        if isinstance(num[0], Number) and isinstance(num[1], Number) and not isinstance(num[0], bool) and not isinstance(num[1], bool):
            return True
        return False

    def add(self, num_1, num_2):
        """Cette fonction additionne 2 nombres complexes"""
        if not self.isanumber(num_1) or not self.isanumber(num_2):
            return "ERROR"

        res = (num_1[0] + num_2[0], num_1[1] + num_2[1])
        return res
```

### Package test
Un ensble de test couvrant la plus part des possiblitées sont réalisés dans ce programme : résultat correcte, erreur lors de l'entrée de valeurs incorrectes. Voici une portion du programme, en plus des tests, il y a une indication si celui-ci a été correctement réalisé. Pour cela, nous avons importer le package unittest qui réalise le test, logging qui affiche les resultats et le package à tester. 
```python
class TestAdd(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode add dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()
    
    def test_add(self):
        """Somme de deux complexes, le résultat doit être -1-i"""
        self.assertEqual(
            self.calculator.add((3, -6), (-4, 5)), (-1, -1), "Erreur sur la somme"
        )
        self.log.warning("test somme OK")

    def test_add_str(self):
        """Somme d'un complexe et d'un caractère, le résultat doit être ERROR"""
        self.assertEqual(
            self.calculator.add((5, 4), (3, "s")), "ERROR", "Erreur sur la somme"
        )
        self.log.warning("erreur pour somme avec str OK")
```

### Fichier setup.py

Il renseigne les informations qui seront transmise dans le package ainsi qui l'endroie ou le trouver lors du build.
```python
from setuptools import setupfallu

setup(name='SimpleComplexCalculator_Amaury_CHRONOWSKI_AdmCo',
      version='1.0',
      description='A Simple Complex Calculator',
      author='Amaury CHRONOWSKI',
      author_email='amaury.chronowski@cpe.fr',
      url='https://gitlab.com/Amaury_CHRONOWSKI/admco/-/tree/main/Partie_1',
      packages=['Calculator'],
      package_dir={'Calculator': 'Calculator'},
     )
```
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
### Pypi
Il a fallu installer build et twine pour pemmettre l'exportation sur Pypi : 
```bash
python3 -m pip install --upgrade build
```
```bashfallu
python3 -m pip install --user --upgrade twine
```

## IV. Test
---
Pour réaliser le test, il suffit de lancer le programme de test et on obtient en résultat :
![test](/Image/test_part1_admco.png)
Le resultat est donc correcte et toutes les fonctions retournent bien ce qui est attendue.

## V. Intégration Continue
---
Il existe 2 façons de réaliser l'intégration continue vu au cours de ce projet :
### Pypi
Pour faire l'intégration avec Pypi, il est nécessaire de ce crée un compte de d'obtenir un token qui sera demander lors de l'exportation, ou utiliser un fichier .pypirc, avec les données du token, qu'il faut mettre dans le $HOME pour evite la demande du token à chaque exportation. Et pour exporter apres avoir télécharger les package nécessaire (vu dans la section package), il faut faire la commande suivante :
```bash
python3 -m twine upload dist/*
```

### GitLab
Je n'ai pas eu le temps de traiter cette partie du sujet.
## VI. Autres Dépots du projet
---

Tout le projet a été réalise via des question succesive presente dans des projet GitLab indépendants. pour obtenir plus d'information concernant chaque étapes du projet il ets possible de lire les README;md des differents projets, les liens : 

- Exercice 0 (Reflexion sur les packages de python): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-0
- Exercice 1 (Création des fonction de calcule): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-1
- Exercice 2 (Mise en class des fonctions): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-2
- Exercice 3 (Bonne pratique et amélioration visuel du code): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-3
- Exercice 4 (Premier test avec unittest): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-4
- Exercice 5-6-7 (Conception du test final, avec retoure de message d'erreur, test des variables d'entrées et affichage du résultat du test): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-5-6-7
- Exercice 8 ( Exportation du package via .zip): https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-8
- Exercice 9 (Exportation de package via Pypi) : https://gitlab.com/Amaury_CHRONOWSKI/admco-partie-1-exercice-9

## VII. Ressources
------
- Enoncé de TP : https://prod.e-campus.cpe.fr/course/view.php?id=2199
- Exemple de rendu : https://gitlab.com/fabricejumel/rendufinal_bouyssoux
- Redaction du setup.py : https://docs.python.org/fr/3/distutils/setupscript.html
- Integration continue : https://gitlab.com/js-ci-training/ci-hero-unitarytest-python