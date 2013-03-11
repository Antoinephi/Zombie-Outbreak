'''
Created on 28 fevr. 2013

@author: cacheran
'''

from carte.Direction import *
import time

class BrainZombiStrat():

    def __init__(self, zombi, arena):
        self.zombi = zombi
        self.arena = arena
        
    def nextAction(self):
        entity = self.closerEntity()
        if(entity != None):
            if(entity.printType() == 'Z'):
                print("Un Zombi ! :D")
            elif(entity.printType() == 'B'):
                print("Un Berzerk ! :(")
            elif(entity.printType() == 'H'):
                print("Miam miam !")
        else:
            print("Je suis tout seul ! :(")
            
    def closerEntity(self):
        i = 0
        j = 0
        longueur = 0
        entity = None
        n = (int)(self.zombi.getViewRadius())
        for i in range(n):
            for j in range(n - i):
                if(self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() + j).getEntity() != None):
                    x = self.zombi.getCase().getCoo().getX() - i
                    y = self.zombi.getCase().getCoo().getY() - j
                    if((longueur == 0 or abs(x) + abs(y) < longueur) and abs(x) + abs(y) != 0):
                        longueur = abs(x) + abs(y)
                        entity = self.arena.getCase(i, j).getEntity()
                if(self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() - j).getEntity() != None):
                    x = self.zombi.getCase().getCoo().getX() - i
                    y = self.zombi.getCase().getCoo().getY() - j
                    if((longueur == 0 or abs(x) + abs(y) < longueur) and abs(x) + abs(y) != 0):
                        longueur = abs(x) + abs(y)
                        entity = self.arena.getCase(i, j).getEntity()
                if(self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() + j).getEntity() != None):
                    x = self.zombi.getCase().getCoo().getX() - i
                    y = self.zombi.getCase().getCoo().getY() - j
                    if((longueur == 0 or abs(x) + abs(y) < longueur) and abs(x) + abs(y) != 0):
                        longueur = abs(x) + abs(y)
                        entity = self.arena.getCase(i, j).getEntity()
                if(self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() - j).getEntity() != None):
                    x = self.zombi.getCase().getCoo().getX() - i
                    y = self.zombi.getCase().getCoo().getY() - j
                    if((longueur == 0 or abs(x) + abs(y) < longueur) and abs(x) + abs(y) != 0):
                        longueur = abs(x) + abs(y)
                        entity = self.arena.getCase(i, j).getEntity()
        if(entity != None):
            return entity
        else:
            return None
        
    def plusCourtChemin(self, coo):
        a = time.time()
        mapValue = {}
        for i in range(self.arena.getRows()):
            for j in range(self.arena.getCols()):
                mapValue[self.arena.getCase(i, j).getCoo().toString()] = None
        mapValue[self.zombi.getCase().getCoo().toString()] = 0
        k = 0
        fin = False
        atteint = False
        while(not fin):
            fin = True
            for i in range(self.arena.getRows()):
                for j in range(self.arena.getCols()):
                    if((mapValue[self.arena.getCase(i, j).getCoo().toString()]) == k):
                        if(i > 0):
                            x = i + North.x
                            y = j + North.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                               or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                               and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                                fin = False
                            if(coo.getX() == x and coo.getY() == y):
                                atteint = True
                                break
                        if(j > 0):
                            x = i + West.x
                            y = j + West.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                               or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                               and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                                fin = False
                            if(coo.getX() == x and coo.getY() == y):
                                atteint = True
                                break
                        if(j < self.arena.getCols() - 1):
                            x = i + East.x
                            y = j + East.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                               or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                               and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                                fin = False
                            if(coo.getX() == x and coo.getY() == y):
                                atteint = True
                                break
                        if(i < self.arena.getRows() - 1):
                            x = i + South.x
                            y = j + South.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                               or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                               and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                                fin = False
                            if(coo.getX() == x and coo.getY() == y):
                                atteint = True
                                break
                if(atteint == True):
                    break
            if(atteint == True):
                break
            k += 1
        b = time.time()
        print(b - a)
        for i in range(self.arena.getRows()):
                for j in range(self.arena.getCols()):
                    print(mapValue[self.arena.getCase(i, j).getCoo().toString()]),
                print("")
                
    def plusCourtChemin2(self):
        a = time.time()
        mapValue = {}
        n = (int)(self.zombi.getViewRadius())
        for i in range(n + 1):
            for j in range(n + 1 - i):
                mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() + j).getCoo().toString()] = None
                mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() - j).getCoo().toString()] = None
                mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() + j).getCoo().toString()] = None
                mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() - j).getCoo().toString()] = None
                #mapValue[self.arena.getCase(i, j).getCoo().toString()] = None
        mapValue[self.zombi.getCase().getCoo().toString()] = 0
        k = 0
        fin = False
        while(not fin):
            fin = True
            for i in range(n):
                for j in range(n - i):
                    if(mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() + j).getCoo().toString()] == k):
                        fin = False
                        if(self.zombi.getCase().getCoo().getX() + i > 0):
                            x = self.zombi.getCase().getCoo().getX() + i + North.x
                            y = self.zombi.getCase().getCoo().getY() + j + North.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() + j > 0):
                            x = self.zombi.getCase().getCoo().getX() + i + West.x
                            y = self.zombi.getCase().getCoo().getY() + j + West.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() + j < self.arena.getCols() - 1):
                            x = self.zombi.getCase().getCoo().getX() + i + East.x
                            y = self.zombi.getCase().getCoo().getY() + j + East.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getX() + i < self.arena.getRows() - 1):
                            x = self.zombi.getCase().getCoo().getX() + i + South.x
                            y = self.zombi.getCase().getCoo().getY() + j + South.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                    if(mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() - j).getCoo().toString()] == k):
                        fin = False
                        if(self.zombi.getCase().getCoo().getX() - i > 0):
                            x = self.zombi.getCase().getCoo().getX() - i + North.x
                            y = self.zombi.getCase().getCoo().getY() - j + North.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() - j > 0):
                            x = self.zombi.getCase().getCoo().getX() - i + West.x
                            y = self.zombi.getCase().getCoo().getY() - j + West.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() - j < self.arena.getCols() - 1):
                            x = self.zombi.getCase().getCoo().getX() - i + East.x
                            y = self.zombi.getCase().getCoo().getY() - j + East.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getX() - i < self.arena.getRows() - 1):
                            x = self.zombi.getCase().getCoo().getX() - i + South.x
                            y = self.zombi.getCase().getCoo().getY() - j + South.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                    if(mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() - i, self.zombi.getCase().getCoo().getY() + j).getCoo().toString()] == k):
                        fin = False
                        if(self.zombi.getCase().getCoo().getX() - i > 0):
                            x = self.zombi.getCase().getCoo().getX() - i + North.x
                            y = self.zombi.getCase().getCoo().getY() + j + North.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() + j > 0):
                            x = self.zombi.getCase().getCoo().getX() - i + West.x
                            y = self.zombi.getCase().getCoo().getY() + j + West.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() + j < self.arena.getCols() - 1):
                            x = self.zombi.getCase().getCoo().getX() - i + East.x
                            y = self.zombi.getCase().getCoo().getY() + j + East.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getX() - i < self.arena.getRows() - 1):
                            x = self.zombi.getCase().getCoo().getX() - i + South.x
                            y = self.zombi.getCase().getCoo().getY() + j + South.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                    if(mapValue[self.arena.getCase(self.zombi.getCase().getCoo().getX() + i, self.zombi.getCase().getCoo().getY() - j).getCoo().toString()] == k):
                        fin = False
                        if(self.zombi.getCase().getCoo().getX() + i > 0):
                            x = self.zombi.getCase().getCoo().getX() + i + North.x
                            y = self.zombi.getCase().getCoo().getY() - j + North.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() - j > 0):
                            x = self.zombi.getCase().getCoo().getX() + i + West.x
                            y = self.zombi.getCase().getCoo().getY() - j + West.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getY() - j < self.arena.getCols() - 1):
                            x = self.zombi.getCase().getCoo().getX() + i + East.x
                            y = self.zombi.getCase().getCoo().getY() - j + East.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
                        if(self.zombi.getCase().getCoo().getX() + i < self.arena.getRows() - 1):
                            x = self.zombi.getCase().getCoo().getX() + i + South.x
                            y = self.zombi.getCase().getCoo().getY() - j + South.y
                            if((mapValue[self.arena.getCase(x, y).getCoo().toString()] > k+1 
                                or mapValue[self.arena.getCase(x, y).getCoo().toString()] == None)
                                and self.arena.getCase(x, y).getPietinable()):
                                mapValue[self.arena.getCase(x, y).getCoo().toString()] = k+1
            k = k + 1 
        b = time.time()
        print(b - a)
        #for i in range(self.arena.getRows()):
            #for j in range(self.arena.getCols()):
                #if(mapValue[self.arena.getCase(i, j).getCoo().toString()] == None):
                    #print("~"),
                #else:
                    #print(mapValue[self.arena.getCase(i, j).getCoo().toString()]),
            #print("")