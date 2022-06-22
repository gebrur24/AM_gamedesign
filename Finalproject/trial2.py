import pygame, os, time
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

#background and character
bg=pygame.image.load("images\spacebg.png")

def Main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 1
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 50)
    
    def redraw_window():
        win.blit(bg,(0,0))
        #draw text at top of screen
        lives_label = main_font.render(f"lives: {lives}", 1, (255,255,255))
        levels_label = main_font.render(f"level: {level}", 1, (255,255,255))

        win.blit(lives_label, (10,10))
        win.blit(levels_label, (WIDTH - levels_label.get_width() - 10, 10))

        pygame.display.update()

    #everything above is abt the background and the labels on the backgrnd
    
    
    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                self.displayText("Mission accomplished")

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:  # sipka doleva
                hero.x -= 2 if hero.x > 20 else 0  # leva hranice plochy
            elif pressed[pygame.K_RIGHT]:  # sipka doprava
                hero.x += 2 if hero.x < width - 20 else 0  # prava hranice

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.lost:
                    self.rockets.append(Rocket(self, hero.x, hero.y))

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)
                if (alien.y > height):
                    self.lost = True
                    self.displayText("YOU DIED")

            for rocket in self.rockets:
                rocket.draw()

            if not self.lost: hero.draw()

def displayText(self, text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 50)
        textsurface = font.render(text, False, (44, 0, 62))
        self.screen.blit(textsurface, (110, 160))


class Alien:
        def __init__(self, game, x, y):
            self.x = x
            self.game = game
            self.y = y
            self.size = 30

def draw(self):
        pygame.draw.rect(self.game.screen,  # renderovací plocha
                         (81, 43, 88),  # barva objektu
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
                         (210, 250, 251),
                         pygame.Rect(self.x, self.y, 8, 5))


    class Generator:
        def __init__(self, game):
            margin = 30  
            width = 50  
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
            pygame.draw.rect(self.game.screen, 
                            (254, 52, 110),  
                            pygame.Rect(self.x, self.y, 2, 4))
            self.y -= 2  
            
Main()        
