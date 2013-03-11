
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
                    
    def getRows(self):
        return self.rows
    
    def getCols(self):
        return self.cols
        
    def getCase(self,rows,cols):
        return self.grid[rows][cols]
    
    def setCase(self,case):
        rows = case.getCoo().getX()
        cols = case.getCoo().getY()
        self.grid[rows][cols] = case
        
    def print_arena(self):
        for i in range(self.rows):
            print(i),
        print ' '
        for i in range(self.rows):
            for j in range(self.cols):
                    self.grid[i][j].print_case()
            print(i)
    
    def nextTurn(self):
        i = 0 
        j = 0
        list = [6]
        size = 0
        flag = False
        for i in range(self.getRows()):
            for j in range(self.getCols()):
                if(self.getCase(i, j).getEntity() != None):
                    t = 0
                    for t in range(size):
                        if(list[t] == self.getCase(i, j).getEntity()):
                            flag = True
                    if(flag == False):                        
                        if(self.getCase(i, j).getEntity().printType() == 'B'):
                            self.getCase(i, j).getEntity().decrementDelay()
                        self.getCase(i, j).getEntity().getBrain().nextAction()
                        self.killDead()
                        list.append(self.getCase(i, j).getEntity())
                        size += 1
         
    def killDead(self):
        i = 0
        j = 0
        for i in range(self.getRows()):
            for j in range(self.getCols()):
                if(self.getCase(i, j).getEntity() != None):
                    if(not self.getCase(i, j).getEntity().isAlive()):
                        self.getCase(i, j).setEntity(None)
    