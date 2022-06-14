#Ruth Gebru
#6/9/22
#we are learning pygame basic functions
#creating screens, clrs, shape

from difflib import SequenceMatcher
import os
from re import U
from turtle import left
import pygame, time
pygame.init()#initialize the pygame pakage
os.system('cls')
WIDTH=700 #like constant 
HEIGHT=700
colors= {"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255,),"limegreen":(153,255,512)}
circleClr=colors.get("limegreen")
#create display window with any name you like
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('My First Game') #hange the title of my window
pygame.time.delay(2000)
redClr=(255,0,0)
screen.fill(redClr)
pygame.display.update()
pygame.time.delay(2000)
greenClr=(0,255,0)
screen.fill(greenClr)
pygame.display.update()
pygame.time.delay(2000)
hb=50
wb=50
xb=100
yb=300
square=(xb,yb,wb,hb)#create the ject tdraw
circleClr=colors.get("pink")
#keep running create lp
circleClr=colors.get("blue")
circleClr=colors.get("limegreen")
background= greenClr
run = True
#crete var mve
speed= 5
while run:
    screen.fill(background)
    for event in pygame.event.get():
        if event.type==pygame.QUIT: 
            run=False 
            print("Y quit")
    keys= pygame.key. get_pressed() #this is a list
    if keys [pygame.K_RIGHT]:
        square.x += speed
    if keys[pygame.K_LEFT]:
        square.x -= speed
    if keys[pygame.K_UP]: #means loser to 0



        square.x -= speed
    #rect(surface, color, rect)>
    pygame.draw.rect(screen, redClr, square)
    #cirle(surface,color,center,radius)
    pygame.draw.circle(screen, circleClr, (350,350), 25)
    pygame.display.update()
