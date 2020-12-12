# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 11:34:35 2020

@author: Devon
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 10:24:11 2020

@author: Devon
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

import time

x,y,z = mc.player.getTilePos()

for i in range(10):
    r = random.randint(1, 6)
    a = random.randint(0, 15)
    
    
    if r == 2:
        mc.setBlocks(x,y,z,x+10,y,z,95,a)
        x = x-4
        
    elif r == 1:
        mc.setBlocks(x,y,z,x,y,z-10,95,a)   
        x = x+4
        
    elif r == 3:
        mc.setBlocks(x,y,z,x-10,y,z,95,a)
        z = z-4
        
    elif r == 4:
        mc.setBlocks(x,y,z,x,y,z+10,95,a)
        z = z+4
    
    elif r == 5:
        mc.setBlocks(x,y,z,x,y+10,z,95,a)
        z = z+4
        
    elif r == 6:
        mc.setBlocks(x,y,z,x,y-10,z,95,a)
        z = z+4