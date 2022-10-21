import pygame
pygame.init()
import time
clock=pygame.time.Clock()
class variables:
    def __init__(self):
        self.run=True
        self.start=True
        self.ball_pic=pygame.image.load('Ball.png')
        self.block_pic=pygame.image.load('Block.png')
        self.bar=pygame.image.load('bar.png')
        self.width_ball=64
        self.height_ball=64
        self.width_bar=300
        self.height_bar=59
        self.width_block=152
        self.height_block=117
        self.screen_Width=1200
        self.screen_Height=800
        self.gameover=False
        self.space_display=False
        
        self.M_display=False
        self.xb=1200/2-300/2
        self.acc_bar=6
        self.y_bar=self.screen_Height-self.height_bar-10
        self.won=False
        self.double=False
        self.d2=False
        self.fin=False
        self.l1=False
        self.l2=False
        self.l3=False
        self.lTextSurf=""
        self.level3=[[68,68+self.width_block,68+2*self.width_block,68+3*self.width_block,68+4*self.width_block,68+5*self.width_block,68+6*self.width_block],[68+self.width_block,68+2*self.width_block,68+3*self.width_block,68+4*self.width_block,68+5*self.width_block],[68+2*self.width_block,68+3*self.width_block,68+4*self.width_block],[68+3*self.width_block]]
        self.level2=[[[111,111],[111+self.width_block,111],[self.screen_Width-111-self.width_block,111],[self.screen_Width-111-2*self.width_block,111]],[[111,111+self.height_block],[self.screen_Width-111-self.width_block,111+self.height_block]],[[111,111+2*self.height_block],[111+self.width_block,111+2*self.height_block],[111+2*self.width_block,111+2*self.height_block],[self.screen_Width-111-self.width_block,111+2*self.height_block],[self.screen_Width-111-2*self.width_block,111+2*self.height_block],[self.screen_Width-111-3*self.width_block,111+2*self.height_block]]]
        self.level1=[[50,275],[300,275],[550,275],[800,275],[1050,275],[50,100],[300,100],[550,100],[800,100],[1050,100]]
        self.start_pic=pygame.image.load('gf1.jpg')
        self.level_pic=pygame.image.load('gf2.jpg')
        self.quit_pic=pygame.image.load('gf3.jpg')
        self.levels_pic=[pygame.image.load('1bg.jpg'),pygame.image.load('2bg.jpg'),pygame.image.load('3bg.jpg')]
    def display(self):
        win.blit(self.bar,(self.xb,self.y_bar))
        pygame.display.update()
        win.blit(self.bg,(0,0))
        win.blit(self.ball_pic,(Ball.x,Ball.y))
        if self.M_display:
            win.blit(self.TextSurf,self.TextRect)

clock = pygame.time.Clock()
class ball :
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.jx=-7
        self.jy=-7
    def position(self):
        
        if self.x<=0 and not(self.y==0 ):
            self.jx*=-1
        if self.y<=0 and not(self.x==0 ):
            self.jy*=-1
        if self.x>=vari.screen_Width-vari.width_ball and not (self.y==0 ):
            self.jx*=-1
        if self.y>=vari.screen_Height-vari.height_ball:
            vari.run=False
            vari.gameover=True
        if(self.x+vari.width_ball>=vari.xb and self.x<=vari.xb+vari.width_bar) and (self.y+vari.height_ball>=vari.y_bar) and vari.double:
            self.jy*=-1
            vari.d2=True
        if  vari.d2:
            vari.double=False
            self.y-=5
        else:
            vari.double=True
        self.x+=self.jx
        self.y+=self.jy
        vari.d2=False
        
        
        
