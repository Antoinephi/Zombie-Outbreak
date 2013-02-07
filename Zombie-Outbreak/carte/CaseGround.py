'''
Created on 29 janv. 2013

@author: Antoine
'''

from carte.Case import Case

class CaseGround(Case):
    
    def __init__(self, coo):        
        super(CaseGround, self).__init__(coo)
        self.isPietinable = True
        self.affiche = '.'
    
    #Methode pour initialiser une entite dans la case
    def initializeEntity(self,arena,entity):
        print("GROUND")
        self.setEntity(entity)
    
    #Methode pour afficher la case Ground sous forme d'un "." pour le mode textuel du jeu     
    def print_case(self):
            if (self.entity) :
                print (self.entity.printType(), end=' ')
            elif(not self.isFog):
                print(self.affiche, end=' ')
            else:
                print("*", end=' ')
                
    def getType(self):
        return "ground"

        