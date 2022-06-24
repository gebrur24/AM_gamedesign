import sys
import pygame, time,os,random, math, datetime
date=datetime.datetime.now()

pygame.init()#initialize the pygame package

os.system('cls')
WIDTH=700 #like constant
HEIGHT=700

TITLE_FONT = pygame.font.SysFont('comicsans', WIDTH//20)
MENU_FONT = pygame.font.SysFont('comicsans', WIDTH//30)
colors={"white":(255,255,255),"pink":(255,0,255),"blue":(0,0,255),"limeGreen":(153,255,51), 'red':(255, 0, 0), 'purple': (138,43,226), 'yellow':(255,215,0), 'black':(0,0,0), 'lblue':(0,206,209)}
clock=pygame.time.Clock()

message=['Instructions', 'Settings', 'Game 1', 'Game 2', 'Scoreboard', 'Exit']
#create dispay wind with any name y like
screen=pygame.display.set_mode((WIDTH,HEIGHT)) 
pygame.display.set_caption("My final game")  #change the title of my window


menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
#boxes for menu
Bx=WIDTH/2.5
Button_menu=pygame.Rect(Bx, 125, WIDTH/4, 40)
Button_instruct=pygame.Rect(Bx, 150, WIDTH//4, 40)
Button_settings=pygame.Rect(Bx, 200, WIDTH/4, 40)
Button_Game1=pygame.Rect(Bx, 250, WIDTH/4, 40)
Button_Game2=pygame.Rect(Bx, 300, WIDTH/4, 40)
Button_score=pygame.Rect(Bx, 350, WIDTH/4, 40)
Button_exit=pygame.Rect(Bx, 400, WIDTH/4, 40)
#images
bg=pygame.image.load(r'C:\\Users\\gebrur24\\OneDrive - Greenhill School\Desktop\AM_gamedesign\AM_gamedesign\\images\\bgSmaller.jpg')
char = pygame.image.load(r'C:\\Users\\gebrur24\\OneDrive - Greenhill School\Desktop\AM_gamedesign\AM_gamedesign\\images\standing.png')
char = pygame.transform.scale(char, (50, 50))
# screen.blit(bg, (0,0))
# pygame.display.update()
# pygame.time.delay(5000)

mx = 0
my = 0

score = 0



def mainMenu():
    global menuColor
    pygame.draw.rect(screen, colors.get('limeGreen'), Button_settings)
    Title = TITLE_FONT.render("Ruth's final game ", 1, colors.get("blue"))
    screen.fill(menuColor)
    xd = WIDTH//2 - (Title.get_width()//2)
    screen.blit(Title, (xd, 50))
    yMenu=150
    
    for item in message:
        Button_menu=pygame.Rect(WIDTH/2.5, yMenu, WIDTH/4, 40)
        text=MENU_FONT.render(item, 1, colors.get('blue'))
        pygame.draw.rect(screen, colors.get('limeGreen'), Button_menu)
        screen.blit(text, (WIDTH/2.5, yMenu))
        pygame.display.update()
        pygame.time.delay(50)
        yMenu += 50
        

    
    MENU=True
    while MENU:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("You quit")
                pygame.display.quit()
                MENU=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_instruct.collidepoint((mx, my)):
                    Instructions()
                if Button_settings.collidepoint((mx, my)):
                    settings()
                if Button_Game1.collidepoint((mx, my)):
                    Game_1()
                if Button_score.collidepoint((mx, my)):
                    scoreboard()
                if Button_exit.collidepoint((mx, my)):
                    exit()
                if Button_Game2.collidepoint((mx, my)):
                    Game_2()
    
def Instructions():
    #rendering text objects
    Title = TITLE_FONT.render("Instructions", 1, colors.get("blue"))
    text = MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    #fills screen with white
    screen.fill(menuColor)

    #creating button options
    Button_1 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_1)

    #Instructions
    myFile = open("programs\instructions234.txt", "r")
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
    screen.blit(text, (WIDTH//17,HEIGHT/1.1))

    pygame.display.update()
    Instructions = True
    while Instructions:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Instructions=False
                pygame.display.quit()
                print("You quit")
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = pygame.mouse.get_pos()
                mx = mousePos[0]
                my = mousePos[1]
                if Button_1.collidepoint((mx, my)):
                    mainMenu() 

def namebox():

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
    run=True
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
                if event.key ==pygame.K_RETURN:
                    print(user_name)
                    run=False
                    mainMenu()
                elif event.key ==pygame.KSCAN_BACKSPACE:
                    user_name=user_name[:-1]
                    print('back')
                else:
                    user_name += event.unicode
                pygame.draw.rect(screen, bxClr, nameBox)
                textSurface=MENU_FONT.render(user_name, True, nameClr)
                #use tect x and y to allign the text
                screen.blit(textSurface, (nameBox.x+5, nameBox.y+5))
                pygame.display.update()


def settings():
    global menuColor
    global screen 
    global WIDTH
    global HEIGHT
    title=TITLE_FONT.render('Settings', 1, colors.get('blue'))
    text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))

    screen.fill(menuColor)

    color=MENU_FONT.render('Change Background Color:', 1, colors.get('blue'))
    screen.blit(color, (WIDTH/18, HEIGHT/4))
    pygame.display.update()
    pygame.time.delay(50)
    
    
#changing color random
    Button_color = pygame.Rect(WIDTH/21, HEIGHT/3, WIDTH//3.8, 40)
    pygame.draw.rect(screen, colors.get('white'), Button_color)

    textcolor = MENU_FONT.render('Random', 1, colors.get('blue'))
    screen.blit(textcolor, (WIDTH/20, HEIGHT/3))
#back to menu
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("white"), Button_3)

    #buttons for size changing 
    Button_4=pygame.Rect(WIDTH/20, HEIGHT/1.8, WIDTH//7, 40)
    Button_5=pygame.Rect(WIDTH/4, HEIGHT/1.8, WIDTH//5, 40)
    pygame.draw.rect(screen, colors.get('white'), Button_4)
    pygame.draw.rect(screen, colors.get('white'), Button_5)

    #buttons for sound
    Button_on=pygame.Rect(WIDTH/20, HEIGHT/1.3, WIDTH//6, 40)
    Button_off=pygame.Rect(WIDTH/3, HEIGHT/1.3, WIDTH//6, 40)
    pygame.draw.rect(screen, colors.get('white'), Button_on)
    pygame.draw.rect(screen, colors.get('white'), Button_off)

    #text for buttons/screen
    screen.blit(title, (WIDTH/2.5,50))
    screen.blit(text, (WIDTH//18, HEIGHT/1.1))
    text5=MENU_FONT.render('UP 100', 1, colors.get('blue'))
    text6=MENU_FONT.render('DOWN 100', 1, colors.get('blue'))
    screen.blit(text5, (WIDTH/18, HEIGHT/1.8))
    screen.blit(text6, (WIDTH/4, HEIGHT/1.8))
    
    text7=MENU_FONT.render('Sound On', 1, colors.get('blue'))
    text8=MENU_FONT.render('Sound Off', 1, colors.get('blue'))
    screen.blit(text7, (WIDTH/18, HEIGHT/1.3))
    screen.blit(text8, (WIDTH/3, HEIGHT/1.3))
    text10=MENU_FONT.render('Change screen size:', 1, colors.get('blue'))
    text11=MENU_FONT.render('Change sound settings:', 1, colors.get('blue'))
    screen.blit(text10, (WIDTH/18, HEIGHT/2.1))
    screen.blit(text11, (WIDTH/18, HEIGHT/1.5))


    pygame.display.update()

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                mainMenu()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                #button for menu
                if Button_3.collidepoint((mx, my)):
                    mainMenu()
                    #button for color
                if Button_color.collidepoint((mx, my)):
                    menuColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    print("change color")
                    pygame.display.update()
                    settings()
                    #buttons for sizing
                if Button_4.collidepoint((mx,my)) and WIDTH <1000 and HEIGHT<1000:
                    WIDTH +=100
                    HEIGHT +=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
                if Button_5.collidepoint((mx,my)) and WIDTH>600 and HEIGHT>600:
                    WIDTH -=100
                    HEIGHT -=100
                    screen=pygame.display.set_mode((WIDTH, HEIGHT))
                    settings()
            pygame.display.update()

def scoreboard():
    high=0
    title=TITLE_FONT.render('Scoreboard', 1, colors.get('blue'))
    text3 = MENU_FONT.render("Return to Menu", 1, colors.get("blue"))

    screen.fill(menuColor)
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
    
    screen.blit(title, (WIDTH//3,50))
    screen.blit(text3, (WIDTH//17, HEIGHT/1.1))
    pygame.display.update()
    
    
    print(yscore) # referrenced before its been created: yscore
    # if score>high:
    #     high=score
    # scrLine=str(high)+"\t " (':')+ "\t" +date.strftime('%m/%d/%Y')+ "\n"
    scrLine=str(yscore)+(': ')+ "\t"+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("Finalproject\\finalscoreboard.py", "a")
    myFile.write(str(scrLine))
    myFile.close()

    myFile=open('Finalproject\\finalscoreboard.py', 'r')
    content = myFile.readlines()

    #var to controll change of line
    yscore = 150
    for lines in content:
        Instruc = MENU_FONT.render(lines[0:-1], 1, colors.get("blue"))
        screen.blit(Instruc, (40, yscore))
        pygame.display.update()
        pygame.time.delay(50)
        yscore += 40

    myFile.close()

    scoreboard=True
    while scoreboard:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.display.quit()
                print("You quit")
            if event.type==pygame.MOUSEBUTTONDOWN:
                mousePos=pygame.mouse.get_pos()
                mx=mousePos[0]
                my=mousePos[1]
                if Button_3.collidepoint((mx, my)):
                    mainMenu()

    while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.display.quit()
                    print("You quit")
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_3.collidepoint((mx, my)):
                        mainMenu()

def exit():
    title=TITLE_FONT.render('Bye-Thank you!', 1, colors.get('blue'))
    screen.fill(menuColor)

    screen.blit(title, (WIDTH/2.5, HEIGHT/2.5))
    pygame.display.update()

    pygame.time.delay(1000)
    pygame.display.quit()







def Game_1():

    WIDTH, HEIGHT = 750, 750
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space invaders")

    # Load images
    RED_SPACE_SHIP = pygame.image.load(os.path.join( "images\pixel_ship_red_small.png"))
    GREEN_SPACE_SHIP = pygame.image.load(os.path.join( "images\pixel_ship_green_small.png"))
    BLUE_SPACE_SHIP = pygame.image.load(os.path.join( "images\pixel_ship_blue_small.png"))

    # Player player
    YELLOW_SPACE_SHIP = pygame.image.load(os.path.join( "images\pixel_ship_yellow.png"))

    # Lasers
    RED_LASER = pygame.image.load(os.path.join("images\pixel_laser_red.png"))
    GREEN_LASER = pygame.image.load(os.path.join("images\pixel_laser_green.png"))
    BLUE_LASER = pygame.image.load(os.path.join( "images\pixel_laser_blue.png"))
    YELLOW_LASER = pygame.image.load(os.path.join( "images\pixel_laser_yellow.png"))

    # Background
    BG = pygame.transform.scale(pygame.image.load(os.path.join("images\level2bg.png")), (WIDTH, HEIGHT))
    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)


    class Laser:
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
            return not(self.y <= height and self.y >= 0)

        def collision(self, obj):
            return collide(self, obj)
            


    class Ship:
        COOLDOWN = 30

        def __init__(self, x, y, health=100):
            self.x = x
            self.y = y
            self.health = health
            self.ship_img = None
            self.laser_img = None
            self.lasers = []
            self.cool_down_counter = 0

        def draw(self, window):
            pygame.draw.rect(window, (255,0,0), (self.x, self.y, 0,0))
            window.blit(self.ship_img, (self.x, self.y))
            for laser in self.lasers:
                laser.draw(window)

        def move_lasers(self, vel, obj):
            self.cooldown()
            for laser in self.lasers:
                laser.move(vel)
                if laser.off_screen(HEIGHT):
                    self.lasers.remove(laser)
                elif laser.collision(obj):
                    obj.health -= 10
                    self.lasers.remove(laser)

        def cooldown(self):
            if self.cool_down_counter >= self.COOLDOWN:
                self.cool_down_counter = 0
            elif self.cool_down_counter > 0:
                self.cool_down_counter += 1

        def shoot(self):
            if self.cool_down_counter == 0:
                laser = Laser(self.x, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1

        def get_width(self):
            return self.ship_img.get_width()

        def get_height(self):
            return self.ship_img.get_height()

        score_value= 0
        font = pygame.font.Font('freesansbold.ttf', 32)
        textx = 10
        texty = 10


    class Player(Ship):
        def __init__(self, x, y, health=100):
            super().__init__(x, y, health)
            self.ship_img = YELLOW_SPACE_SHIP
            self.laser_img = YELLOW_LASER
            #mask means where things are or are not
            #so when there is a collision we know that a laser was fired
            self.mask = pygame.mask.from_surface(self.ship_img)
            self.max_health = health

        def move_lasers(self, vel, objs):
            self.cooldown()
            for laser in self.lasers:
                laser.move(vel)
                if laser.off_screen(HEIGHT):
                    self.lasers.remove(laser)
                else:
                    for obj in objs:
                        if laser.collision(obj):
                            objs.remove(obj)
                            if laser in self.lasers:
                                self.lasers.remove(laser)

        def draw(self, window):
            super().draw(window)
            self.healthbar(window)

        def healthbar(self, window):
            pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
            pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))



    #these are the enemy ship, 
    #not sure if i should try to move them below into the redraw window
    class Enemy(Ship):
        COLOR_MAP = {
                    "red": (RED_SPACE_SHIP, RED_LASER),
                    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
                    "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
                    }

        def __init__(self, x, y, color, health=100):
            super().__init__(x, y, health)
            self.ship_img, self.laser_img = self.COLOR_MAP[color]
            self.mask = pygame.mask.from_surface(self.ship_img)

        def move(self, vel):
            self.y += vel

        def shoot(self):
            if self.cool_down_counter == 0:
                laser = Laser(self.x-20, self.y, self.laser_img)
                self.lasers.append(laser)
                self.cool_down_counter = 1


    def collide(obj1, obj2):# the obj is whatever the laser is colliding with
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

   

    def main():
        run = True
        FPS = 60
        level = 2
        lives = 7
        main_font = pygame.font.SysFont("comicsans", 50)
        lost_font = pygame.font.SysFont("comicsans", 60)

        enemies = []
        wave_length = 3
        enemy_vel = 1

        player_vel = 5 #velocity variable which is how fast square can move in a direction
        laser_vel = 6

        player = Player(300, 630)

        clock = pygame.time.Clock()
        won_count = 5
        won = True
        lost = False
        lost_count = 0

        

        def redraw_window():
            #below is where the info for my rectangle and image are
            #redraw window 3x bc it will restart a life
            win.blit(BG, (0,0))
            # draw text
            lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
            #text with be drawn at the top of the game so it can be seen by the player

            win.blit(lives_label, (10, 10))
            #i think this is the position of the square
    
            #this is where my enemies appear

            for enemy in enemies:
                enemy.draw(win)

            player.draw(win)

            if lost:
                lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
                win.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
                Endgame(1)
                

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
                if lost_count > FPS * 3:
                    run = False
                else:
                    continue

            if len(enemies) == 0:
                level += 1
                wave_length += 5
                for i in range(wave_length):
                    enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)


            #keys for moving up,down,right,left
            #i think this is the position of the square
            #these keys are for the red square
            #without them the square will not pop up by themselves
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x - player_vel > 0: # left
                player.x -= player_vel
            if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH: # right
                player.x += player_vel
            if keys[pygame.K_UP] and player.y - player_vel > 0: # up
                player.y -= player_vel
            if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
                player.y += player_vel
            if keys[pygame.K_SPACE]:
                player.shoot()

            # meaning: velcotity of square to value of x= will be off the screen
            #I am having trouble with the red square staying with in the lines of visable areas

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, player)

                if random.randrange(0, 2*60) == 1:
                    enemy.shoot()

                if collide(enemy, player):
                    player.health -= 10
                    enemies.remove(enemy) 
                elif enemy.y + enemy.get_height() > HEIGHT:
                    lives -= 1
                    enemies.remove(enemy)
        


    


            player.move_lasers(-laser_vel, enemies)

    def main_menu():
        title_font = pygame.font.SysFont("comicsans", 40)
        run = True
        while run:
            win.blit(BG, (0,0))
            title_label = title_font.render("click on the screen to begin", 1, (255,255,255))
            win.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    

                
                    main()
        pygame.quit()
    
    def display_score(score):
        score_surf = self.font.render(f'score: {self.score}',False, )

    
    def zero_Array(): 
        for x in range(3):
            row= [0] *3
            markers.append(row)
    backgrnd=colors.get('pink')

    




    def Endgame(num):
        #question
        
        
        screen.fill('Blue')
        textagn=MENU_FONT.render('Would you like to play again?', 1, (255,255,255))
        textMOre=MENU_FONT.render('press yes to play again or no!', 2, (255,255,255))
        screen.blit(textMOre, (WIDTH/3, HEIGHT/2.3))
        screen.blit(textagn,(WIDTH/3, HEIGHT/2.8))
        #buttons yes and no
        Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50) #how to draw a rectangle
        Button_no=pygame.Rect(3*WIDTH/4, HEIGHT//2, 100, 50)
        pygame.draw.rect(screen, colors.get('pink'), Button_yes)
        pygame.draw.rect(screen, colors.get('pink'), Button_no)
        #text yes and no
        textYes=MENU_FONT.render('Yes', 1, (255,255,255))
        textNo=MENU_FONT.render('  No', 1, (255,255,255))
        screen.blit(textYes, (WIDTH//3.8, HEIGHT//2))
        screen.blit(textNo, (3*WIDTH//4, HEIGHT//2))
                   
        text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
        screen.blit(text, (WIDTH//18, HEIGHT/1.1))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.display.quit()
                    print("You quit")
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_3.collidepoint((mx, my)):
                        mainMenu()
                    if Button_yes.collidepoint((mx, my)):

                        if num==1:
                            Game_1()
                        if num==2:
                            Game_2()

                    if Button_no.collidepoint((mx, my)):
                        mainMenu()
                       
                        
    
                
            
        
    

    
    main_menu()








def Game_2():
    global screen
    class Game:

        screen = None
        aliens = []
        rockets = []
        lost = False

        def __init__(self, width, height):
            pygame.init()
            self.width = width
            self.height = height
            self.screen = pygame.display.set_mode((width, height))
            self.clock = pygame.time.Clock()
            done = False

            hero = Hero(self, width / 2, height - 20)
            generator = Generator(self)
            rocket = None

            while not done:
                if len(self.aliens) == 0:
                    self.displayText("YAY!!!Winner!!")

                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_LEFT]:  # sipka doleva
                    hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
                elif pressed[pygame.K_RIGHT]:  # sipka doprava
                    hero.x += 2 if hero.x < width - 20 else 0  # prava hranice

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        screen=pygame.display.set_mode((WIDTH, HEIGHT))
                        done = True
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                        self.rockets.append(Rocket(self, hero.x, hero.y))

                pygame.display.flip()
                self.clock.tick(60)
                self.screen.fill((255,255,255))

                for alien in self.aliens:
                    alien.draw()
                    alien.checkCollision(self)
                    if (alien.y > height):
                        self.lost = True
                        self.displayText("EW!YOU LOST")

                for rocket in self.rockets:
                    rocket.draw()

                if not self.lost: hero.draw()
                

        def displayText(self, text):
            pygame.font.init()
            font = pygame.font.SysFont('comicsans', 30)
            textsurface = font.render(text, False, ('black'))
            self.screen.blit(textsurface, (110, 160))


    class Alien:
        def __init__(self, game, x, y):
            self.x = x
            self.game = game
            self.y = y
            self.size = 20

        def draw(self):
            pygame.draw.rect(self.game.screen,  
                            ('pink'),  
                            pygame.Rect(self.x, self.y, self.size, self.size))
            self.y += 0.05

        def checkCollision(self, game):
            for rocket in game.rockets:
                if (rocket.x < self.x + self.size and
                        rocket.x > self.x - self.size and
                        rocket.y < self.y + self.size and
                        rocket.y > self.y - self.size):
                    game.rockets.remove(rocket)
                    game.aliens.remove(self)


    class Hero:
        def __init__(self, game, x, y):
            self.x = x
            self.game = game
            self.y = y

        def draw(self):
            pygame.draw.rect(self.game.screen,
                            ('blue'),
                            pygame.Rect(self.x, self.y, 8, 5))


    class Generator:
        def __init__(self, game):
            margin = 30  # mezera od okraju obrazovky
            width = 50  # mezera mezi alieny
            for x in range(margin, game.width - margin, width):
                for y in range(margin, int(game.height / 2), width):
                    game.aliens.append(Alien(game, x, y))

            # game.aliens.append(Alien(game, 280, 50))


    class Rocket:
        def __init__(self, game, x, y):
            self.x = x
            self.y = y
            self.game = game

        def draw(self):
            pygame.draw.rect(self.game.screen,  # renderovací plocha
                            (254, 52, 110),  # barva objektu
                            pygame.Rect(self.x, self.y, 2, 4))
            self.y -= 2  # poletí po herní ploše nahoru 2px/snímek


    if __name__ == '__main__':
        game = Game(600, 400)
        Endgame(2)

    Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
    pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)

def Endgame(num):
        #question
        screen=pygame.display.set_mode((WIDTH, HEIGHT))
        screen.fill('Blue')
        textagn=MENU_FONT.render('Would you like to play again?', 1, (255,255,255))
        textMOre=MENU_FONT.render('press yes to play again or no!', 2, (255,255,255))
        screen.blit(textMOre, (WIDTH/3, HEIGHT/2.3))
        screen.blit(textagn,(WIDTH/3, HEIGHT/2.8))
        #buttons yes and no
        Button_yes=pygame.Rect(WIDTH/4, HEIGHT//2, 100, 50) #how to draw a rectangle
        Button_no=pygame.Rect(3*WIDTH/4, HEIGHT//2, 100, 50)
        pygame.draw.rect(screen, colors.get('pink'), Button_yes)
        pygame.draw.rect(screen, colors.get('pink'), Button_no)
        #text yes and no
        textYes=MENU_FONT.render('Yes', 1, (255,255,255))
        textNo=MENU_FONT.render('  No', 1, (255,255,255))
        screen.blit(textYes, (WIDTH//3.8, HEIGHT//2))
        screen.blit(textNo, (3*WIDTH//4, HEIGHT//2))
                   
        text=MENU_FONT.render('Return to Menu', 1, colors.get('blue'))
        Button_3 = pygame.Rect(WIDTH//18, HEIGHT/1.1, WIDTH//4, 40)
        pygame.draw.rect(screen, colors.get("limeGreen"), Button_3)
        screen.blit(text, (WIDTH//18, HEIGHT/1.1))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run=False
                    pygame.display.quit()
                    print("You quit")
                if event.type==pygame.MOUSEBUTTONDOWN:
                    mousePos=pygame.mouse.get_pos()
                    mx=mousePos[0]
                    my=mousePos[1]
                    if Button_3.collidepoint((mx, my)):
                        mainMenu()
                    if Button_yes.collidepoint((mx, my)):

                        if num==1:
                            Game_1()
                        if num==2:
                            Game_2()

                    if Button_no.collidepoint((mx, my)):
                        mainMenu()

        
namebox()  
print("1")    
mainMenu()
Instructions() 
exit()