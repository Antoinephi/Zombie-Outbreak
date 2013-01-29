'''
Created on 29 janv. 2013

@author: Antoine
'''

from player.Entity import Entity
from player.Zombi import Zombi
from player.Berzerk import Berzerk

import random

class Human(Entity):
    
    def __init__(self,s,policier):
        super(Human,self).__init__(s)
        if (policier == True):
            self.setBulletAmount(9)
    
    def printType(self):
        return "H"
        
    def transform(self,contA,contC):        
        probaConta = contC / contA
        r = (random.random())
        print(probaConta , r) 
        if(r >= 0 and r <= probaConta):
            if (self.getBulletAmount() > 0):
                return Zombi(self.getName(),True)
            else: 
                return Zombi(self.getName(),False)
        else:
            probaConta = ((contA - contC) / contA) * (1/4)
            if(r >= 0 and r <= probaConta):
                return Berzerk(self.getName())
            else:
                self.setAlive(False)    