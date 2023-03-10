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

    def test_add(self):
        """Somme de deux complexes, le résultat doit être -1-i"""
        self.assertEqual(
            self.calculator.add((3, -6), (-4, 5)), (-1, -1), "Erreur sur la somme"
        )
        self.log.warning("test somme OK")

    def test_add_str(self):
        """Somme d'un complexe et d'un caractère, le résultat doit être une erreur"""
        with self.assertRaises(TypeError):
            self.calculator.add((2, 1), "49")
        self.log.warning("erreur pour somme avec str OK")


class TestSub(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode sub dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_sub(self):
        """Soustraction de deux complexes, le résultat doit être 9+3i"""
        self.assertEqual(
            self.calculator.sub((5, 4), (-4, 1)), (9, 3), "Erreur sur la différence"
        )
        self.log.warning("test différence OK")

    def test_sub_str(self):
        """Soustraction d'un complexe et d'un caractère, le résultat doit être une erreur"""
        with self.assertRaises(TypeError):
            self.calculator.sub((1, 2), "23")
        self.log.warning("erreur pour différence avec str OK")


class TestMul(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode mul dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_mul(self):
        """Multiplication de deux complexes, le résultat doit être 10-24i"""
        self.assertEqual(
            self.calculator.mul((2, 3), (-4, -6)),
            (10, -24),
            "Erreur sur la multiplication",
        )
        self.log.warning("test multiplication OK")

    def test_mul_str(self):
        """Multiplication d'un complexe et d'un caractère, le résultat doit être une erreur"""
        with self.assertRaises(TypeError):
            self.calculator.mul((6, 1), "55")
        self.log.warning("erreur pour multiplication avec str OK")


class TestDiv(unittest.TestCase):
    """Cette classe a pour role de réaliser les tests pour la methode div dans Calculator.py
    et vérifier son bon fonctionnement"""

    def setUp(self):
        """Executed before every test case"""
        self.calculator = SimpleComplexCalculator()
        self.log = logging.getLogger()

    def test_div(self):
        """Division de deux complexes, le résultat doit être 2i"""
        self.assertEqual(
            self.calculator.div((4, 4), (2, -2)), (0, 2), "Erreur sur la division"
        )
        self.log.warning("test division OK")

    def test_div_0(self):
        """Division d'un complexe et 0, le résultat doit être une erreur"""
        with self.assertRaises(ZeroDivisionError):
            self.calculator.div((4, 4), (0, 0))
        self.log.warning("erreur pour division par 0 OK")

    def test_div_str(self):
        """Division d'un complexe et d'un caractère, le résultat doit être une erreur"""
        with self.assertRaises(TypeError):
            self.calculator.div((5, 4), "51")
        self.log.warning("erreur pour division avec str OK")


if __name__ == "__main__":
    unittest.main()
