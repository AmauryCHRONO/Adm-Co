#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

import unittest
import logging
from robot.Map import Grid

class TestMoveSeul(unittest.TestCase):
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(3, 3, 1, 0, 0, [[1, 1]], [], [])
        self.log = logging.getLogger()
    
    def test_move_up(self):
        self.assertEqual(
            self.grille.Up(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut seul OK")
    
    def test_move_down(self):
        self.assertEqual(
            self.grille.Down(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas seul OK")
    
    def test_move_up_edge(self):
        self.grille.Up(1) 
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut seul au bort OK")   
        self.grille.Down(1)
    
    def test_move_down_edge(self):
        self.grille.Down(1)
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas seul au bort OK")   
        self.grille.Up(1) 

    def test_move_right(self):
        self.assertEqual(
            self.grille.Right(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite seul OK")
    
    def test_move_left(self):
        self.assertEqual(
            self.grille.Left(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche seul OK")
    
    def test_move_right_edge(self):
        self.grille.Right(1)
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite seul au bort OK")   
        self.grille.Left(1)

    def test_move_left_edge(self):
        self.grille.Left(1)
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche seul au bort OK")   
        self.grille.Up(1)

class TestMoveContreObstacle(unittest.TestCase):
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(3, 3, 1, 1, 0, [[0, 1]], [[1, 1]], [])
        self.log = logging.getLogger()
    
    def test_move_down(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[0, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas contre obstacle OK")
    
    def test_move_right(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 0]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite contre obstacle OK")

    def test_move_up(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut contre obstacle OK")
        

    def test_move_left(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 2]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche contre obstacle OK")

class TestMovePlusieurs(unittest.TestCase):
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(4, 4, 2, 0, 0, [[1, 1],[2, 2]], [], [])
        self.log = logging.getLogger()
    
    def test_move_up_1(self):
        self.assertEqual(
            self.grille.Up(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut du robot 1 OK")
    
    def test_move_down_1(self):
        self.assertEqual(
            self.grille.Down(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas du robot 1 OK")
    
    def test_move_right_1(self):
        self.assertEqual(
            self.grille.Right(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite du robot 1 OK")
    
    def test_move_left_1(self):
        self.assertEqual(
            self.grille.Left(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche du robot 1 OK")

    def test_move_up_2(self):
        self.assertEqual(
            self.grille.Up(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut du robot 2 OK")
    
    def test_move_down_2(self):
        self.assertEqual(
            self.grille.Down(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas du robot 2 OK")
    
    def test_move_right_2(self):
        self.assertEqual(
            self.grille.Right(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite du robot2 OK")
    
    def test_move_left_2(self):
        self.assertEqual(
            self.grille.Left(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche du robot 2 OK")
    
    def test_move_1_sur_2(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 1]
        self.grille.UpdatePos(1)

        self.grille.grid[self.grille.pos[1][0]][self.grille.pos[1][1]] = 0
        self.grille.pos[1]=[1, 2]
        self.grille.UpdatePos(2)

        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement interdit sur le robot 2 pour le robot 1 OK")
    
    def test_move_2_sur_1(self):
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 1]
        self.grille.UpdatePos(1)

        self.grille.grid[self.grille.pos[1][0]][self.grille.pos[1][1]] = 0
        self.grille.pos[1]=[1, 2]
        self.grille.UpdatePos(2)
        self.assertEqual(
            self.grille.Left(2), False, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement interdit sur le robot 1 pour le robot 2 OK")
        

if __name__ == "__main__":
    unittest.main()