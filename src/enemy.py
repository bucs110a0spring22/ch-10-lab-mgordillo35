import pygame
import random
#model
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    '''
    this function initializes the enemy
    args: (self)- needs to be used to call atributtes (name) - unsure of what dies does 
  (x)- assigned x coordinate for the rect of the enemy 
  (y)- assigned y coordinate for the rect of the enemy 
  (img_file) - imports an image from another file into the screen 
    return None
    '''



  
    def update(self):
      changeCord = random.randrange(-1, 2) #from -1 to 1
      self.rect.x += changeCord
      self.rect.y += changeCord
      
      #print("'Update me,' says " + self.name)

    '''
    this function allows the rect enemy to move around randomly in the screen 
    args: (self)- needs to be used to call atributtes
    return None
    '''