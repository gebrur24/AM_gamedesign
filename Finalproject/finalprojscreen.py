#Ruth Gebru
#6/20/2022
#I am creating a space invaders/fruit ninja game





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
#images for the game
Strawberry= pygame.image.load("images\strawberry.png")  
Orange= pygame.image.load("images\orange.png")
pineapple=pygame.image.load("images\pineapple.png")
cherry=pygame.image.load("images\cherry.jpg")
apple= pygame.image.load("images\/apple1.png")
lemon=pygame.image.load("images\lemon.png")


# laser to cut fruit
laser=pygame.image.load("images\\red_laser.png")

#background and character
bg=pygame.image.load("images\spacebg.png")
character=pygame.image.load("images\\ninja.png")

class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img= pygame.image.load("images\\ninja.png")
        self.laser_imag = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50,50))

def Main():
    run = True
    frame = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 3
    player_vel= 5
    main_font = pygame.font.SysFont("comicsans", 50)

  

    ship = Ship(300, 650)

    def redraw_window():
        win.blit(bg, (0,0))
        #text with be drawn at the top of the game so it can be seen by the player
        lives = main_font.render("level: 1", 1,(255,255,255))
        level = main_font.render("lives: 3", 1,(255,255,255))

        win.blit(lives,(10,10))
        win.blit(level,(WIDTH - level.get_width()- 10,10))
        
        ship.draw(win)

        pygame.display.update()

    while run:
        clock.tick(frame)
        redraw_window()
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: #left
            ship.x -= player_vel
        if keys[pygame.K_d]: #right
            ship.x += player_vel
        if keys[pygame.K_w]: #up
            ship.x -= player_vel
        if keys[pygame.K_s]: #down
            ship.y += player_vel


            

Main() 


