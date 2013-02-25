'''
Created on 29 janv. 2013

@author: Antoine
'''

from entities.Entity import Entity
from entities.Zombi import Zombi
from entities.Berzerk import Berzerk
import ast
import random

class Human(Entity):
    
    def __init__(self,s,policier,a):
        Entity.__init__(self,s,a)
        if (policier == True):
            self.setBulletAmount(ast.literal_eval(self.cfg.getData(11)))
    
    def printType(self):
        return "H"
        
    def transform(self,contA,contC):        
        probaConta = contC / contA
        r = (random.random())
        print(probaConta , r) 
        if(r >= 0 and r <= probaConta):
            if (self.getBulletAmount() > 0):
                return Zombi(self.getName(),True,self.getArena())
            else: 
                return Zombi(self.getName(),False,self.getArena())
        else:
            probaConta = ((contA - contC) / contA) * (1/4)
            if(r >= 0 and r <= probaConta):
                return Berzerk(self.getName(),self.getArena())
            else:
                self.setAlive(False)
                return self
                