# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 10:19:19 2020

@author: Devon
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()



while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        print('block ID:'+ str(block))
        
#------------------------------------------------------------------------------
        
from mcpi.minecraft import Minecraft
mc = Minecraft.create()



while True:
    hits = mc.events.pollBlockHits()
    
    if len(hits) > 0:
        hit = hits[0]
        
        x,y,z = hit.pos.x, hit.pos.y, hit.pos.z
        block = mc.getBlock(x,y,z)
        if block == 1:
            mc.setBlock(x,y,z,0)
            
#----------------------------------------------------------------------------------------------------------------------------            #-----------------------------------------------------------------------------
            
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


x,y,z = mc.player.getTilePos()
mc.setSign(x+2,y,z+2,63,0,'甚麼時候可以下課','','','')





#------------------------------------------------------------------------------
from mcpi.minecraft import Minecraft

i = 0
while i < 20:
    pos = mc.player.getPos()
    i = i + 1
    x = pos.x + random.uniform(-20,20) 
    y = pos.y + random.uniform(3,0)
    z = pos.z + random.uniform(-20,20)
    
    mc.spawnEntity(x,y,z,12)
    time.sleep(0.2)













