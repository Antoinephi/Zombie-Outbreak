'''
Created on 28 janv. 2013

@author: jolya
'''

from carte.Direction import Direction

class Entity():
    
    def __init__(self,s,a):
        self.name = s
        self.bulletAmount = 0
        self.alive = True
        self.case = None
        self.arena = a
        self.MOVE_LEN = (1)
        self.VIEW_RADIUS = (3)
        self.SHOT_RADIUS = (3)
        self.SHOT_SUCCESS = (50)
        
    def getName(self):
        return self.name
    
    def getBulletAmount(self):
        return self.bulletAmount
    
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
        if(caseTo.getPietinable() or caseTo.entity):
            caseFrom.setEntity(None)
            caseTo.setEntity(self)
        else:
            print("Deplacement impossible")
        
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