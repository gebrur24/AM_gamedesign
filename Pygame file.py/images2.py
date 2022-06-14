#Maria Suarez
#6/9/2022
#We are learning pygame basic functins, 
# creating screens, clrs, shape ,move 
# move  the square
# K_UP                  up arrow
# K_DOWN                down arrow
# K_RIGHT               right arrow
# K_LEFT                left arrow
#picture = pygame. image. load(filename)
#picture = pygame. transform. scale(picture, (1280, 720))
#bg=pygame.image.load('ClassStuff\CircleEatsSquare\Images\\bgSmaller.jpg')

import pygame, time,os
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window
#square Var
hb=50
wb=50
xb=100
yb=300
square=pygame.Rect(xb,yb,wb,hb)# create the object to draw
squareClr=colors.get("pink")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("limeGreen")
run = True
#create var mve
speed=2
cx=350
cy=350
rad=25
while run:
    screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
    keys= pygame.key.get_pressed() #this is a list
    #mve square
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means clser t 0
        square.y -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means clser t max value HEIGHT
        square.y += speed
        #mve circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
    if keys[pygame.K_a] and  cx > (speed+rad):
        cx -= speed
    if keys[pygame.K_w] and cy > (speed+rad):   #means clser t 0
        cy -= speed
    if keys[pygame.K_s] and cy <HEIGHT -hb:  #means clser t max value HEIGHT
       cy += speed
    if square.collidpoint(cx.cy):
        print("BOOM")
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        rad+=5
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.display.update()