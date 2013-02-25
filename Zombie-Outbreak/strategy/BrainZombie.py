'''
Created on 4 fevr. 2013

@author: Antoine
'''

import random
from carte.Direction import North, South, West, East

class BrainZombie():
    
    def __init__(self, zombi, arena):
        self.zombi = zombi
        self.arena = arena
        
    def nextAction(self):
        if(self.zombi.isAlive()):
            nbMove = self.zombi.MOVE_LEN 
            while(nbMove > 0):
                if(not self.closerHuman()):
                    error = 0
                    r = random.randint(1,4)
                    if(r == 1):
                        error = self.zombi.move(North)
                        if(error == -1):
                            error = 0
                            error = self.zombi.move(South)
                            if(error == -1):
                                error = 0
                                error = self.zombi.move(West)
                                if(error == -1):
                                    error = 0
                                    error = self.zombi.move(East)
                    elif(r == 2):
                        error = self.zombi.move(South)
                        if(error == -1):
                            error = 0
                            error = self.zombi.move(West)
                            if(error == -1):
                                error = 0
                                error = self.zombi.move(East)
                                if(error == -1):
                                    error = 0
                                    error = self.zombi.move(North)
                    elif(r == 3):
                        error = self.zombi.move(West)
                        if(error == -1):
                            error = 0
                            error = self.zombi.move(East)
                            if(error == -1):
                                error = 0
                                error = self.zombi.move(North)
                                if(error == -1):
                                    error = 0
                                    error = self.zombi.move(South)
                    else:
                        error = self.zombi.move(East)
                        if(error == -1):
                            error = 0
                            error = self.zombi.move(North)
                            if(error == -1):
                                error = 0
                                error = self.zombi.move(South)
                                if(error == -1):
                                    error = 0
                                    error = self.zombi.move(West)
                nbMove -= 1 
        
    def closerHuman(self):
        i = 0
        j = 0
        longueur = 0
        human = None
        for i in range(self.arena.getRows()):
            for j in range(self.arena.getCols()):
                if(self.arena.getCase(i, j).getEntity() != None):
                    if(self.arena.getCase(i, j).getEntity().printType() == "H"):
                        x = self.zombi.getCase().getCoo().getX() - i
                        y = self.zombi.getCase().getCoo().getY() - j
                        if(longueur == 0 or abs(x) + abs(y) < longueur):
                            longueur = abs(x) + abs(y)
                            human = self.arena.getCase(i, j).getEntity()
        if(longueur == 0):
            return False
        elif(longueur <= self.zombi.getContagionRadius()):
            human.getCase().setEntity(human.transform(self.zombi.getContagionAmount(), self.zombi.getContagionCount()))
            return True
        else:
            return False