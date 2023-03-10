# Exercice 1
## add
Addition simple entre chaque partie réel et imaginaire.
## sub
Soustraction simple entre chaque partie réel et imaginaire.
Attention les parammètres en entrées sont dans cette ordre "def sub(x,y)", on réalise cette soustractrion : x-y
## mul
Multiplcation : Pour la partie réel, on multiplis les parties réels entre elles et on additionne le négatif de la multiplication des parties imaginaires. Pour la partie imaginaire, on additionnes les mutplications des parties réels avec les parties imaginaires.
## div
Division : On multiplie par le conjugé du denominateur en-haut et en-bas. On réutilise la fonction mul pour calculer le numérateur qui est la multiplicaton de x et du conjugué de y. Au dénominateur, on utilise l'identité remarquable qui nous donne l'addtion entre le carré des deux parties. Attention les parammètres en entrées sont dans cette ordre "def div(x,y)", on réalise cette division : x/y 