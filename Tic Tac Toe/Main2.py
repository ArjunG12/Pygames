import itertools
import pygame
pygame.init()
pygame.display.set_caption("Tic tac toe")

screenWidth=462
screenHeight=462

win =pygame.display.set_mode((screenWidth,screenHeight))

x = 0
y = 0
width = screenWidth / 3
height = screenHeight/3
horizontal=width
vertical=height

circle=pygame.image.load('Circle.png')
cross=pygame.image.load('cross.png')
R1=pygame.image.load('Tic.jpg')
R2=pygame.image.load('Tic2.jpg')


def Display_all():
    win.blit(R1,(0,0))
    win.blit(R2,(x,y),(0,0,width,height))

    pygame.display.update



draw=False
run=True
#Main loop
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False

    keys =pygame.key.get_pressed()

    if not draw:
        if keys[pygame.K_LEFT] and x>horizontal:
             x-=horizontal
        elif keys[pygame.K_RIGHT] and x <screenWidth-horizontal:
            x+=horizontal
        elif keys[pygame.K_UP] and y>vertical:
            y-=vertical
    elif keys[pygame.K_DOWN] and y < screenHeight-vertical:
        y+=vertical
    
    
    Display_all()
    




pygame.quit()
































    


































