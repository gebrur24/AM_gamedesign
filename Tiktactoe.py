#Ruth Gebru
#TikTacToe game 

#Functions: 
# make_grid()
# Zer_grid()
# draw_markers()
# check_winner()
#game _end()

from asyncio import events
import sys
from turtle import color
import pygame, time,os,random, math
pygame.init()#initialize the pygame package
os.system('cls')
WIDTH=700 #like constant
HEIGHT=700
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My First Game")  #change the title of my window

#Define list and Dict
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(15SIZE,255,51)}

SIZE=5
markers=[]
MxMy=(0,0)
lineWidth=10
cellx=0
celly=0
player=1
cirClr=colors.get("limeGreen")
XClr=colors.get("blue")

def draw_Grid():
    for x in range(SIZE):
        row=[0]*SIZE #this will create SIZE zeros
        markers.append(row)
        
#zer_grid()
#print(markers)
#markers[1][1]=-1 #first index is row sec is col
#print(markers)
#print(markers[1][1])
def zer_grid():

    def draw_grid():
        bgClr=colors.get("pink")
    lineClr=colors.get("white")
    screen.fill(bgClr)
    for x in range(1,SIZE):
        pygame.draw.line(screen, lineClr(0,HEIGHT//SIZE*x),(WIDTH,HEIGHT//SIZE*x), lineWidth)#Hztal line
        pygame.draw.line(screen, lineClr(WIDTH//SIZE*x,0),(WIDTH//SIZE*x, HEIGHT), lineWidth)   #verrt line
        pygame.display.update()
        pygame.time.delay(100)

def draw_Markers():
    xValue=0
    for x in markers: #give me each row the list
        yValue=0
        for y in x:
            if y==1:
                pygame.draw.line(screen,XClr(xValue**WIDTH//3+15, yValue*HEIGHT//3 +15),(xValue*WIDTH//3+WIDTH//3+WIDTH-15),lineWidth)
                #draw X 

            
                if y==-1:
                    #draw O
                    pygame.draw.circle(screen,cirClr, (xValue*WIDTH, //3+WIDTH//6, yValue*HEIGHT//3,HEIGHT-15), rad, lineWidth)
                yValue+=1
            xValue+=1
def check_end():
    print(markers[0][0])

draw_Grid()
zer_grid()
Game=True   
while Game:
    draw_Grid()
    draw_Markers()
    for even in pygame.event.get():
        if events.tupe==pygame.QUIT:
            #menu(titleMain,messageMenu,True)
            pygame.exit()
            sys.exit()
        if  events.type == pygame.MOUSEBUTTONDOWN:
            MxMy=pygame.mouse.get_pos()
            cellx=MxMy[0]//(WIDTH//SIZE)
            celly=MxMy[1]//(HEIGHT//SIZE)
            print(markers)
            if markers[cellx][celly]==0:
               markers[cellx][celly]==player
               player*=-1
