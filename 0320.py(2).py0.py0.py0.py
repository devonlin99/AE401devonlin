
import pygame

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



pygame.init()

size = (700, 500)
screen =pygame.display.set_mode(size)
pygame.display.set_caption("粉圓2")

done = False
clock =pygame.time.Clock()
x = random.randrange(0, 400)
y = random.randrange(0, 400)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done==True
    
    screen.fill(white)
 

    pygame.draw.circle(screen,red,(x,y),4,4)
    
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()