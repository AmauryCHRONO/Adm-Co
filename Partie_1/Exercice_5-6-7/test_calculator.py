#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

import unittest
import logging
from calculator import SimpleComplexCalculator


class TestAdd(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode add dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_add_str(self):
        """Somme d'un complexe et d'un caractère, le résultat doit être ERROR"""
        self.assertEqual(
            self.calculator.add((5, 4), (3, "s")), "ERROR", "Erreur sur la somme"
        )
        self.log.warning("erreur pour somme avec str OK")


class TestSub(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode sub dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_sub_str(self):
        """Soustraction d'un complexe et d'un caractère, le résultat doit être une erreur"""
        self.assertEqual(
            self.calculator.add((5, 4), (3, "s")), "ERROR", "Erreur sur la différence"
        )
        self.log.warning("erreur pour différence avec str OK")


class TestMul(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode mul dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_mul_str(self):
        """Multiplication d'un complexe et d'un caractère, le résultat doit être une erreur"""
        self.assertEqual(
            self.calculator.mul((5, 4), (3, "s")), "ERROR", "Erreur sur la multiplication"
        )
        self.log.warning("erreur pour multiplication avec str OK")


class TestDiv(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode div dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_div_0(self):
        """Division d'un complexe et 0, le résultat doit être une erreur"""
        self.assertEqual(
            self.calculator.div((5, 4), (0, 0)), "ERROR", "Erreur sur la division"
        )
        self.log.warning("erreur pour division par 0 OK")

    def test_div_str(self):
        """Division d'un complexe et d'un caractère, le résultat doit être une erreur"""
        self.assertEqual(
            self.calculator.div((5, 4), (3, "s")), "ERROR", "Erreur sur la division"
        )
        self.log.warning("erreur pour division avec str OK")


if __name__ == "__main__":
    unittest.main()
