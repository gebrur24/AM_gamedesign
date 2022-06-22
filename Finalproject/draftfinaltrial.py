#Ruth Gebru
#6/20/2022
#I am creating a space invaders/fruit ninja game


from turtle import color
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
yb= 100
xb= 300

#image variable
yellow= pygame.image.load("images\pixel_ship_yellow.png")  
red= pygame.image.load("images\pixel_ship_red_small.png")
blue=pygame.image.load("images\pixel_ship_blue_small.png")
green=pygame.image.load("images\pixel_ship_green_small.png")

# laser to cut fruit
redlaser=pygame.image.load("images\\red_laser.png")

#background and character
bg=pygame.image.load("images\spacebg.png")
char=pygame.image.load("images\ship.png")
char= pygame.transform.scale(char,(40,40))
screen.blit(char, (WIDTH//3, HEIGHT//4))



class Ship:
    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img= pygame.image.load("images\ship.png")
        self.laser_imag = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img(self.x, self.y))
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 50,50))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class player(Ship):  
    def __init__(self, x, y, health=100):
        super().__init__(x,y, health)
        self.ship_img = Ship
        self.laser_imag = redlaser
        self.mask = pygame.mask.from_surface(self.ship_img)
        #mask means where things are or are not
        #so when there is a collision we know that a laser was fired
        self.max_health = health
    




#these are the enemy ship, 
#not sure if i should try to move them below into the redraw window
class alien(Ship):
    COLOR_MAP ={ "red": (red), "green": (green),"blue": (blue), "yellow": (yellow)}
    def __init__(self, x, y, health=100): 
        super().__init__(x, y, health) 
        self.ship_img, self.laser_imag= self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self,vel):
        self.y +=vel
        
def Main():
    run = True
    frame = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 3
    player_vel= 5 #velocity variable which is how fast square can move in a direction
    x = 600 #positioning of the object on either the X or Y axis
    y = 600
    main_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    
    ship = Ship(300, 650)
#below is where the info for my rectangle and image are
    def redraw_window(): #redraw window 3x bc it will restart a life
        global x,y
        win.blit(bg, (0,0))
        #text with be drawn at the top of the game so it can be seen by the player
        lives = main_font.render("level: 1", 1,(255,255,255))
        level = main_font.render("lives: 3", 1,(255,255,255))
       
        win.blit(lives,(10,10))
        win.blit(level,(WIDTH - level.get_width()- 10,10))
        char=pygame.image.load("images\ship.png")
        char= pygame.transform.scale(char,(50,50))# zoom in on character
        screen.blit(char,(ship.x, ship.y))#i think this is the position of the square
    
        
        for enemy in enemies:
            enemy.draw(win)

        pygame.display.update()

    while run:
        clock.tick(frame)
        
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = alien(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                enemies.append(alien)
                #start at -1500, so they start off the screen

       #Keys for moving around the square
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False
        screen.blit(char,(ship.x, ship.y))#i think this is the position of the square
        #these keys are for the red square
        #without them the square will not pop up by themselves
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and ship.x - player_vel > 0: 
            ship.x -= player_vel
        if keys[pygame.K_RIGHT] and ship.x + player_vel < WIDTH -50 : 
        # meaning: velcotity of square to value of x= will be off the screen
            ship.x += player_vel
        if keys[pygame.K_UP] and ship.y - player_vel > 0:
            ship.y -= player_vel
        if keys[pygame.K_DOWN] and ship.y + player_vel < HEIGHT:
            ship.y += player_vel
       #I am having trouble with the red square staying with in the lines of visable areas
        pygame.time.delay(10) 
        

        for enemy in enemies:
            enemy.move(enemy_vel)
            
        redraw_window() 
        
        Main()      
