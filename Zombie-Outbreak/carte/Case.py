'''
Created on 27 janv. 2013

@author: Antoine
'''

from entities.Entity import Entity

class Case(): 
    
    
    def __init__(self, coo):
        self.coo = coo
        self.entity = None    
        self.affiche = ' '
        self.isPietinable = True
        
    def getCoo(self):
        return self.coo
        
    def getPietinable(self):
        return self.isPietinable 
    
    def setEntity(self, entity):
        self.entity = entity
        if(entity != None):
            self.entity.setCase(self)
    
    def setAffiche(self, caractere):
        self.affiche = caractere
        
    def getType(self):
        return "case"
        
    def getEntity(self):
        return self.entity
    
    def initializeEntity(self,arena,entity):
        pass
    
    def print_case(self):
        pass