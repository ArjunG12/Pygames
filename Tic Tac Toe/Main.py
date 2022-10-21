import collections

import itertools
import pygame
pygame.init()
pygame.display.set_caption("Tic tac toe")

screenWidth=462
screenHeight=462

win =pygame.display.set_mode((screenWidth,screenHeight))

abc=False
horiWinner=[]
verWinner=[]
screenUp=462/3
screenLeft=462/3
ab=[]
x=0
y=0
width=screenLeft
height=screenUp
images=[]
j=0
circle=pygame.image.load('Circle.png')
cross=pygame.image.load('cross.png')
R1= pygame.image.load('Tic.jpg')
R2=pygame.image.load('Tic2.jpg')
oY=[]
oX=[]
xX=[]
xY=[]
def Display_all():
    win.blit(R1 ,(0,0))
    win.blit(R2,(x,y),(0,0,width,height))
    global j,s,gb,ab,draw ,k,horiWinner ,verWinner
    s=0
    
    if draw and not [x,y] in ab:
        j=x
        k=y
        ab.append([j,k])
        count=next(cou)
        images.append(count)
        if count==circle:
            oY.append(y)
            oX.append(x)
        elif count == cross:
            xX.append(x)
            xY.append(y)
        draw=False
    if gb:
        for u in images:
            
            win.blit(u,(ab[s]),(0,0,width,height))            
            s+=1
            
        
    pygame.display.update()

diagnol=0
draw=False
diag=False
def winner(OX,OY,CX,CY):
    global run
    for x in [OX,OY,CX,CY]:
        if len(x) >=3:
            a=collections.Counter(x)
            s=0
            kjf=0
            while s<=3:
                if kjf in a:
                    if a[kjf]>=3:
                        run =False
                        message_display("Winner")
                        abc=True
                s+=1
                kjf+=154
            diagnol=0
            oy=set(OY)
            ox=set(OX)
            cx=set(CX)
            cy=set(CY)
            for x1 in cx:
                for y1 in cy:
                    if y1==x1:
                        diagnol +=1
            if diagnol==3:
                run =False
                message_display("Winner")

            else:
                diagnol=0
                for  x2 in ox:
                    for y2 in oy:
                        if y2==x2:
                            diagnol +=1
                if diagnol==3:
                    run =False
                    message_display("Winner")        
                    
    
def text_object(text, font):
    textSurface=font.render(text , True , (0,0,0))
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    TextSurf , TextRect = text_object(text , largeText)
    TextRect.center=(screenWidth/2,screenHeight/2)
    win.blit(TextSurf,TextRect)
    
    pygame.display.update()
    


gb=False
count=0
run =True
draw=False
cou=itertools.cycle([cross,circle])

while run:
    
    pygame.time.delay(125)
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run =False
    
    keys=pygame.key.get_pressed()
    

    if keys[pygame.K_LEFT] and x>= screenLeft:
        x =x- screenLeft
    elif keys[pygame.K_RIGHT] and x < screenWidth-screenLeft:
        x =x+ screenLeft
    elif keys[pygame.K_UP]  and y>=screenUp:
        y =y- screenUp
    elif keys[pygame.K_DOWN] and y < screenHeight-screenUp:
         y = y+ screenUp
    if keys[pygame.K_SPACE] and draw==False:
        draw=True
        
        gb=True




    Display_all()

    winner(oX,oY,xX,xY)




pygame.quit()
