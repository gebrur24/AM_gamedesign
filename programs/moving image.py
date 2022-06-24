#ruth
import pygame, sys, os, random, time
pygame.font.init()
WIDTH = 600 #size of the screen
HEIGHT = 600
win = pygame.display.set_mode((600,600))
pygame.display.set_caption("space invaders")
clock = pygame.time.Clock()
TITLE_FONT = pygame.font.SysFont('comicsans', 40)
MENU_FONT = pygame.font.SysFont('comicsans', 20)
main_font = pygame.font.SysFont("comicsans", 30)
screen=pygame.display.set_mode((WIDTH,HEIGHT))





colors= (255,255,255)
backgrndcolor= (255,255,255)
ship_x = 30
ship_y = 30

move_left = False
move_right = False
move_down = False
move_up = False

while True:
    screen.fill(backgrndcolor)
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if(event.key == pygame.K_RIGHT):
                move_right = True
            if(event.key == pygame.K_LEFT):
                move_left = True
            if(event.key == pygame.K_DOWN):
                move_down = True
            if(event.key == pygame.K_UP):
                move_up = True
        elif(event.type == pygame.KEYUP):
            if(event.key == pygame.K_RIGHT):
                move_right = False
            if(event.key == pygame.K_LEFT):
                move_left = False
            if(event.key == pygame.K_DOWN):
                move_down = False
            if(event.key == pygame.K_UP):
                move_up = False
    if(move_right):
        ship_x += 1
    