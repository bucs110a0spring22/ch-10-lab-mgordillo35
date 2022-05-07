import sys
import pygame
import random
from src import hero
from src import enemy
from replit import audio
#from src import music



class Controller:
    def __init__(self, width=640, height=480):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.background.fill((250, 250, 250))  # set the background to white
        pygame.font.init()  # you have to call this at the start, if you want to use this module.
        pygame.key.set_repeat(1, 50)  # initialize a held keey to act as repeated key strikes
        """Load the sprites that we need"""

        self.enemies = pygame.sprite.Group()
        num_enemies = 3
        for i in range(num_enemies):
            x = random.randrange(100, 400)
            y = random.randrange(100, 400)
            self.enemies.add(enemy.Enemy("Boogie", x, y, 'assets/enemy.png'))
        self.hero = hero.Hero("Conan", 50, 80, "assets/hero.png")
        #self.music = music.Music("assets/bg.mp3")
        self.all_sprites = pygame.sprite.Group((self.hero,) + tuple(self.enemies))
        self.state = "GAME"
      #music
      


    '''
    this function initializes pygame, sets up screen, sets bg color, and creates sprite group for enemt
    args: (self)- needs to be used to call atributtes (width)- set for the width of the displsy  (height)- height of the display baclground
    return None
    '''

  
    def mainLoop(self):
        while True:
            if(self.state == "GAME"):
                self.gameLoop()
                
            elif(self.state == "GAMEOVER"):
                self.gameOver()

    '''
    this function sets the function required to make sure your playing the game whe its over 
    args: (self)- needs to be used to call atributtes
    return None
    '''
        

    def gameLoop(self):
        source = audio.play_file('assets/bg.mp3')

        while True:
          pass 
          
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if(event.key == pygame.K_UP):
                        self.hero.move_up()
                    elif(event.key == pygame.K_DOWN):
                        self.hero.move_down()
                    elif(event.key == pygame.K_LEFT):
                        self.hero.move_left()
                    elif(event.key == pygame.K_RIGHT):
                        self.hero.move_right()

            # check for collisions
            fights = pygame.sprite.spritecollide(self.hero, self.enemies, True)
            if(fights):
                for e in fights:
                    if(self.hero.fight(e)):
                        e.kill()
                        self.background.fill((250, 250, 250))
                    else:
                        self.background.fill((250, 0, 0))
                        self.enemies.add(e)

            # redraw the entire screen
            self.enemies.update()
            self.screen.blit(self.background, (0, 0))
            if(self.hero.health == 0):
                self.state = "GAMEOVER"
            self.all_sprites.draw(self.screen)

            # update the screen
            pygame.display.flip()


      


    '''
    gameloop is the game itself these are where the programmer sets the keys and conditions such as gameover
    args: (self)- needs to be used to call atributtes
    return None
    '''

    def gameOver(self):
        self.hero.kill()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


    '''
    this function is for events - to show text in screen when player is dead 
    args: (self)- needs to be used to call atributtes
    return None
    '''