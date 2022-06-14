import pygame
pygame.init()

win = pygame.display.set_mode((500,480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('images\R1.png'), pygame.image.load('images\R2.png'), pygame.image.load('images\R3.png'), pygame.image.load('images\R4.png'), pygame.image.load('images\R5.png'), pygame.image.load('images\R6.png'), pygame.image.load('images\R7.png'), pygame.image.load('images\R8.png'), pygame.image.load('images\R9.png')]
walkLeft = [pygame.image.load('images\L1.png'), pygame.image.load('images\L2.png'), pygame.image.load('images\L3.png'), pygame.image.load('images\L4.png'), pygame.image.load('images\L5.png'), pygame.image.load('images\L6.png'), pygame.image.load('images\L7.png'), pygame.image.load('images\L8.png'), pygame.image.load('images\L9.png')]
bg = pygame.image.load('images\\bgSmaller.jpg')
char = pygame.image.load('images\standing.png')

x = 50
y = 400
width = 40
height = 60
vel = 5

clock = pygame.time.Clock()

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    global walkCount
    
    win.blit(bg, (0,0))  
    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1                          
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
        walkCount = 0
        
    pygame.display.update() 
    


run = True

while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: 
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow() 
    
    
pygame.quit()
    
#Creating a menu
import pygame, time,os,random, math, sys, datetime
pygame. init()#initialize the pygame package

#print(pygame.font.get_fonts())
#pygame.time.delay (10000)
TITLE_FONT = pygame.font. SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 22)

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font. SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//25)

colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51)}
clr=colors.get("limeGreen")

os.system('cls')

#screen dimensions 
WIDTH = 700
HEIGH= 700

#colors
colors = {"white":(255,255,255), "grey":(96,96,96), "Black":(0,0,0), "red":(255,0,0), "green":(0,0)}
clr= colors.get("white")
#Create a display with a name on it
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("!st game")  # title of my window

#images
bg=pygame.image.load('images\\bgSmaller.jpg')
char = pygame.image.load('images\standing.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

#square Var
hb=50
wb=50
xb=100
yb=300

charx = xb
chary = yb

cx=350
cy=350
rad=25
speed=2
ibox = rad*math.sqrt(2)
xig = cx-(ibox/2)
yig = cy-(ibox/2)

#mouse variables
mx = 0
my = 0

square=pygame.Rect(xb,yb,wb,hb)#create the object to draw
insSquare=pygame.Rect(xig,yig,ibox,ibox)
squareClr=colors.get("limeGreen")
#keep running create a lp
circleClr=colors.get("blue")
backgrnd=colors.get("Pink")
run = True
Game = False

def menu():
    global Title
    Title = TITLE_FONT.render("Circle eats Square", 1, colors.gte("blue"))

def Instructions():
    global text3 
    global text4
    #rendering text objects
    Title = TITLE_FONT.render("Menu", 1, colors.get("blue"))
    text1 = MENU_FONT.render("Yes", 1, colors.get("blue"))
    text2 = MENU_FONT.render("No", 1, colors.get("blue"))
    text3 = MENU_FONT.render("scores", 1, colors.get("blue"))
    text4 = MENU_FONT.render("Instructions", 1, colors.get("blue"))
    
    

    #fills screen with white
    screen.fill(colors.get("white"))

    #creating button options
    Button_1 = pygame.Rect(200, 400, 100, 50)
    Button_2 = pygame.Rect(400, 400, 100, 50)
    Button_3 = pygame.Rect(200,600,100, 50 )
    Button_4 = pygame.Rect(400, 600, 100, 50)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_2)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_4)

 #Instructions
    myFile = open("instructions.txt")
    content = myFile.readlines()

    #var to control change of line
    yinstructions = 150
    for line in content:
        Instruc = MENU_FONT.render(line[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yinstructions))
        pygame.display.update()
        pygame.time.delay(50)
        yinstructions += 40

    myFile.close()

    #renderig fonts to the screen
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    screen.blit(text1, (225, 410))
    screen.blit(text2, (425, 410))
    screen.blit(text3, (225,610))
    screen.blit(text4, (425,610))

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("Y quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    return True
                if Button_2.collidepoint((mx, my)):
                    return False
                if Button_3.collidepoint((mx, my)):
                    Myfile=open('How-To-Play.txt')

run = Instructions()

while run:
    # screen.fill(backgrnd)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            print("Y quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            mx = mousePos[0]
            my = mousePos[1]
    screen.blit(bg, (0,0))
    keys= pygame.key.get_pressed() #this is a list
    #mve square
    if keys[pygame.K_RIGHT] and square.x < WIDTH -(wb):
        square.x += speed
        charx += speed
    if keys[pygame.K_LEFT] and  square.x > speed:
        square.x -= speed
        charx -= speed
    if keys[pygame.K_UP] and square.y >speed:   #means closer t 0
        square.y -= speed
        chary -= speed
    if keys[pygame.K_DOWN] and square.y <HEIGHT -hb:  #means closer t max value HEIGHT
        square.y += speed
        chary += speed
        #mve Circle
    if keys[pygame.K_d] and cx < WIDTH -(rad):
        cx += speed
        insSquare.x += speed
    if keys[pygame.K_a] and  cx > (speed+rad):
        cx -= speed
        insSquare.x -= speed
    if keys[pygame.K_w] and cy >(speed+rad):   #means closer t 0
        cy -= speed
        insSquare.y -= speed
    if keys[pygame.K_s] and cy <HEIGHT -(rad):  #means closer t max value HEIGHT
        cy += speed
        insSquare.y += speed

    if square.colliderect(insSquare):
        print("BOOM")
        rad+=1
        cx=random.randint(rad, WIDTH-rad)
        cy=random.randint(rad, HEIGHT-rad)
        ibox = rad*math.sqrt(2)
        xig = cx-(ibox/2)
        yig = cy-(ibox/2)
        insSquare=pygame.Rect(xig,yig,ibox,ibox)
    #rect(surface, color, rect) -> Rect
    pygame.draw.rect(screen, squareClr,square)
    screen.blit(char, (charx, chary))
    #circle(surface, color, center, radius)
    pygame.draw.circle(screen, circleClr, (cx,cy), rad)
    pygame.draw.rect(screen, squareClr, insSquare)
    pygame.display.update()