'''
Created on 29 janv. 2013

@author: Antoine
'''

from carte.Case import Case

class CaseGround(Case):
    
    def __init__(self, coo):        
        Case.__init__(self, coo)
        self.isPietinable = True
        self.affiche = '.'
    
    #Methode pour initialiser une entite dans la case
    def initializeEntity(self,arena,entity):
        print("GROUND")
        self.setEntity(entity)
    
    #Methode pour afficher la case Ground sous forme d'un "." pour le mode textuel du jeu     
    def print_case(self):
            if (self.entity) :
                print (self.entity.printType()),
            else:
                print(self.affiche),
                
    def getType(self):
        return "ground"

        