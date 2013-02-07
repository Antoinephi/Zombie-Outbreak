'''
Created on 4 fevr. 2013

@author: Nicolas
'''

class Direction():
    pass


class Up(Direction):
    x = -1
    y = 0
    
class Down(Direction):    
    x = 1
    y = 0
    
class Left(Direction):
    x = 0
    y = -1
    
class Right(Direction):
    x = 0
    y = 1 
        