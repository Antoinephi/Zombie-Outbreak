'''
Created on 20 fevr. 2013

@author: Nicolas
'''

from carte.Direction import *
import random

class BrainPolicier():
    
    def __init__(self, entity, arena):
        self.entity = entity
        self.arena = arena

    def nextAction(self):
        if(self.entity.isAlive()):
            nbMove = self.entity.MOVE_LEN 
            while(nbMove > 0):
                if(not self.closerZombi()):
                    error = 0
                    r = random.randint(1,4)
                    if(r == 1):
                        error = self.entity.move(North)
                        if(error == -1):
                            error = 0
                            error = self.entity.move(South)
                            if(error == -1):
                                error = 0
                                error = self.entity.move(West)
                                if(error == -1):
                                    error = 0
                                    error = self.entity.move(East)
                    elif(r == 2):
                        error = self.entity.move(South)
                        if(error == -1):
                            error = 0
                            error = self.entity.move(West)
                            if(error == -1):
                                error = 0
                                error = self.entity.move(East)
                                if(error == -1):
                                    error = 0
                                    error = self.entity.move(North)
                    elif(r == 3):
                        error = self.entity.move(West)
                        if(error == -1):
                            error = 0
                            error = self.entity.move(East)
                            if(error == -1):
                                error = 0
                                error = self.entity.move(North)
                                if(error == -1):
                                    error = 0
                                    error = self.entity.move(South)
                    else:
                        error = self.entity.move(East)
                        if(error == -1):
                            error = 0
                            error = self.entity.move(North)
                            if(error == -1):
                                error = 0
                                error = self.entity.move(South)
                                if(error == -1):
                                    error = 0
                                    error = self.entity.move(West)
                nbMove -= 1 
        
    def closerZombi(self):
        i = 0
        j = 0
        longueur = 0
        Direction = None
        for i in range(self.arena.getRows()):
            for j in range(self.arena.getCols()):
                if(self.arena.getCase(i, j).getEntity() != None):
                    if(self.arena.getCase(i, j).getEntity().printType() == "Z"):
                        x = self.entity.getCase().getCoo().getX() - i
                        y = self.entity.getCase().getCoo().getY() - j
                        if(longueur == 0 or abs(x) + abs(y) < longueur):
                            longueur = abs(x) + abs(y)
                            if(x == 0 and y < 0):
                                Direction = East
                            elif(x == 0 and y > 0):
                                Direction = West
                            elif(y == 0 and x < 0):
                                Direction = South
                            elif(y == 0 and x > 0):
                                Direction = North
        if(longueur == 0):
            return False
        elif(longueur <= self.entity.getShotRadius()):
            if(self.entity.getBulletAmount() > 0 and Direction != None):
                self.entity.tir(Direction)
                return True
            else:
                return False
        else:
            return False