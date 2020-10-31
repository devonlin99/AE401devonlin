from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()


try:
    blocktype = int(input('請輸入方塊id'))
    mc.setBlock(x,y,z, blocktype)
    
except:
    print('只能輸入數字!!!!!!')
    
    

#-----------------------------------------
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()


a = int(input('enter x'))

b = int(input('enter y'))

c = int(input('enter z'))

mc.setBlocks(x ,y ,z, x+a, y+b, z+c, 86)

mc.setBlocks(x+1,y+1,z+1, x+a-1, y+b-1, z+c-1, 0)
