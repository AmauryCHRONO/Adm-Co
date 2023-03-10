import unittest
import logging
from Morpion.MorpionGame.MorpionTools import MorpionBoard

class TestPlacement(unittest.TestCase):
    def setUp(self):
        """Executed before every test case"""
        self.jeu = MorpionBoard()
        self.log = logging.getLogger()

    def test_placement_X(self):
        self.assertEqual(
                    self.jeu.Next_move('X', 1)[1], True, "Erreur sur le palcement"
                )
        self.log.warning("test palcement 'X' OK")

    def test_placement_O(self):
        self.assertEqual(
                    self.jeu.Next_move('O', 2)[1], True, "Erreur sur le palcement"
                )
        self.log.warning("test palcement 'O' OK")

    def test_placement_invalide_hors_grille(self):
        self.assertEqual(
                    self.jeu.Next_move('O', 20)[1], False, "Erreur sur le palcement"
                )
        self.log.warning("test palcement hors grille OK")

    def test_placement_invalide_deja_utlilise(self):
        self.jeu.grid[8]='O'
        self.assertEqual(
                    self.jeu.Next_move('O', 9)[1], False, "Erreur sur le palcement"
                )
        self.log.warning("test palcement invalide surune case déjà utilisée OK")
    
class TestVictoir(unittest.TestCase):
    def setUp(self):
        """Executed before every test case"""
        self.jeu = MorpionBoard()
        self.log = logging.getLogger()
    
    def test_victoir_1(self):
        self.jeu.grid[0]='X'
        self.jeu.grid[1]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 3)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 1 OK")
        self.jeu.grid[0]=0
        self.jeu.grid[1]=0
        self.jeu.grid[2]=0

    def test_victoir_2(self):
        self.jeu.grid[3]='X'
        self.jeu.grid[4]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 6)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 2 OK")
        self.jeu.grid[3]=0
        self.jeu.grid[4]=0
        self.jeu.grid[5]=0

    def test_victoir_3(self):
        self.jeu.grid[6]='X'
        self.jeu.grid[7]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 9)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 3 OK")
        self.jeu.grid[6]=0
        self.jeu.grid[7]=0
        self.jeu.grid[8]=0

    def test_victoir_4(self):
        self.jeu.grid[0]='X'
        self.jeu.grid[3]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 7)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 4 OK")
        self.jeu.grid[0]=0
        self.jeu.grid[3]=0
        self.jeu.grid[6]=0

    def test_victoir_5(self):
        self.jeu.grid[1]='X'
        self.jeu.grid[4]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 8)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 5 OK")
        self.jeu.grid[1]=0
        self.jeu.grid[4]=0
        self.jeu.grid[7]=0

    def test_victoir_6(self):
        self.jeu.grid[2]='X'
        self.jeu.grid[5]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 9)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 6 OK")
        self.jeu.grid[2]=0
        self.jeu.grid[5]=0
        self.jeu.grid[8]=0

    def test_victoir_7(self):
        self.jeu.grid[0]='X'
        self.jeu.grid[4]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 9)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 7 OK")
        self.jeu.grid[0]=0
        self.jeu.grid[4]=0
        self.jeu.grid[8]=0

    def test_victoir_8(self):
        self.jeu.grid[2]='X'
        self.jeu.grid[4]='X'
        self.assertEqual(
                    self.jeu.Next_move('X', 7)[0], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 8 OK")
        self.jeu.grid[2]=0
        self.jeu.grid[4]=0
        self.jeu.grid[6]=0

    def test_victoir_9(self):
        self.jeu.grid[0]='X'
        self.jeu.grid[1]='X'
        self.jeu.grid[2]='O'

        self.jeu.grid[3]='O'
        self.jeu.grid[4]='O'
        self.jeu.grid[5]='X'

        self.jeu.grid[6]='X'
        self.jeu.grid[7]='X'
        self.jeu.grid[7]='O'
        self.jeu.coup = 9
        self.assertEqual(
                    self.jeu.Next_move('O', 9)[2], True, "Erreur sur le palcement"
                )
        self.log.warning("test victoir 8 OK")


if __name__ == "__main__":
    unittest.main()