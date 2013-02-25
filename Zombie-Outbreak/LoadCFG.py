'''
Created on 14 fevr. 2013

@author: Antoine
'''

class LoadCFG():

    def __init__(self):   
        self.source = open("cfg.txt", "r")  
        self.lecture = self.source.readlines()
        self.nbLignes = len(self.lecture)
        self.source.close()       
        self.tableau= [None] * self.nbLignes      
        self.source = open("cfg.txt", "r")    
        for i in range (self.nbLignes):
            self.tableau[i] = self.source.readline().split()        
        self.source.close()
    
    def printCFG(self):
        for i in range (self.nbLignes):
            print(self.tableau[i])
            
    def printLineNumber(self):
        print self.nbLignes
        
    def getData(self,line):
        return self.tableau[line][1]