class level_1:
    def __init__(self,pos):
        self.pos=pos
        vari.bg=pygame.image.load('bg.jpg')
    def block_1(self):
        if Ball.y<=275+vari.height_block and Ball.y+vari.height_ball>=275:
            for blockx in self.pos:
                if Ball.x+vari.width_ball>=blockx[0] and Ball.x<=blockx[0]+vari.width_block and not(blockx[1]==100):
                    if Ball.x+hg>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                        Ball.jy*=-1
                    else:
                        Ball.jx*=-1
                    self.pos.remove(blockx)
        if Ball.y<=100+vari.height_block and Ball.y+vari.height_ball>=100:
            for blockx in self.pos:
                if Ball.x+vari.width_ball>=blockx[0] and Ball.x<=blockx[0]+vari.width_block and not(blockx[1]==275):
                    if Ball.x+hg>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                        Ball.jy*=-1
                    else:
                        Ball.jx*=-1
                    self.pos.remove(blockx)

        
        for x in self.pos :
            win.blit(vari.block_pic,(x[0],x[1]))

hg=40
class level_2:
    def __init__(self,pos):
        self.pos=pos
        vari.bg=pygame.image.load('bg.jpg')
    def block_1(self):
        if Ball.y+vari.height_ball>=115 and Ball.y<=115+vari.height_block:
            for blockx in self.pos[0]:
                if Ball.x+vari.width_ball>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                     if Ball.x+hg>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[0].remove(blockx)
                     
        if Ball.y+vari.height_ball>=115+vari.height_block and Ball.y<=115+2*vari.height_block:
            for blockx in self.pos[1]:
                 if Ball.x+vari.width_ball>=blockx[0] and Ball.x<=blockx[0]+vari.width_block:
                     if Ball.x+hg>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[1].remove(blockx)
        if Ball.y+vari.width_ball>=115+2*vari.height_block and Ball.y<=115+3*vari.height_block:
             for blockx in self.pos[2]:
                 if Ball.x+vari.width_ball>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                     if Ball.x+hg>=blockx[0] and Ball.x<=blockx[0]+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[2].remove(blockx)


        
        for x in self.pos :
            for y in x:
                win.blit(vari.block_pic,(y[0],y[1]))
        

vari=variables()

class level_3:
    def __init__(self,pos):
        self.pos=pos
        vari.bg=pygame.image.load('bg.jpg')
    def block_1(self):
        if Ball.y+vari.height_ball>=115 and Ball.y<=115+vari.height_block:
            for blockx in self.pos[0]:
                if Ball.x+vari.width_ball>=blockx and Ball.x<=blockx+vari.width_block :
                     if Ball.x+hg>=blockx and Ball.x<=blockx+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[0].remove(blockx)
                     
        if Ball.y+vari.height_ball>=115+vari.height_block and Ball.y<=115+2*vari.height_block:
            for blockx in self.pos[1]:
                 if Ball.x+vari.width_ball>=blockx and Ball.x<=blockx+vari.width_block:
                     if Ball.x+hg>=blockx and Ball.x<=blockx+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[1].remove(blockx)
        if Ball.y+vari.width_ball>=115+2*vari.height_block and Ball.y<=115+3*vari.height_block:
             for blockx in self.pos[2]:
                 if Ball.x+vari.width_ball>=blockx and Ball.x<=blockx+vari.width_block :
                     if Ball.x+hg>=blockx and Ball.x<=blockx+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[2].remove(blockx)
        if Ball.y+vari.width_ball>=115+3*vari.height_block and Ball.y<=115+4*vari.height_block:
             for blockx in self.pos[3]:
                 if Ball.x+vari.width_ball>=blockx and Ball.x<=blockx+vari.width_block :
                     if Ball.x+hg>=blockx and Ball.x<=blockx+vari.width_block :
                        Ball.jy*=-1
                     else:
                        Ball.jx*=-1
                     self.pos[3].remove(blockx)
        if self.pos==[[],[],[],[]]:
            vari.fin=True
        self.gb=111
        self.lis=self.pos
        for dsd in range(4):
            for x in self.lis[dsd]:                    
                win.blit(vari.block_pic,(x,self.gb))
                    
            self.gb+=vari.height_block
            self.lis=self.pos


                     
win=pygame.display.set_mode((vari.screen_Width,vari.screen_Height))
def text_object(text, font):
    textSurface=font.render(text , True , (255,255,255))
    return textSurface , textSurface.get_rect()

