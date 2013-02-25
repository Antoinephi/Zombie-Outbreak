'''
Created on 28 janv. 2013

@author: jolya
'''

from carte.Direction import Direction
from LoadCFG import LoadCFG
import ast

class Entity():
    
    def __init__(self,s,a):
        self.cfg = LoadCFG()
        self.name = s
        self.bulletAmount = 0
        self.alive = True
        self.case = None
        self.arena = a
        self.MOVE_LEN = ast.literal_eval(self.cfg.getData(5))
        self.VIEW_RADIUS = ast.literal_eval(self.cfg.getData(4))
        self.SHOT_RADIUS = ast.literal_eval(self.cfg.getData(9))
        self.SHOT_SUCCESS = ast.literal_eval(self.cfg.getData(10))
        
    def getName(self):
        return self.name
    
    def getBulletAmount(self):
        return self.bulletAmount
    
    def getShotRadius(self):
        return self.SHOT_RADIUS
    
    def getCase(self):
        return self.case
    
    def getArena(self):
        return self.arena
    
    def isAlive(self):
        return self.alive
    
    def setName(self,s):
        self.name = s
        
    def setBulletAmount(self,i):
        self.bulletAmount = i    
    
    def setAlive(self,b):
        self.alive = b  
      
    def setCase(self,c):
        self.case = c
           
    def printType(self):
        pass
    
    def getHit(self):
        self.alive = False
        
    def move(self, direction):
        caseFrom = self.case
        x = caseFrom.getCoo().getX() + direction.x
        y = caseFrom.getCoo().getY() + direction.y
        if(x < 0): 
            x = 0
        if(x >= self.arena.getRows()):
            x = self.arena.getRows() - 1
        if(y < 0): 
            y = 0 
        if(y >= self.arena.getRows()):
            y = self.arena.getRows() - 1
        caseTo = self.getArena().getCase(x, y)
        if(caseTo.getPietinable() and not caseTo.entity):
            caseTo.setEntity(caseFrom.getEntity())
            caseFrom.setEntity(None)
        else:
            print("Deplacement impossible")
            return -1
        
    def tir(self, direction):
        x = self.case.getCoo().getX() + direction.x
        y = self.case.getCoo().getY() + direction.y
        caseTo = self.getArena().getCase(x, y)
        tir = False
        if(self.bulletAmount == 0):
            print("Pas de munition !")
        else:
            while(tir == False):
                if(x < 0 or x >= self.arena.getRows()-1 or y < 0 or y >= self.arena.getCols()-1):
                    print("Rate !")
                    tir = True
                    self.bulletAmount -= 1
                if(caseTo.entity):
                    print("Touche !")
                    caseTo.entity.getHit()
                    tir = True                        
                    self.bulletAmount -= 1
                caseTo.setAffiche('o')
                self.getArena().print_arena()
                if(caseTo.getType() == "ground"):
                    caseTo.setAffiche('.')
                if(caseTo.getType() == "water"):
                    caseTo.setAffiche('~')
                if(tir == False):
                    x = caseTo.getCoo().getX() + direction.x
                    y = caseTo.getCoo().getY() + direction.y
                    caseTo = self.getArena().getCase(x, y)