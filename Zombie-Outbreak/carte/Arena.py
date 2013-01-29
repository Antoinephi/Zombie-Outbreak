'''
Created on 28 janv. 2013

@author: Antoine
'''
from carte.Coordonnees import Coordonnees
from carte.CaseGround import CaseGround
from carte.CaseWater import CaseWater
import random

class Arena:
    ''' int rows : Hauteur de l'arene en cases
       int cols : longueur de l'arene en cases
       Team[] team : tableau contenant les 2 equipes
    '''
    ''' initialise la grille de rows lignes et cols colonnes avec
    aleatoirement une case terre ou eau (0.95 chances pour case terre) '''
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Coordonnees] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                coo = Coordonnees(i,j)
                r = random.randint(0,100)
                if (r < 95):
                    self.grid[i][j] = CaseGround(coo)
                else:
                    self.grid[i][j] = CaseWater(coo)
        
        
        
    def afficher(self):
        for i in range(self.rows):
            print(i, end=' ')
        print()
        for i in range(self.rows):
            for j in range(self.cols):
                    self.grid[i][j].afficher()
            print(i)
    