'''
Created on 24 janv. 2013

@author: Antoine
'''

class Coordonnees:

    def __init__(self, x , y ):
        self.x = x
        self.y = y    
  
    def getCoo(self):
        return self.x, self.y
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def toString(self):
        return "[%i][%i]"%(self.x, self.y) 
    