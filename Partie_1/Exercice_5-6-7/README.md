# Exrecice 5-6-7
### Test des varibales d'entrées
On améliore le package de calcule pour implemanter un teste de type de valeur pour qu'il s'agisse bien d'un nombre. on crée une méthode Isanulber :
```python
def isanumber(self, num):
    """Cette fonction vérifie si on a bien des nombre dans nos tuples. Et renvoi True si ils sont bien des nombres sinon False"""
    if isinstance(num[0], Number) and isinstance(num[1], Number) and not isinstance(num[0], bool) and not isinstance(num[1], bool):
        return True
    return False
```
De plus, on va ajouter un test dans la methode de la division pour vérifier s'il le denominateur n'est pas négatif. En cas des deux erreur le programme va retourner 'ERROR'.
### Affichage des résultats du test
Pour améliorer la compréhension du test il a fallu ajouter un affichage avec logging qui permet d'ajouter un text après chaque test :
```python 
    self.log.warning("erreur pour somme avec str OK")
```