def message_display(text,size_1):
    largeText=pygame.font.Font('freesansbold.ttf',85)
    TextSurf , TextRect = text_object(text , largeText)
    TextRect.center=(size_1)
    vari.TextSurf=TextSurf
    vari.TextRect=TextRect
    vari.M_display=True
def text_object1(text, font):
    textSurface=font.render(text , True , (255,255,255))
    return textSurface , textSurface.get_rect()

def message_display1(text,size):
    largeText=pygame.font.Font('freesansbold.ttf',85)
    TextSurf , TextRect = text_object1(text , largeText)
    TextRect.center=(size)
    win.blit(TextSurf,TextRect) 





Ball=ball(vari.xb+vari.width_bar/2-vari.width_ball/2,vari.y_bar-vari.height_bar-5.7)

 
start_screen1=True
levelno=1


gj=[vari.start_pic,vari.level_pic,vari.quit_pic]
c=0

while start_screen1:
    win.blit(gj[c],(0,0))
    pygame.display.update()
    keys=pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and not c==2: 
       c+=1
    if keys[pygame.K_UP] and not c==0:
       c-=1
    if keys[pygame.K_SPACE]:
        if gj==[vari.start_pic,vari.level_pic,vari.quit_pic]:
            if c==0:
               start_screen1=False
               Block=level_1(vari.level1)
            elif c==1:
                gj=vari.levels_pic
            elif c==2:
               vari.run=False
               vari.start=False
               vari.gameover=False
               start_screen1=False
        else :
            if c==0:
                Block=level_1(vari.level1)
                levelno=1
            elif c==1:
                Block=level_2(vari.level2)
                levelno=2
            else:
                Block=level_3(vari.level3)
                levelno=3
            start_screen1=False
    for events in pygame.event.get():
       if events.type==pygame.QUIT:
           vari.run=False
           vari.start=False
           vari.gameover=False
           start_screen1=False
    time.sleep(0.085)
        





        

def start_():
    while vari.start:
        message_display1(("level "+str(levelno)),(vari.screen_Width/2,vari.screen_Height/2-50))
        message_display(("Press Space to Start "),(vari.screen_Width/2,vari.screen_Height/2+50))
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            vari.start=False
            vari.M_display=False
        vari.display()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] and vari.xb<vari.screen_Width-vari.width_bar:
            vari.xb+=vari.acc_bar
            Ball.x+=vari.acc_bar
        if keys[pygame.K_LEFT] and vari.xb>0:
            vari.xb-=vari.acc_bar
            Ball.x-=vari.acc_bar
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                vari.run=False
                vari.start=False
                vari.gameover=False
       
  
while vari.run:
   
    start_()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            vari.run=False
            vari.gameover=False
    message_display1(("level "+str(levelno)),(vari.screen_Width-150,40))
    keys=pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and vari.xb<vari.screen_Width-vari.width_bar:
        vari.xb+=vari.acc_bar
    if keys[pygame.K_LEFT] and vari.xb>0:
        vari.xb-=vari.acc_bar
    if vari.run:
        Block.block_1()
        vari.display()
        Ball.position()
    if Block.pos==[]:
        Block=level_2(vari.level2)
        levelno+=1
        vari.start=True
        Ball.x,Ball.y=vari.xb+vari.width_bar/2-vari.width_ball/2,vari.y_bar-vari.height_bar-5.7
    if Block.pos==[[],[],[]]:
        Block=level_3(vari.level3)
        levelno+=1
        vari.start=True
        Ball.x,Ball.y=vari.xb+vari.width_bar/2-vari.width_ball/2,vari.y_bar-vari.height_bar-5.7
    if vari.fin:
        vari.run=False
        vari.gameover=False
        vari.won=True
    clock.tick(120)






while vari.gameover:
    message_display(("NOOOO!You lost the game "),(vari.screen_Width/2,vari.screen_Height/2))
    vari.display()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            vari.gameover=False
            vari.won=False
while vari.won:
    message_display(("YEE!!You Won"),(vari.screen_Width/2,vari.screen_Height/2))
    vari.display()
    for events in pygame.event.get():
        if events.type==pygame.QUIT:
            vari.won=False
            

pygame.quit()






            
