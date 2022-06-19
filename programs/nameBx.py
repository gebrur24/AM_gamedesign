#Maria
#6/17/22
#get user name in pygame
import pygame, sys,os

pygame.init()
sys.os('cls')

clock=pygame.time.Clock('cls')
backgroundClr=(255,255,255)
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Get Name")
screen.fill(backgroundClr)
pygame.display.update()
run=True #run the while
user_name=''
nameClr=(0,105,105) #text the name
bxClr= (200,200,200) #text b

TITLE_FONT = pygame.font.SysFont('comicsans', 20)
MENU_FONT = pygame.font.SysFont('comicsans', 25)
title=TITLE_FONT.render("Enter Name", 1,bxClr)
screen.blit(title,(200,50))
pygame.time.delay(500)

nameBox=pygame.Rect(WIDTH/2.5, HEIGHT//4, WIDTH//2, HEIGHT//5)
pygame.draw.rect(nameBox,)
while run:
    pygame.display
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            #Menu(mainTitle,messageMenu)
            pygame.quit()
            sys.exit()
            print("You Quit")
        if event.type == pygame.MOUSEBUTTONDOWN:
            print()
        if event.type == pygame.KEYDOWN:
            if event==pygame.K_RETURN:
                print(userName)
                pygame,quit()
                sys.exit()
            if event==pygame.KSCAN_BACKSPACE:
                userName=userName[:-1]
                print('back')
            else:
                userName+= event.unicode
        pygame.draw.rect(screen, bxClr, nameBox)
        textSurface=MENU_FONT.render(userName, True, nameClr)
        #use tect x and y to allign the text
        screen.blit(textSurface, (nameBox.x+5))

        pygame.display.flip()
        clock.tick(60)



