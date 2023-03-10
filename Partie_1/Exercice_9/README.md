# Exercice 9

Pour permettre l'upload, on crée d'abord le dossier src qui va contenir mon package avec un fichier __init__ vide.
Ensuite, on crée le fichier setup.py qui renseigne les informations sur le package (version, auteur, PATH).
Apres on fait la commande dans le fichier qui contient le setup.py:

```bash
python3 -m build
```
On a l'apparition des dossier dist et egg-info. Après, on lance la commande :

```bash
python3 -m twine upload dist/*
```

Soit, on rentre les donners du token à chaque fois, soit on réalise un fichier .pypirc sour la forme
```pypirc
[pypi]
  username = __token__
  password = <token>
```

Pour faire le requirements.txt il fallait installer pyreqs puis faire la commande :  
```bash
python3 -m pireqs.pireqs .
```