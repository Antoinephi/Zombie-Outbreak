'''
Created on 28 janv. 2013

@author: Antoine
'''
from carte import Case, Coordonnees

class Arena:
    ''' int rows : Hauteur de l'arene en cases
       int cols : longueur de l'arene en cases
       Team[] team : tableau contenant les 2 equipes
    '''
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Coordonnees.Coordonnees] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                coo = Coordonnees.Coordonnees(i,j)
                self.grid[i][j] = Case.Case(coo)
        
        
    def afficher(self):
        for i in range(self.rows):
            print(i, end=' ')
        print()
        for i in range(self.rows):
            for j in range(self.cols):
                    self.grid[i][j].afficher()
            print(i)
    