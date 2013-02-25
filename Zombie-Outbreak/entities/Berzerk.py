'''
Created on 29 janv. 2013

@author: Antoine
'''

from entities.Entity import Entity
import ast 

class Berzerk(Entity):
    
    def __init__(self,s,a):
        Entity.__init__(self,s,a)
        self.berzerkDelay = ast.literal_eval(self.cfg.getData(7))
        self.BERZERK_RADIUS = ast.literal_eval(self.cfg.getData(2))
        
    def printType(self):
        return "B"    
    
    def getBerzerkDelay(self):
        return self.berzerkDelay
    
    def decrementDelay(self):
        self.berzerkDelay -= 1
    def getBerzerkRadius(self):
        return self.BERZERK_RADIUS
    
    def explose(self):
        print("BOOM")
        self.getHit()
        i = 0
        j = 0
        for i in range(self.arena.getRows()):
            for j in range(self.arena.getCols()):
                if(self.arena.getCase(i, j).getEntity() != None):
                    x = self.getCase().getCoo().getX() - i
                    y = self.getCase().getCoo().getY() - j
                    if(abs(x) + abs(y) <= self.getBerzerkRadius()):
                        self.arena.getCase(i, j).getEntity().getHit()
                    