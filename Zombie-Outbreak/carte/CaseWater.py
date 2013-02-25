'''
Created on 29 janv. 2013

@author: Antoine
'''
from carte.Case import Case
from carte.CaseGround import CaseGround

class CaseWater(Case):
    
    def __init__(self, coo):
        Case.__init__(self, coo)
        self.isPietinable = False
        self.affiche = '~'
    
    #Methode pour initialiser une entite dans la case et transforme la case Water en case Ground
    def initializeEntity(self,arena,entity):
        case = self
        print("WATER TO GROUND")
        case = CaseGround(case.getCoo())
        arena.setCase(case)
        case.setEntity(entity)
    
    #Methode pour afficher la case Water sous forme d'un "~" pour le mode textuel du jeu              
    def print_case(self):
            if (self.entity) :
                print(self.entity.printType()),
            else:
                print(self.affiche),
                
    def getType(self):
        return "water"