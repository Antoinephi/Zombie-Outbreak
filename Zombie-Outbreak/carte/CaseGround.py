'''
Created on 29 janv. 2013

@author: Antoine
'''

from carte.Case import Case

class CaseGround(Case):
    
    def __init__(self, coo):
        super(CaseGround, self).__init__(coo)
        
        
    def afficher(self):
        print(".", end=' ')
        
    
    def setEntity(self, entity):
        self.entity = entity    
        
    def getEntity(self):
        return self.entity