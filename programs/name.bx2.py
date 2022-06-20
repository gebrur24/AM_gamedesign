# maria Suarez
#6/17/22
#get user_name in python
import pygame, sys,os

pygame.init()
os.system('cls')

clock= pygame.time.Clock()
backgrndClr= (255,255,255)
WIDTH = 700
HEIGHT = 700
screen =pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgrndClr)

run= True #run the while 
user_name=''
nameClr= (0,105,105)
bxClr= (200,200,200)

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)

title=TITLE_FONT.render("Enter Name", 1, bxClr)
screen.blit(title,(WIDTH//2.5, HEIGHT//7))
pygame.time.delay(200)

nameBox=pygame.Rect(WIDTH//4, HEIGHT//3, WIDTH//2, HEIGHT//10)
pygame.draw.rect(screen, bxClr, nameBox)
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle, messageMenu)
            pygame.quit()
            sys.exit()
            print("You Quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event==pygame.K_RETURN:
                print(user_name)
                pygame,quit()
                sys.exit
            if event==pygame.KSCAN_BACKSPACE:
                user_name=user_name[:-1]
                print('back')
            else:
                user_name += event.unicode
        pygame.draw.rect(screen, bxClr, nameBox)
        textSurface=MENU_FONT.render(user_name, True, nameClr)
        #use tect x and y to allign the text
        screen.blit(textSurface, (nameBox.x+5, nameBox.y+5))
    
        pygame.display.flip()
        clock.tick(60)
        #return to menu
        #before mainmen function


