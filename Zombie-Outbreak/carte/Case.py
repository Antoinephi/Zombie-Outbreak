'''
Created on 27 janv. 2013

@author: Antoine
'''

class Case(): 
    
    
    def __init__(self, coo):
        self.coo = coo
        self.isFog = True
        self.isPietinable = True
        
        
    def setFog(self, isFog):
        self.isFog = isFog
    
    def isFog(self):
        return self.isFog
        
    def isPietinable(self):
        return self.isPietinable
        
    
        
    