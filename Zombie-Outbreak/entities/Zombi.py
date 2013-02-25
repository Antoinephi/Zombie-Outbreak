'''
Created on 28 janv. 2013

@author: jolya
'''

from entities.Entity import Entity
import ast

class Zombi(Entity):
    
    def __init__(self,s,policier,a):
        Entity.__init__(self,s,a)
        self.ATTACK_RADIUS = (self.cfg.getData(1))
        self.CONTAGION_AMOUNT = ast.literal_eval(self.cfg.getData(6))
        self.contagionCount = ast.literal_eval(self.cfg.getData(6))
        self.CONTAGION_RADIUS = ast.literal_eval(self.cfg.getData(12))
        if (policier == True):
            self.setBulletAmount(self.cfg.getData(11))
            
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