'''
Created on 27 janv. 2013

@author: Antoine
'''

class Case(): 
    
    
    def __init__(self, coo):
        self.coo = coo
        self.isFog = True
        self.isPietinable = True
        self.entity = None    
    
    def getCoo(self):
        return self.coo
        
    def setFog(self, isFog):
        self.isFog = isFog
    
    def isFog(self):
        return self.isFog
        
    def isPietinable(self):
        return self.isPietinable 
    
    def setEntity(self, entity):
        self.entity = entity
        if(entity != None):
            self.entity.setCase(self)   
        
    def getEntity(self):
        return self.entity