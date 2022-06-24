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
greenlaser=pygame.image.load("images\pixel_laser_green.png")
bluelaser=pygame.image.load("images\pixel_laser_blue.png")
yellowlaser=pygame.image.load("images\pixel_laser_yellow.png")

#background and character
bg=pygame.image.load("images\spacebg.png")
char=pygame.image.load("images\ship.png")
char= pygame.transform.scale(char,(40,40))
screen.blit(char, (WIDTH//3, HEIGHT//4))

class laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y < height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)

class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img= pygame.image.load("images\ship.png")
        self.laser_imag = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        pygame.draw.rect(window, (255,0,0), (self.x, self.y, 0,0))
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.laser:
            laser.draw(window)


    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.laser.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.laser.remove(laser)



    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = laser(self.x, self.y, self.laser_img)
            self.laser.append(laser)
            self.cool_down_counter = 1

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


    def move_laser(self, vel, objs):
        self.cooldown()
        for laser in self.laser:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.laser.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.laser.remove(laser)



#these are the enemy ship, 
#not sure if i should try to move them below into the redraw window
class alien(Ship):
    COLOR_MAP ={ "red": (red,redlaser), "green": (green,greenlaser),"blue": (blue,bluelaser), "yellow": (yellow,yellowlaser)}
    color=COLOR_MAP.get("green")
    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    


    def move(self, vel):
        self.y += vel

def collide( obj1, obj2):# the obj is whatever the laser is colliding with
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2, (offset_x, offset_y)) != None

        
def Main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 3
    player_vel= 5 #velocity variable which is how fast square can move in a direction
    x = 600 #positioning of the object on either the X or Y axis
    y = 600
    main_font = pygame.font.SysFont("comicsans", 50)
    lost_font = pygame.font.SysFont("comicsans", 60)
    enemies = [red,green,blue,yellow]
    wave_length = 5
    enemy_vel = 1
    player.health= 10
    ship = Ship(300, 650)
    lost = False
    lost_count = 0
    laser_vel = 4
    

 
    

    


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
        char= pygame.transform.scale(char,(50,50))
        # zoom in on character
        screen.blit(char,(ship.x, ship.y))
        #i think this is the position of the square
    
        #this is where my enemies appear
        for enemy in enemies:
            enemy.draw(win)
        
        
        #txt for lost
        if lost: 
            lost_label = lost_font.render("You Lost!!", 1,(255,255,255))
            win.blit(lost_label, (WIDTH/2- lost_label.get_width()/2, 350))
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()
        #ask question about how to lose points
        #why is the number of lives not changing each time a player is hit


        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1
        if lost:
            if lost_count > FPS * 3:# 3 second time so now lets quit da game
                run = False 
            else:
                continue
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = alien (random.randrange(100, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green", "yellow"]))
                enemies.append(enemy)



       #Keys for moving around the square
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                run = False

        screen.blit(char,(ship.x, ship.y))
        #i think this is the position of the square
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
        if keys[pygame.K_SPACE]:
            player.shoot()
    
    
         
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)
            if enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                
        player.move_laser(-laser_vel, enemies)

    pygame.time.delay(10)         
Main() 


