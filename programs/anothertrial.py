#Shreya Chhaya 
#tic tac toe 
#functions: 
# grid(), 
#zeroGrid()
#drawMarkers()
#checkWinner()
#gameOver()

import pygame, time, random, math, sys, os
os.system('cls')
pygame.init()
player= 1
WIDTH=700 
HEIGHT=700

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}

screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption('Tic Tac Toe')

clock=pygame.time.Clock()

player=1   #change player
gameOver=False #check if game is over
markers=[] #control cells
scoreOne=0
scoreTwo=0
winner = 0 #this means tie - save winner here either 1 or -1
lineWidth=10 #line thickness
Game=True #control game
MxMy=(0,0) #clicks
cirClr=colors.get("lblue") #colors
xClr=colors.get("lblue")

#function to zero array
def zero_Array(): 
    for x in range(3):
        row= [0] *3
        markers.append(row)
backgrnd=colors.get('black')


def grid():
    lineClr=colors.get("purple")
    for x in range(1,3):
        pygame.draw.line(screen,lineClr,(0,HEIGHT//3*x),(WIDTH,HEIGHT//3*x),lineWidth)  #Hztal line
        pygame.draw.line(screen,lineClr,(WIDTH//3*x, 0),(WIDTH//3*x,HEIGHT),lineWidth)  #Vert line
    pygame.time.delay(100)

def draw_Markers():
    xValue=0
    for x in markers:   # getting a rw
        yValue=0
        for y in x:  #each elem fthe rw
            if y ==1:
                pygame.draw.line(screen,xClr,(xValue * WIDTH//3 + 15, yValue * HEIGHT//3 + 15), (xValue * WIDTH//3 + WIDTH//3-15, yValue * WIDTH//3 + WIDTH//3-15),lineWidth)
                pygame.draw.line(screen, xClr,(xValue*WIDTH//3 +WIDTH//3-15, yValue*HEIGHT//3+15),(xValue *WIDTH//3+15,yValue*HEIGHT//3+HEIGHT//3-15),lineWidth)
            if y==-1:
                pygame.draw.circle(screen,cirClr,(xValue*WIDTH//3+WIDTH//6,yValue*HEIGHT//3 +HEIGHT//6),WIDTH//6-15, lineWidth)
            yValue +=1
        xValue +=1
    pygame.display.update()

def x_winner():
    screen.fill(backgrnd)
    sx=str(scoreOne)
    so=str(scoreTwo)
    text=MENU_FONT.render('Player X won!', 1, (cirClr))
    textScore=MENU_FONT.render('Player X score = '+sx, 1, (cirClr))
    text2Score=MENU_FONT.render('Player O score = '+so, 1, (cirClr))
    screen.blit(textScore, (WIDTH/4, HEIGHT/1.5))
    screen.blit(text2Score, (WIDTH/1.75, HEIGHT/1.5))
    screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()
def o_winner():
    screen.fill(backgrnd)
    sx=str(scoreOne)
    so=str(scoreTwo)
    texto=MENU_FONT.render('Player O won!', 1, (cirClr))
    textScore=MENU_FONT.render('Player X score = '+sx, 1, (cirClr))
    text2Score=MENU_FONT.render('Player O score = '+so, 1, (cirClr))
    screen.blit(textScore, (WIDTH/4, HEIGHT/1.5))
    screen.blit(text2Score, (WIDTH/1.75, HEIGHT/1.5))
    screen.blit(texto, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd() 
def tieGame():
    screen.fill(backgrnd)
    textTie=MENU_FONT.render("It's a tie!", 1, (cirClr))
    screen.blit(textTie, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()
    pygame.time.delay(2000)
    gameEnd()
def checkWinner():
    global gameOver, winner, scoreOne, scoreTwo
    x_position=0
    for x in markers:
        if sum(x)==3:
            winner =1
            scoreOne+=1
            gameOver=True
            x_winner()
        if sum(x)==-3:
            winner = -1
            scoreTwo+=1
            gameOver = True
            o_winner()
        #check rows
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==3:
            winner = 1
            scoreOne+=1
            gameOver=True
            x_winner()
        
        if markers[0][x_position]+markers[1][x_position]+markers[2][x_position] ==-3:
            winner = -1
            scoreTwo+=1
            gameOver=True
            o_winner()
        x_position +=1
    #check diagonals
    if markers[0][0]+markers[1][1]+markers[2][2] == 3 or markers[2][0]+markers[1][1]+markers[0][2] ==3:
        winner=1
        scoreOne+=1
        gameOver=True
        x_winner()
    if markers[0][0]+markers[1][1]+markers[2][2] == -3 or markers[2][0]+markers[1][1]+markers[0][2] == -3:
        winner=-1
        scoreTwo+=1
        gameOver=True
        o_winner()
    #check tie
    if gameOver == False:
        tie = True
        for ROW in markers:
            for COL in ROW:
                if COL ==0:
                    tie = False
        #return winner 
        if tie:  #in a boolean variable you dotn need ==
            gameOver=True
            winner=0
            print(winner)
            tieGame()

def gameEnd():
    global markers 
    screen.fill(backgrnd)
    #question
    textagn=MENU_FONT.render('Would you like to play again?', 1, (cirClr))
    textMOre=MENU_FONT.render('Click yes twice to play again. If not click no', 1, (cirClr))
    screen.blit(textMOre, (WIDTH/4, HEIGHT/2.3))
    screen.blit(textagn,(WIDTH/2.8, HEIGHT/2.8))
    #buttons yes and no
    Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50)
    Button_no=pygame.Rect(3*WIDTH/4, HEIGHT//2, 100, 50)
    pygame.draw.rect(screen, colors.get('pink'), Button_yes)
    pygame.draw.rect(screen, colors.get('pink'), Button_no)
    #text yes and no
    textYes=MENU_FONT.render('Yes', 1, (cirClr))
    textNo=MENU_FONT.render('No', 1, (cirClr))
    screen.blit(textYes, (WIDTH//4, HEIGHT//2))
    screen.blit(textNo, (3*WIDTH//4, HEIGHT//2))
    textWin1=MENU_FONT.render('Player X won the whole game!', 1, (cirClr))
    textWin2=MENU_FONT.render('Player O won the whole game!', 1, (cirClr))
    pygame.display.update()
    run=True 
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                print('go to menu')
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_yes.collidepoint((mx, my)):
                    run = False
                    markers.clear()
                    markers = []
                    zero_Array()
                    pygame.display.update()
                if Button_no.collidepoint((mx, my)): #why button taking so long?
                    text=MENU_FONT.render('Bye!', 1, (cirClr))
                    screen.fill(backgrnd)
                    screen.blit(text, (WIDTH/2.5, HEIGHT/2.5))
                    if scoreOne>scoreTwo:
                        screen.blit(textWin1, (WIDTH/3.5, HEIGHT/1.5))
                    if scoreOne<scoreTwo:
                        screen.blit(textWin2, (WIDTH/3.5, HEIGHT/1.5))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()
                    #go to menu
                

zero_Array()
while Game:
    screen.fill(backgrnd)
    grid()
    draw_Markers()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            MxMy = pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//3)
            celly=MxMy[1]//(HEIGHT//3)
            if markers[cellx][celly]==0:
                markers[cellx][celly]=player
                player *=-1
                checkWinner()
                print(winner)
                if gameOver:
                    gameOver = False
                    gameEnd()
pygame.display.update()
clock.tick(60)