'''
Created on 29 janv. 2013

@author: Antoine
'''
from carte.Case import Case

class CaseWater(Case):
    
    def __init__(self, coo):
        self.isPietinable = False
        super(CaseWater,self).__init__(coo)
              
    def afficher(self):
        print("~", end=' ')