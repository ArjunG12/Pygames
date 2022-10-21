import pygame
import random
pygame.init()
ran=random.randint(-980+250,0)
sH=980
sW=878
wd=sW-160
win =pygame.display.set_mode((sW,sH))
upper=pygame.image.load('upper.png')
lower=pygame.image.load('lower.png')
bird=[pygame.image.load('Bird.png'),pygame.image.load('bird2.png'),pygame.image.load('bird3.png'),pygame.image.load('bird5.png'),pygame.image.load('bird6.png'),pygame.image.load('bird7.png')]
bg=pygame.image.load('Background.jpg')
gameOver=pygame.image.load('Gameover.png')
jum=False
x=250
y=490
jC=10
J=jC/3
xw=sW-200
upper2=upper
lower2=lower
wd2=sH+300
ran2=random.randint(-980+250,-50)
r=0
jg=0
def displa_y():
    global score
    global wd,ran,wd2,ran2
    win.blit(bg , (0,0))
    win.blit(bird[r],(x,y))
    win.blit(upper,(wd,ran))
    win.blit(lower,(wd,ran+1000))
    win.blit(upper2,(wd2,ran2))
    win.blit(lower,(wd2,ran2+1000))
    if wd==-168:
        wd=sW
        ran=random.randint(-980+250,-50)
        score+=1
    wd-=2
    if wd2==-168:
        wd2=sW
        ran2=random.randint(-980+250,-50)
        score+=1
    wd2-=2
    pygame.display.update()
gameover=False
def jump():
    global jC,y,x,r,jg
    if jC>=0:
        y-=(jC**2)/6
    else:
        y+=(jC**2)/6
    jC-=1
    if jg>=J and r<5:
        r+=1
        jg=0
    else:
        jg+=1
    if y >=sH-37:
        jum=False
        y=sH-37
    if y<=37:
        y=37
        jC=-1
score=0
def text_object(text, font):
    textSurface=font.render(text , True , (0,0,0))
    return textSurface , textSurface.get_rect()


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',100)
    TextSurf , TextRect = text_object(text , largeText)
    TextRect.center=(sW/2,sH/2)
    win.blit(TextSurf,TextRect)
    
    pygame.display.update()
def poles():
    global run,gameover
    if x>=(wd-37) and x<=(wd+168)and ((y>=ran and y<=ran+700) or (y>=ran+1020 and y<=ran+1000+710)):
        gameover=True
        run =False
    if x>=(wd2-37) and x<=(wd2+168)and ((y>=ran and y<=ran2+700) or (y>=ran2+1020 and y<=ran2+1000+710)):
        gameover=True
        run =False
    
run = True
while run:
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            run =False
    displa_y()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jum=True
        jC=10
        jg=0
        r=0
    if  jum:
        jump()
        
    poles()

while gameover:
    win.blit(bg ,(0,0))
    win.blit(gameOver,(100,100))
    message_display('Score= '+str(score))
    pygame.display.update()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            gameover=False
pygame.quit()
