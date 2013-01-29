'''
Created on 28 janv. 2013

@author: jolya
'''

from player.Entity import Entity

class Zombi(Entity):
    
    def __init__(self,s,policier):
        self.ATTACK_RADIUS = (1)
        self.CONTAGION_AMOUNT = (10)
        self.contagionCount = 10
        self.CONTAGION_RADIUS = (2)
        super(Zombi,self).__init__(s)
        if (policier == True):
            super(Zombi,self).setBulletAmount(9)
            
    def getContagionAmount(self):
        return self.CONTAGION_AMOUNT
    
    def getContagionRadius(self):
        return self.CONTAGION_RADIUS
    
    def getContagionCount(self):
        return self.contagionCount
    
    def setContagionCount(self,i):
        self.contagionCount = i
        
    def printType(self):
        return "Z"        