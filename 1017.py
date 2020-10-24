# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 10:21:52 2020

@author: Devon
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setBlock(x,y,z,9)
mc.setBlock(x,y+1,z,15)
mc.setBlock(x,y+2,z,15)
mc.setBlock(x,y+3,z,12)
mc.setBlock(x,y+4,z,13)
mc.setBlock(x,y+5,z,11)
mc.setBlock(x,y+6,z,12)
mc.setBlock(x,y+7,z,90)
mc.setBlock(x,y+8,z,15)
mc.setBlock(x,y+9,z,15)
mc.setBlock(x,y+10,z,15)
mc.setBlock(x,y+11,z,15)
mc.setBlock(x,y+12,z,90)
mc.setBlock(x,y+13,z,90)
mc.setBlock(x,y+14,z,15)


x,y,z = mc.player.getTilePos()
mc.setBlock(x+1,y,z,20)
mc.setBlock(x-1,y,z,20)
mc.setBlock(x+1,y,z+1,20)
mc.setBlock(x-1,y,z-1,20)
mc.setBlock(x,y,z-1,20)
mc.setBlock(x,y,z+1,20)
mc.setBlock(x-1,y,z+1,20)
mc.setBlock(x+1,y,z-1,20)


x,y,z = mc.player.getTilePos()
mc.setBlocks(x+1,y+100,z+1,x+1,y-100,z+1,20)
