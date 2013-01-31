'''
Created on 29 janv. 2013

@author: Antoine
'''

from carte.Case import Case

class CaseGround(Case):
    
    def __init__(self, coo):
        super(CaseGround, self).__init__(coo)
        self.entity = None
        
    def afficher(self):
        if (not self.entity) :
            print(".", end=' ')
        else :
            print (self.entity.printType(),end=' ')   
        
    
    def setEntity(self, entity):
        self.entity = entity    
        
    def getEntity(self):
        return self.entity