'''
Created on 31 janv. 2013

@author: Antoine
'''
from entities.Zombi import Zombi

class Team():
    
    def __init__(self,name,nbZombi):
        self.name = name
        self.inGame = True
        self.zombis = [None] * nbZombi
        for i in range(nbZombi):
            j = str(i+1)
            s = "Zombi " + j
            self.zombis[i] = Zombi(s,False)
            
    def printTeam(self):
        for i in range(len(self.zombis)):
            print(self.zombis[i].getName())
            
    def getList(self):
        return self.zombis 
    
    def getZombi(self,index):
        return self.zombis[index]