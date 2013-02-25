'''
Created on 24 fevr. 2013

@author: Nicolas
'''

from carte.Direction import *
import random

class BrainBerzerk():
    
    def __init__(self, berzerk, arena):
        self.berzerk = berzerk
        self.arena = arena

    def nextAction(self):
        if(self.berzerk.isAlive()):
            nbMove = self.berzerk.MOVE_LEN 
            while(nbMove > 0):
                if(self.berzerk.getBerzerkDelay() > 0):
                    error = 0
                    r = random.randint(1,4)
                    if(r == 1):
                        error = self.berzerk.move(North)
                        if(error == -1):
                            error = 0
                            error = self.berzerk.move(South)
                            if(error == -1):
                                error = 0
                                error = self.berzerk.move(West)
                                if(error == -1):
                                    error = 0
                                    error = self.berzerk.move(East)
                    elif(r == 2):
                        error = self.berzerk.move(South)
                        if(error == -1):
                            error = 0
                            error = self.berzerk.move(West)
                            if(error == -1):
                                error = 0
                                error = self.berzerk.move(East)
                                if(error == -1):
                                    error = 0
                                    error = self.berzerk.move(North)
                    elif(r == 3):
                        error = self.berzerk.move(West)
                        if(error == -1):
                            error = 0
                            error = self.berzerk.move(East)
                            if(error == -1):
                                error = 0
                                error = self.berzerk.move(North)
                                if(error == -1):
                                    error = 0
                                    error = self.berzerk.move(South)
                    else:
                        error = self.berzerk.move(East)
                        if(error == -1):
                            error = 0
                            error = self.berzerk.move(North)
                            if(error == -1):
                                error = 0
                                error = self.berzerk.move(South)
                                if(error == -1):
                                    error = 0
                                    error = self.berzerk.move(West)
                else:
                    self.berzerk.explose()
                nbMove -= 1 