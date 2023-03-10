#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""


class MorpionBoard:
    """
    Classe simulant un plateau de jeu du morpion.
    """

    def __init__(self):
        """
        Méthode d'initialisation de la classe, initialisation des différentes vraiables de la classe
        """

        # Création de la grille
        self.grid = [0 for j in range(9)]

        # Nombre de coup jouer au totale
        self.coup=0

        # Couple de solution donnant la victoire
        self.winner = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]

    def Print_board(self):
        """
        Méthode permétant l'affichage du plateau de jeu.
        """
        case = 1
        print("---------")
        for i in self.grid:  # Affichage pour toute les cases du plateau
            end = " | "

            if case % 3 == 0:  # Retoure a la ligne après 3 cases d'affichées
                end = " \n"
                if i != 1:
                    end += "---------\n"
            char = " "
            if i in ("X", "O"):
                char = i
                # Affichage des coups joués en fonction du joueur
            case += 1
            print(
                char, end=end
            )  # Affichage soit d'une "|" soit d'un retoure à la ligne.

    def Next_move(self, joueur, case_choisi):
        """
        Méthode permétant de réaliser un coup, indique si le coup est correcte 
        et indique si le coup fait gagner.
        Args :
            joueur(str) : joueur qui fait le coup soit 'X' ou 'O'.
            i(int) : numéor de la case a jouer (entre 1 et 9).
        Returns :
            list of boolean : le premier boolen indique si le coup fait gagner 
                              et le deuxieme indique si le coup est réalisé
                              et le troisieme indique s'il y a match nul      
        """         
        if self.coup == 9:
            return [False,False,True]
        case = 0
        list_case_joueur = []
        if case_choisi > 0 and case_choisi < 10 :
            if self.grid[case_choisi - 1] == 0: # Regarde si la case est libre
                self.grid[case_choisi - 1] = joueur
                for case_id in self.grid: # Opptention des coups du joueur actuel
                    if case_id == joueur:
                        list_case_joueur.append(case)
                        case += 1
                for lis in self.winner:  # Regarde si la combinaison de coup fait gagner
                    win = True
                    for j in lis:
                        if self.grid[j] != joueur:
                            win = False
                            break
                    if win:
                        break
                self.coup+=1
                return [win, True,False]
        return [False, False,False]
        