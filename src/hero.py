import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
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
        self.name = name
        self.speed = 3
        self.health = 3


    '''
    this function initializes the enemy
    args: (self)- needs to be used to call atributtes (name) - unsure of what dies does 
  (x)- assigned x coordinate for the rect of the hero 
  (y)- assigned y coordinate for the rect of the hero 
  (img_file) - imports the image of the hero from another file into the screen 
    return None
    '''

      

    #methods to make moving our hero easier
    def move_up(self):
        self.rect.y -= self.speed

    '''
    this function sets the screen action for the player y coordinate to go up
    args: (self)- needs to be used to call atributtes 
    return None
    '''
      
    def move_down(self):
        self.rect.y += self.speed

    '''
    this function sets the screen action for the player y coordinate to go down 
    args: (self)- needs to be used to call atributtes 
    return None
    '''
  
    def move_left(self):
        self.rect.x -= self.speed

    '''
    this function sets the screen action for the player x coordinate to go left
    args: (self)- needs to be used to call atributtes 
    return None
    '''
      
    def move_right(self):
        self.rect.x += self.speed

    '''
    this function sets the screen action for the player x coordinate to go right
    args: (self)- needs to be used to call atributtes 
    return No

    '''
  
    def fight(self, opponent):
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True

    '''
    this function sets the life of the hero if health decreases and prints wether or not attached failed or was a sucess
    args: (self)- needs to be used to call atributtes (opponent) - unsure of how this is used
    return boolean 
    '''