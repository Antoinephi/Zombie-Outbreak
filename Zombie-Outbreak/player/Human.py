'''
Created on 29 janv. 2013

@author: Antoine
'''

from player.Entity import Entity
from player.Zombi import Zombi
import random

class Human(Entity):
    
    def __init__(self,s,policier):
        super(Human,self).__init__(s)
        if (policier == True):
            self.setBulletAmount(9)
        
    def transform(self,contA,contC):        
        probaConta = contC / contA
        r = random.random(0.0,100.0)
        if(r > 0 and r < probaConta):
            if (self.getBulletAmount() > 0):
                self = Zombi(self.getName(),True)
            else: 
                self = Zombi(self.getName(),False)
        