'''
Created on 28 janv. 2013

@author: jolya
'''

from player.Entity import Entity

class Zombi(Entity):
    
    def __init__(self,s,policier):
        self.ATTACK_RADIUS = (1)
        super(Zombi,self).__init__(s)
        if (policier == True):
            super(Zombi,self).setBulletAmount(9)