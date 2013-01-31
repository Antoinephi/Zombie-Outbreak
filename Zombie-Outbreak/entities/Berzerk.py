'''
Created on 29 janv. 2013

@author: Antoine
'''

from entities.Entity import Entity

class Berzerk(Entity):
    
    def __int__(self,s):
        super(Berzerk,self).__init__(s)
        self.berzerkDelay = 10
        self.BERZERK_RADIUS = (2)
        
    def printType(self):
        return "B"    