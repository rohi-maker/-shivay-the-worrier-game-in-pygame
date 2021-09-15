import pygame
import random
import sys
def welcome():
    value=True
    im=pygame.image.load("player.png")
    im=pygame.transform.scale(im,(160,160))
    TEXT=pygame.font.SysFont("TTF",40)
    text=TEXT.render("SHIVAY THE WORRIER",True,(255,0,0))
    enter=pygame.font.Font(None,40)
    enter1=enter.render("PRESS ENTER TO PLAY",True,(255,0,0))
    global gameWindow
    global background
    while value:
        gameWindow.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    value=False
        gameWindow.blit(background,(0,0))
        gameWindow.blit(im,(250,160))
        gameWindow.blit(text,(100,90))
        gameWindow.blit(enter1,(130,400))
        pygame.display.update()
    return

my_villens=[]
WIDTH=600
HEIGHT=500
FPS=30
val=0
score=0
pygame.font.init()
my_score=pygame.font.Font(None,10)
font_obj=pygame.font.Font(None,25)
fps=pygame.time.Clock()
# game sounds
pygame.mixer.init()
throw=pygame.mixer.Sound("wing.wav")
upnow=pygame.mixer.Sound("jump.wav")
hit=pygame.mixer.Sound("hit.wav")
#-----
# villen specific variables of game
villen1=pygame.image.load("villen.png")
villen1=pygame.transform.scale(villen1,(96,96))
villen2=pygame.image.load("villen2.png")
villen2=pygame.transform.scale(villen2,(96,96))
villen3=pygame.image.load("chakra.png")
villenX=WIDTH+10
villenY=296
villen_velocity=-10 
die=pygame.mixer.Sound("die.wav")
#-----list of villens
my_villens.append(villen1)
my_villens.append(villen2)
my_villens.append(villen3)
v=random.choice(my_villens)
# player specific variables of game
playerX=250
playerY=296
backsong=pygame.mixer.music.load("Kalimba.mp3")
pygame.mixer.music.set_volume(30)
weponX=250
weponY=296
wepon_x_velocity=0
wepon_y_velocity=0
y_velocity=2
x_velocity=0
var=296
gameWindow=pygame.display.set_mode((WIDTH,HEIGHT))
background=pygame.image.load("background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
ground=pygame.image.load("base.png")
ground=pygame.transform.scale(ground,(WIDTH,112))
pygame.display.set_caption("SHIVAY SHOOTER")
icon=pygame.image.load("player.png")
pygame.display.set_icon(icon)
groundY=388
player=pygame.image.load("player.png")
player=pygame.transform.scale(player,(96,96))
wepon=pygame.image.load("wepon.png")
wepon=pygame.transform.scale(wepon,(64,64))
game_exit=False
jump=False
attack=False
state="active"
welcome()
pygame.mixer.music.play()
while not game_exit:
    
    y_velocity=7
    if state is "active":
        wepon_y_velocity=7
    else:
        wepon_y_velocity=0
    gameWindow.fill((255,255,255)) 
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_exit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                jump=True
                upnow.play()
            if event.key==pygame.K_LEFT:
                x_velocity=-10
                if state=="active":
                    wepon_x_velocity=-10
            if event.key==pygame.K_RIGHT:
                x_velocity=10
                if state=="active":
                    wepon_x_velocity=10
            if event.key==pygame.K_SPACE:
                attack=True
                state="notactive"
                throw.play()
        if event.type==pygame.KEYUP and (event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT):
            x_velocity=0
            if state=="active":
                wepon_x_velocity=0
            
    if jump:
        y_velocity=-170
        x_velocity=2
        if state is "active":
            wepon_y_velocity=-170
            wepon_x_velocity=2
        jump=False
    if attack:
        wepon_x_velocity+=10
        weponY=296
        attack=False
    if weponX>=605:
        state="active"
        px=playerX
        weponX=px
        weponY=296
        wepon_x_velocity=0
        gameWindow.blit(wepon,(weponX,weponY))
    playerX+=x_velocity
    weponX+=wepon_x_velocity
    playerY+=y_velocity
    weponY+=wepon_y_velocity
    villenX+=villen_velocity
    if playerY>=296:
         px=playerX
         playerX=px
         playerY=296
         wx=weponX
         weponX=wx
         weponY=296
         gameWindow.blit(wepon,(wx,weponY))
         gameWindow.blit(player,(playerX,playerY))
    # if playerX<=0:
    #     playerX=0
    # elif playerX>=WIDTH:
    #     playerX=WIDTH     
    gameWindow.blit(background,(0,0))
    myfont=font_obj.render("SCORE="+str(score),True,(0,255,0))
    gameWindow.blit(myfont,(10,10))
    gameWindow.blit(ground,(0,groundY))
    gameWindow.blit(wepon,(weponX,weponY))
    gameWindow.blit(player,(playerX,playerY))
    gameWindow.blit(v,(villenX,villenY))
    if villenX<=20:
        villenX=random.randint(450,600)
        v=random.choice(my_villens)
        villenX=random.randint(300,600)
        gameWindow.blit(v,(villenX,villenY))
    if abs(playerX-villenX)<15 and abs(playerY-villenY)<15:
        die.play()
        game_exit=True
    if abs(villenX-weponX)<8 and abs(villenY-weponY)<8:
        
        
        state="active"
        px=playerX
        weponX=px
        weponY=296
        wepon_x_velocity=0
        gameWindow.blit(wepon,(weponX,weponY))
        villenX=random.randint(450,600)
        v=random.choice(my_villens)
        if v==my_villens[2]:
            for i in range(0,5): 
                gameWindow.blit(v,(villenX+val,villenY))
                val=val+4 
        gameWindow.blit(v,(villenX,villenY))
        score+=10
        hit.play()
    pygame.display.update()
    fps.tick(FPS)
pygame.quit()
quit()