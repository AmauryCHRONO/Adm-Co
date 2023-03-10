#!/usr/bin/env python
# coding: utf-8
"""
author : Amaury CHRONOWSKI

"""

import os
import time
import keyboard # Inutilisable en environnement virtuelle

class Grid:
    """
    Cette classe a pour role de simuler un environement decoupé en grille
    dans le quelle se trouve des robots. Ceux-ci sont representés par des nombres
    et peuvent se deplace dans 4 dirrections. Il ne peuvent pas dépacer les limte du terrain 
    et aller sur une case déjà occupé
    """
    
    def __init__(self, nb_lignes = 0, nb_colones = 0, nb_robots = 0, nb_obstacles = 0, nb_obstacle_mouv = 0, pos = [], pos_ob = [], pos_ob_mouv = []):
        """
        Méthode d'initialisation de la classe. Elle construit la grille et place les élements entrées en paramètre.
        
        Args:
            nb_lignes (int, optional): Nombres de lignes de la grille
            nb_colones (int, optional): Nombres de colonnes de la grille
            nb_robots (int, optional): Nombres de robots. Defaults to 0.
            nb_obstacles (int, optional): Nombres d'obstacles. Defaults to 0.
            nb_obstacle_mouv (int, optional): Nombres d'obstacles déplaçables. Defaults to 0.
            pos (list of list, optional): Position des robots, les coordonnées sont stocké dans unbe liste du type [x=, y=]. Defaults to [].
            pos_ob (list of list, optional): Position des obstacles, les coordonnées sont stocké dans unbe liste du type [x=, y=]. Defaults to [].
            pos_ob_mouv (list of list, optional): Position des obstacles déplaçables, les coordonnées sont stocké dans unbe liste du type [x=, y=] . Defaults to [].
        """
        
        #Variables de compte des objets
        self.nb_robots = nb_robots
        self.nb_obstacles = nb_obstacles
        self.nb_obstacle_mouv = nb_obstacle_mouv
        
        #Variables de psoition des objets      
        self.pos = pos
        self.pos_ob = pos_ob
        self.pos_ob_mouv = pos_ob_mouv
        
        #Variables de la grille
        self.nb_lignes = nb_lignes
        self.nb_colones = nb_colones
        self.grid = [[ 0 for i in range(self.nb_colones)] for j in range(self.nb_lignes)]
        
        #Positionnement de tout les robots 
        for robot in range(self.nb_robots):
            self.UpdatePos(robot+1)
            
        #Positionnement de tout les obtacles            
        for obstacle in range(self.nb_obstacles):
            if self.pos_ob[obstacle] not in self.pos :
                self.UpdatePos(obstacle, "X")

        #Positionnement de tout les obstacles déplaçables               
        for obstacle in range(self.nb_obstacle_mouv):
            if self.pos_ob_mouv[obstacle] not in self.pos and self.pos_ob_mouv[obstacle] not in self.pos_ob :
                self.UpdatePos(obstacle, "M")
     

    def UpdatePos(self,num_obj = 0, type_obj = "R", add = [0, 0]) :
        """
        Méthode qui met à jour la position de l'objet voulu avec la modification de coordonnée voulu.
        
        Args:
            num_obj (int, optional): Numéro de l'objet. Defaults to 0.
            type_obj (str, optional): Type de l'objet. Defaults to "R".
            add (list, optional): Modification à apporter aux coordonnées de l'objet. Defaults to [0, 0].
        """
        
        #Robot
        if type_obj == "R" :
            self.grid[self.pos[num_obj-1][0]][self.pos[num_obj-1][1]] = 0
            self.pos[num_obj-1][0],self.pos[num_obj-1][1] = self.pos[num_obj-1][0]+add[0],self.pos[num_obj-1][1]+add[1]
            self.grid[self.pos[num_obj-1][0]][self.pos[num_obj-1][1]] = num_obj
        
        #Obstacle   
        elif type_obj == "X" :
            self.grid[self.pos_ob[num_obj][0]][self.pos_ob[num_obj][1]] = type_obj
        
        #Obstacle déplaçable    
        elif type_obj == "M" :
            self.grid[self.pos_ob_mouv[num_obj-1][0]][self.pos_ob_mouv[num_obj-1][1]] = 0
            self.pos_ob_mouv[num_obj-1][0],self.pos_ob_mouv[num_obj-1][1] = self.pos_ob_mouv[num_obj-1][0]+add[0],self.pos_ob_mouv[num_obj-1][1]+add[1]
            self.grid[self.pos_ob_mouv[num_obj-1][0]][self.pos_ob_mouv[num_obj-1][1]] = type_obj
        
        
    def Print(self):
        """
        Méthode d'affichage de la grille
        """
        
        for ligne in self.grid:
            print("|", *ligne, sep=' ', end=' |\n')
        print('\n')


    def Up(self, num_rob):
        """
        Méthode qui permet de bouger le robot voulu vers le haut, et bouge automatiquement un obstacle déplaçable si son mouvement est autorisé.

        Args:
            num_rob (int): Numéro du robot.

        Returns:
            boolean: Indique si le déplacement est réalisable
        """
        
        add = [-1, 0]
        if self.try_rob(num_rob): # Regarde si le robot existe
            cell =[self.pos[num_rob-1][0]-1,self.pos[num_rob-1][1]]
            ret = self.isCellEmpty(cell, 'U', 'R') # Regarde si la case suivante est disponible
            if ret[0]:
                cell =[self.pos[num_rob-1][0]-1,self.pos[num_rob-1][1]]
                self.mouvObstacle(ret, cell, add)
                self.UpdatePos(num_rob, 'R', add)
                return True
        return False


    def Down(self, num_rob):
        """
        Méthode qui permet de bouger le robot voulu vers le bas, et bouge automatiquement un obstacle déplaçable si son mouvement est autorisé.

        Args:
            num_rob (int): Numéro du robot.

        Returns:
            boolean: Indique si le déplacement est réalisable
        """
        
        add = [1, 0]
        if self.try_rob(num_rob): # Regarde si le robot existe
            cell =[self.pos[num_rob-1][0]+1,self.pos[num_rob-1][1]]
            ret = self.isCellEmpty(cell, 'D', 'R') # Regarde si la case suivante est disponible
            if ret[0]:
                cell =[self.pos[num_rob-1][0]+1,self.pos[num_rob-1][1]]
                self.mouvObstacle(ret, cell, add)
                self.UpdatePos(num_rob, 'R', add)
                return True
        return False


    def Right(self, num_rob):
        """
        Méthode qui permet de bouger le robot voulu vers la droite, et bouge automatiquement un obstacle déplaçable si son mouvement est autorisé.

        Args:
            num_rob (int): Numéro du robot.

        Returns:
            boolean: Indique si le déplacement est réalisable
        """
        
        add = [0, 1]
        if self.try_rob(num_rob): # Regarde si le robot existe
            cell =[self.pos[num_rob-1][0],self.pos[num_rob-1][1]+1]
            ret = self.isCellEmpty(cell, 'R', 'R') # Regarde si la case suivante est disponible
            if ret[0]:
                cell =[self.pos[num_rob-1][0],self.pos[num_rob-1][1]+1]
                self.mouvObstacle(ret, cell, add)
                self.UpdatePos(num_rob, 'R', add)
                return True
        return False


    def Left(self, num_rob):
        """
        Méthode qui permet de bouger le robot voulu vers la gauche, et bouge automatiquement un obstacle déplaçable si son mouvement est autorisé.

        Args:
            num_rob (int): Numéro du robot.

        Returns:
            boolean: Indique si le déplacement est réalisable
        """
        
        add = [0, -1]
        if self.try_rob(num_rob): # Regarde si le robot existe
            cell =[self.pos[num_rob-1][0],self.pos[num_rob-1][1]-1]
            ret = self.isCellEmpty(cell, 'L', 'R') # Regarde si la case suivante est disponible
            if ret[0]:
                cell =[self.pos[num_rob-1][0],self.pos[num_rob-1][1]-1]
                self.mouvObstacle(ret, cell, add)
                self.UpdatePos(num_rob, 'R', add)
                return True
        return False
    
    
    def try_rob(self, num_rob):
        """
        Méhode qui permet de savoir si le robot existe

        Args:
            num_rob (int): Numéro du robot.

        Returns:
            boolean: Indique si le robot existe.
        """
        
        if num_rob > self.nb_robots :
            print("Numéro de robot inexistant.\n")
            return False
        return True
    
    
    def isCellEmpty(self, cell, dir, type_obj = 'R'):
        """
        Méthode qui permet de savoir si la case dans la quel va se déplace l'objet est vide ou que le déplacement de l'objet dans cette case est possible.

        Args:
            cell (list): Coordonnées de la case du déplacement
            dir (str): Direction du déplacement
            type_obj (str, optional): Type de l'objet. Defaults to 'R'.

        Returns:
            list: indique si la case est vide ou que le délacement d'un objet déplaçable est possible avec son type.
        """
        
        if cell[0] >= 0 and cell[0] <= self.nb_colones-1 and cell[1] >= 0 and cell[1] <= self.nb_lignes-1 :
            if self.grid[cell[0]][cell[1]] == 0:
                return [True, 0]
            elif self.grid[cell[0]][cell[1]] == "M" and type_obj == 'R':
                temp=cell
                if dir == "R":
                    temp[1] = temp[1]+1  
                elif dir == "L":
                    temp[1] = temp[1]-1
                elif dir == "U":
                    temp[0] = temp[0]-1
                elif dir == "D":
                    temp[0] = temp[0]+1
                ret = self.isCellEmpty(temp, dir, "M")
                if ret[0]:                
                    return [True, 'M']
        return [False, 0]
                
                
    def mouvObstacle(self, Val, cell, add):
        """
        Méthode qui permet de bouger les obstacle déplaçable.

        Args:
            Val (list): Indique si la case est vide ou que le délacement de l'objet est possible et que type d'objet est la case s'il y a déplacement.
            cell (list): Coordonné de la case actuel.
            add (list): Modification à aporter au coordonnées.
        
        Returns :
            boolean (boolean): Indique si le déplacement de l'obstacle a été fait.
        """
        
        if Val[1] == "M":
            ind = self.pos_ob_mouv.index(cell)
            self.UpdatePos(ind, 'M', add)
            return True
        return False


    def initiallisation(self):
        """
        Méthode qui pertmet la saisi des différent éléments qui compose la grille ainsi que sa taille.
        """
        self.creaGrille()
        self.positionRobots()
        self.posistionObstacle()
        self.posistionObstacleDeplcable()
        

    def creaGrille(self):
        """
        Méthode qui permet de paramètrer la taille de la grille qaund elle n'est pas renseignée
        """

        OK = True
        while OK : # Saisi protégée
            taille = input("Veuillez renter la taille de la grille (sous forme : x,y):\n")
            taille=taille.split(",")      
            try : # Test si les valeurs saisi sont conformes 
                self.nb_lignes = int(taille[0])
                self.nb_colones = int(taille[1])
            except :
                print("Vous avez renté une valeur incorrecte.\n")
            else : 
                OK = False
        self.grid = [[ 0 for i in range(self.nb_colones)] for j in range(self.nb_lignes)] # Création de la grille
        

    def positionRobots(self):
        """
        Méthode qui permet de renseigner le nombre de robot et leur posistion sur la grille.
        """
        OK = True
        while OK : # Saisi protégée
            nb_robots = input("Veuillez renter un nombre de robots :\n")
            try : # Test si les valeurs saisi sont conformes 
                self.nb_robots = int(nb_robots)
                if self.nb_robots > self.nb_lignes*self.nb_colones :
                    int("a")
            except :
                print("Vous avez renté une valeur incorrecte ou trop grande.\n")
            else : 
                OK = False

        for robot in range(self.nb_robots): # Saisi des coordonées de chaque robot
            OK = True
            while OK : # Saisi protégée
                coord = input("Veuillez rentrer les coordonnées du robot n°" + str(robot + 1) + " (exemple : 4,5; x allant de 0 à " + str(self.nb_colones-1) + " et y allant de 0 à " + str(self.nb_lignes-1) + "):\n")
                x = coord[0]
                y = coord[-1]
                try:
                    x = int(x)
                    y = int(y)
                    if self.grid[x][y] == 0 : # Regarde si les coordonnées saisi sont libre
                        self.grid[x][y] = robot + 1
                    else :
                        print("Vous avez déjà entré ces coordonnées\n")
                        int("a")
                except:
                    print("Vous n'avez pas rentrer de valeur correcte, recommencer.\n")
                else:
                    OK = False
            self.pos.append([x, y])


    def posistionObstacle(self):
        """
        Méthode qui permet de renseigner le nombre d'obstacle et leur posistion sur la grille. 
        """
        OK = True
        while OK : # Saisi protégée
            nb_obstacles = input("Veuillez renter un nombre d'obstacle :\n")
            try : # Test si les valeurs saisi sont conformes 
                self.nb_obstacles = int(nb_obstacles)
                if self.nb_obstacles > self.nb_lignes*self.nb_colones-self.nb_robots :
                    int("a")
            except :
                print("Vous avez renté une valeur incorrecte ou trop grande.\n")
            else : 
                OK = False

        for obstacle in range(self.nb_obstacles): # Saisi des coordonées de chaque obstacle
            OK = True
            while OK : # Saisi protégée
                coord = input("Veuillez rentrer les coordonnées de l'obstacle n°" + str(obstacle + 1) + " (exemple : 4,5; x allant de 0 à " + str(self.nb_colones-1) + " et y allant de 0 à " + str(self.nb_lignes-1) + "):\n")
                x = coord[0]
                y = coord[-1]
                try:
                    x = int(x)
                    y = int(y)
                    if self.grid[x][y] == 0 : # Regarde si les coordonnées saisi sont libre
                        self.grid[x][y] = "X"
                    else :
                        print("Vous avez déjà entré ces coordonnées\n")
                        int("a")
                except:
                    print("Vous n'avez pas rentrer de valeur correcte, recommencer.\n")
                else:
                    OK = False
            self.pos_ob.append([x, y])


    def posistionObstacleDeplcable(self):
        """
        Méthode qui permet de renseigner le nombre d'obstacle déplaçable et leur posistion sur la grille. 
        """
        OK = True
        while OK : # Saisi protégée
            nb_obstacle = input("Veuillez renter un nombre d'obstacle déplaçable :\n")
            try : # Test si les valeurs saisi sont conformes
                self.nb_obstacle_mouv = int(nb_obstacle)
                if self.nb_obstacle_mouv > self.nb_lignes*self.nb_colones-self.nb_robots-self.nb_obstacles :
                    int("a")
            except :
                print("Vous avez renté une valeur incorrecte ou trop grande.\n")
            else : 
                OK = False

        for obstacle in range(self.nb_obstacle_mouv): # Saisi des coordonées de chaque obstacle
            OK = True
            while OK : # Saisi protégée
                coord = input("Veuillez rentrer les coordonnées de l'obstacle déplaçable n°" + str(obstacle + 1) + " (exemple : 4,5; x allant de 0 à " + str(self.nb_colones-1) + " et y allant de 0 à " + str(self.nb_lignes-1) + "):\n")
                x = coord[0]
                y = coord[-1]
                try:
                    x = int(x)
                    y = int(y)
                    if self.grid[x][y] == 0 : # Regarde si les coordonnées saisi sont libre
                        self.grid[x][y] = "M"
                    else :
                        print("Vous avez déjà entré ces coordonnées\n")
                        int("a")
                except:
                    print("Vous n'avez pas rentrer de valeur correcte, recommencer.\n")
                else:
                    OK = False
            self.pos_ob_mouv.append([x, y])

    def lancement(self):
        """
        Méthode permetant de déplacer le robot voulu avec les touches du clavier. Inutilisable en environnement virtuelle.
        """
        OK = True
        print("Pour choisir le robot à déplacer utiliser la touche de selection et entrer le numéro du robot voulu (Cous commencer avec le n°1).\nSTART = 'x'.")
        while(OK): # Attente pour commencer la simulation
            if keyboard.is_pressed("x"):
                OK = False
                Simulation = True

        current_rob = 1 # Robot n°1 par defaut au commencement de la simulation
        self.affichageSimulation()
        while(Simulation):
            if keyboard.is_pressed("e"): # Arret de la simulation 
                Simulation = False

            if keyboard.is_pressed("w"): # Déplacement vers le haut
                self.Up(current_rob)
                self.affichageSimulation()

            if keyboard.is_pressed("s"): # Déplacement vers le bas
                self.Down(current_rob)
                self.affichageSimulation()

            if keyboard.is_pressed("a"): # Déplacement vers la gauche
                self.Left(current_rob)
                self.affichageSimulation()

            if keyboard.is_pressed("d"): # Déplacement vers la droite
                self.Right(current_rob)
                self.affichageSimulation()

            if keyboard.is_pressed("r"):# Changement de robot
                os.system('cls')
                TEST = True
                while TEST : # Saisi Protégée
                    rob = input("Veuillez rentrer le numéro du robot voulu:\n")
                    try: # Test si les valeurs saisi sont conformes
                        rob = int(rob)
                        if rob > self.nb_robots :
                            print("Vous avez entré un numéro éronnée\n")
                            int("a")
                    except:
                        print("Vous n'avez pas rentrer de valeur correcte, recommencer.\n")
                    else:
                        TEST = False
                self.affichageSimulation()
                current_rob = rob

    def affichageSimulation(self):
        """
        Méthode qui permet le rafréchissment/affichage de la grille lors de la simulation controllée par clavier
        """
        time.sleep(0.1)
        os.system('cls')
        self.Print()
        print("\n")
        print("UP = 'z', DOWN = 's', LEFT = 'q', RIGHT = 'd', ROBOT CHOICE = 'r', EXIT = 'e'.\n")



if __name__ == "__main__":  # Test de la class
    test=Grid(3, 3, 1, 1, 0, [[0, 1]], [[1, 1]], [])
    test.Print()


    




