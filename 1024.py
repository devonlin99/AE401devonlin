
"""
Created on Sat Oct 24 10:30:20 2020

@author: Devon
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

while True:

    x,y,z = mc.player.getTilePos()

    a=mc.getBlock(x,y-1,z-1)
    b=mc.getBlock(x,y-1,z+1)
    c=mc.getBlock(x-1,y-1,z)
    d=mc.getBlock(x+1,y-1,z)

    if a==0 or a == 0 or b == 0 or b == 0 or c == 0 or c ==0:
        mc.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,165)
       

        
while True:
    x,y,z = mc.player.getTilePos()

    
    mc.setBlock(x,y,z,38)
    time.sleep(0.2)


x,y,z = mc.player.getTilePos()
a=0
while a < 8:
    
    mc.setBlocks(x+20,y-1,z,x-20,y-10,z,19)
    z=z+5
    a=a+1
    
    
    
while True:
    x,y,z = mc.player.getTilePos()
    mc.setBlock(x,y,z,8)
    mc.setBlock(x,y-1,z,19)
    time.sleep(1)   
    