import pygame
sw=1200
sh=800
jx=5
jy=5
pygame.init()
win=pygame.display.set_mode((sw,sh))
block=pygame.image.load('Block.png')
bar=pygame.image.load('bar.png')
bal=pygame.image.load('Ball.png')
bg=pygame.image.load('bg.jpg')
xb=0
x=xb+150
y=sh-69-64
gameover=False
double=True
pos=[[50,275],[300,275],[550,275],[800,275],[1050,275],[50,100],[300,100],[550,100],[800,100],[1050,100]]
def text_object(text, font):
    textSurface=font.render(text , True , (0,0,0))
    return textSurface , textSurface.get_rect()

def block1():
     for x in pos :
        win.blit(block,(x[0],x[1]))
     
def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',85)
    TextSurf , TextRect = text_object(text , largeText)
    TextRect.center=(sw/2,sh/2)
    win.blit(TextSurf,TextRect)
 
    
def Display():
    win.blit(bar,(xb,sh-69))
    pygame.display.update()
    win.blit(bg,(0,0))
   
            
    win.blit(bal,(x,y))
def ball():
    global x,y,jx,jy,run,gameover,pos
    if x<=0 and y<=0:
        jx*=-1
        jy*=-1
    if x>=sw-64 and y<=0:
        jx*=-1
        jy*=-1
    if y<=0:
        jy=-1*jy
    if x<=0:
        jx*=-1
    if y>=sh-64:
        run=False
        gameover=True
    if y+64 >=sh-69  and x+64>=xb and x+64<=xb+300 and  jy==-5 :
        jy*=-1
    if x+64>=sw:
        jx*=-1
    if y<=275+117 and y>=275:
        for blockx in pos:
            if x+64>=blockx[0] and x<=blockx[0]+117 and not(blockx[1]==100):
                if  (y>=275 and y<=280) or (y>=275+117 and y<=280+117):
                    jy*=-1
                else:
                    jx*=-1
                pos.remove(blockx)
    if y <=217 and y>=100:
        for blockx in pos:
            if x+64>=blockx[0] and x<=blockx[0]+117and not(blockx[1]==275):
                if  (y>=100 and y<=105) or (y>=100+117 and y<=105+117):
                    jy*=-1
                else:
                    jx*=-1
                pos.remove(blockx)
    x-=jx
    y-=jy
  
run=True
start=True
while start:
    message_display("Please enter Space to Start")
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        start=False
    Display()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False
            start=False
            gameover=False
    
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run=False
            gameover=False
            
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and xb<sw-300:
        xb+=5
    if keys[pygame.K_LEFT] and xb>0:
        xb-=5
    ball()
    Display()
    if pos==[]:
        run=False
        won=True
    
    block1()

if gameover or won:
    th=True
    while th:
        if gameover:
            message_display("You lost the game")
        else:
            message_display("YAAH!You won the game")
        Display()
        for events in pygame.event.get():

            if events.type==pygame.QUIT:
                th=False



pygame.quit()
