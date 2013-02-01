'''
Created on 28 janv. 2013

@author: jolya
'''

class Entity():
    
    def __init__(self,s):
        self.name = s
        self.bulletAmount = 0
        self.alive = True
        self.case = None
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
   
        
    