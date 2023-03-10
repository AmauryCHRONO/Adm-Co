#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""


class SimpleComplexCalculator:
    """Cette classe a pour role de réaliser les opération arthimetique basique
    pour des nombres complexes (+, -, *, /)"""

    def add(self, num_1, num_2):
        """Cette fonction additionne 2 nombres complexes"""
        res = (num_1[0] + num_2[0], num_1[1] + num_2[1])
        return res

    def sub(self, num_1, num_2):
        """Cette fonction soustrait 2 nombres complexes (num_1 - num_2)"""
        res = (num_1[0] - num_2[0], num_1[1] - num_2[1])
        return res

    def mul(self, num_1, num_2):
        """Cette fonction multiplie 2 nombres complexes"""
        res = (
            num_1[0] * num_2[0] - num_1[1] * num_2[1],
            num_1[1] * num_2[0] + num_2[1] * num_1[0],
        )
        return res

    def div(self, num_1, num_2):
        """Cette fonction divise 2 nombres complexes (num_1 / num_2).
        On mutiple le numérateur et le dénominateur par le conjugué du denominateur
        pour obtenir un nombre réel au dénominateur"""
        temp = (num_2[0], -num_2[1])
        temp = self.mul(num_1, temp)
        res = (
            temp[0] / (num_2[0] * num_2[0] + num_2[1] * num_2[1]),
            temp[1] / (num_2[0] * num_2[0] + num_2[1] * num_2[1]),
        )
        return res


if __name__ == "__main__":  # Test de la class
    num_1 = (2, 3)
    num_2 = (-4, 6)
    test = (
        SimpleComplexCalculator()
    )  # Création de l'élément du type SimpleComplexCalculator
    print(
        test.add(num_1, num_2),
        test.sub(num_1, num_2),
        test.mul(num_1, num_2),
        test.div(num_1, num_2),
    )
