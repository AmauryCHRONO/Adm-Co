#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

import unittest
import logging
from robot.Map import Grid

class TestMoveSeul(unittest.TestCase):
    """
    Cette classe a pour role de réaliser les tests de déplacements pour un robot seul.
    """
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(3, 3, 1, 0, 0, [[1, 1]], [], [])
        self.log = logging.getLogger()
    
    def test_move_up(self):
        """
        Test du déplecement vers le haut.
        """
        self.assertEqual(
            self.grille.Up(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut seul OK")
    
    def test_move_down(self):
        """
        Test du déplecement vers le bas.
        """
        self.assertEqual(
            self.grille.Down(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas seul OK")
    
    def test_move_up_edge(self):
        """
        Test du déplecement vers le haut au bord.
        """
        self.grille.Up(1) 
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le haut seul au bort OK")   
    
    def test_move_down_edge(self):
        """
        Test du déplecement vers le bas au bord.
        """
        self.grille.Down(1)
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le bas seul au bort OK")   

    def test_move_right(self):
        """
        Test du déplecement vers la gauche.
        """
        self.assertEqual(
            self.grille.Right(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite seul OK")
    
    def test_move_left(self):
        """
        Test du déplecement vers la gauche.
        """
        self.assertEqual(
            self.grille.Left(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche seul OK")
    
    def test_move_right_edge(self):
        """
        Test du déplecement vers la droite au bord.
        """
        self.grille.Right(1)
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la droite seul au bort OK")   

    def test_move_left_edge(self):
        """
        Test du déplecement vers la gauche au bords.
        """
        self.grille.Left(1)
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la gauche seul au bort OK")   

class TestMoveContreObstacle(unittest.TestCase):
    """
    Cette classe a pour role de réaliser les test de déplacement contre un obstacle non bougeable
    """
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(3, 3, 1, 1, 0, [[0, 1]], [[1, 1]], [])
        self.log = logging.getLogger()
    
    def test_move_down_obs(self):
        """
        Test du déplecement vers le bas contre un obstacle.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[0, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le bas contre obstacle OK")
    
    def test_move_right_obs(self):
        """
        Test du déplecement vers la droite contre un obstacle.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 0]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la droite contre obstacle OK")

    def test_move_up_obs(self):
        """
        Test du déplecement vers le haut contre un obstacle.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le haut contre obstacle OK")
        

    def test_move_left_obs(self):
        """
        Test du déplecement vers la gauche contre un obstacle.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 2]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la gauche contre obstacle OK")

class TestMovePlusieurs(unittest.TestCase):
    """
    Cette classe a pour role de réaliser les test de déplacement de diffrents robots.
    """
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(4, 4, 2, 0, 0, [[1, 1],[2, 2]], [], [])
        self.log = logging.getLogger()
    
    def test_move_up_1(self):
        """
        Test du déplecement vers le haut du robot 1.
        """
        self.assertEqual(
            self.grille.Up(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut du robot 1 OK")
    
    def test_move_down_1(self):
        """
        Test du déplecement vers le bas du robot 1.
        """
        self.assertEqual(
            self.grille.Down(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas du robot 1 OK")
    
    def test_move_right_1(self):
        """
        Test du déplecement vers la droite du robot 1.
        """
        self.assertEqual(
            self.grille.Right(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite du robot 1 OK")
    
    def test_move_left_1(self):
        """
        Test du déplecement vers la gauche du robot 1.
        """
        self.assertEqual(
            self.grille.Left(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche du robot 1 OK")

    def test_move_up_2(self):
        """
        Test du déplecement vers le haut du robot 2.
        """
        self.assertEqual(
            self.grille.Up(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut du robot 2 OK")
    
    def test_move_down_2(self):
        """
        Test du déplecement vers le bas du robot 2.
        """
        self.assertEqual(
            self.grille.Down(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas du robot 2 OK")
    
    def test_move_right_2(self):
        """
        Test du déplecement vers la droite du robot 2.
        """
        self.assertEqual(
            self.grille.Right(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite du robot2 OK")
    
    def test_move_left_2(self):
        """
        Test du déplecement vers la gauche du robot 2.
        """
        self.assertEqual(
            self.grille.Left(2), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche du robot 2 OK")
    
    def test_move_1_sur_2(self):
        """
        Test du déplecement du robot 1 sur le robot 2.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 1]
        self.grille.UpdatePos(1)

        self.grille.grid[self.grille.pos[1][0]][self.grille.pos[1][1]] = 0
        self.grille.pos[1]=[1, 2]
        self.grille.UpdatePos(2)

        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement interdit sur le robot 2 pour le robot 1 OK")
    
    def test_move_2_sur_1(self):
        """
        Test du déplecement du robot 2 sur le robot 1.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[1, 1]
        self.grille.UpdatePos(1)

        self.grille.grid[self.grille.pos[1][0]][self.grille.pos[1][1]] = 0
        self.grille.pos[1]=[1, 2]
        self.grille.UpdatePos(2)
        self.assertEqual(
            self.grille.Left(2), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement interdit sur le robot 1 pour le robot 2 OK")

class TestMoveObstacle(unittest.TestCase):
    """
    Cette classe a pour role de réaliser les test de déplacement contre un obstacle déplaçable.
    """
    def setUp(self):
        """Executed before every test case"""
        self.grille = Grid(5, 5, 1, 1, 1, [[1, 2]], [[4, 4]], [[2, 2]])
        self.log = logging.getLogger()

    def test_move_down_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le bas.
        """
        self.assertEqual(
            self.grille.Down(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le bas de l'obstacle par le robot 1 OK")

    def test_move_up_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le haut.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[3, 2]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Up(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers le haut de l'obstacle par le robot 1 OK")

    
    def test_move_right_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la droite.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Right(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la droite de l'obstacle par le robot 1 OK")

    def test_move_left_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la gauche.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 3]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Left(1), True, "Erreur sur le déplacement"
        )
        self.log.warning("test déplacement vers la gauche de l'obstacle par le robot 1 OK")

    def test_move_up_obstacle_edge(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le haut contre le bord.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[0, 2]
        self.grille.UpdatePos(1,'M')
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le haut de l'obstacle par le robot 1  au bord OK")

    def test_move_down_obstacle_edge(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le bas contre le bord.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[4, 2]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[3, 2]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le bas de l'obstacle par le robot 1  au bord OK")

    def test_move_right_obstacle_edge(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la droite contre le bord.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[2, 4]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 3]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la droite de l'obstacle par le robot 1  au bord OK")

    def test_move_left_obstacle_edge(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la gauche contre le bord.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[2, 0]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 1]
        self.grille.UpdatePos(1)
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la gauche de l'obstacle par le robot 1  au bord OK")

    def test_move_right_obstacle_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la droite contre un bostacle non déplaçable.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[2, 1]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 0]
        self.grille.UpdatePos(1)
        self.grille.grid[self.grille.pos_ob[0][0]][self.grille.pos_ob[0][1]] = 0
        self.grille.pos_ob[0]=[2, 2]
        self.grille.UpdatePos(0,'X')
        self.assertEqual(
            self.grille.Right(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la droite de l'obstacle par le robot 1 contre un obstacle non bougeable OK")

    def test_move_left_obstacle_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers la gauche contre un bostacle non déplaçable.
        """
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[2, 3]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[2, 4]
        self.grille.UpdatePos(1)
        self.grille.grid[self.grille.pos_ob[0][0]][self.grille.pos_ob[0][1]] = 0
        self.grille.pos_ob[0]=[2, 2]
        self.grille.UpdatePos(0,'X')
        self.assertEqual(
            self.grille.Left(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers la gauche de l'obstacle par le robot 1 contre un obstacle non bougeable OK")

    def test_move_down_obstacle_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le bas contre un bostacle non déplaçable.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[0, 2]
        self.grille.UpdatePos(1)
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[1, 2]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos_ob[0][0]][self.grille.pos_ob[0][1]] = 0
        self.grille.pos_ob[0]=[2, 2]
        self.grille.UpdatePos(0,'X')
        self.assertEqual(
            self.grille.Down(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le bas de l'obstacle par le robot 1 contre un obstacle non bougeable OK")

    def test_move_up_obstacle_obstacle(self):
        """
        Test du déplecement du déplacement de l'obstacle vers le haut contre un bostacle non déplaçable.
        """
        self.grille.grid[self.grille.pos[0][0]][self.grille.pos[0][1]] = 0
        self.grille.pos[0]=[4, 2]
        self.grille.UpdatePos(1)
        self.grille.grid[self.grille.pos_ob_mouv[0][0]][self.grille.pos_ob_mouv[0][1]] = 0
        self.grille.pos_ob_mouv[0]=[3, 2]
        self.grille.UpdatePos(1,'M')
        self.grille.grid[self.grille.pos_ob[0][0]][self.grille.pos_ob[0][1]] = 0
        self.grille.pos_ob[0]=[2, 2]
        self.grille.UpdatePos(0,'X')
        self.assertEqual(
            self.grille.Up(1), False, "Erreur sur le déplacement"
        )
        self.log.warning("test non déplacement vers le haut de l'obstacle par le robot 1 contre un obstacle non bougeable OK")

if __name__ == "__main__":
    unittest.main()