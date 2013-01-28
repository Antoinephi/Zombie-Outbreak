'''
Created on 27 janv. 2013

@author: Antoine
'''
from carte import Coordonnees

class Case: 
    
    
    def __init__(self, coo):
        self.coo = coo
        
    def afficher(self):
        print(".", end=' ')
        
    