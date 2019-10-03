import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    def __init__(self, ai_settings, screen):
        # Initialize the alien and set its starting position
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Loading the image and set its rect attribute

        self.image = pygame.image.load('S:\JP_MORGAN_Python_PROJECTS\MY_ALIEN_PROJECT\images/alien.bmp')
        self.rect = self.image.get_rect()

        #Start each position at top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien exact position
        self.x = float(self.rect.x)

    def check_edges(self):
        screen_rect =self.screen.get_rect()

        if self.rect.right >= screen_rect.right:
            return True 
        elif self.rect.left <= 0:
            return True

    def update(self):
        # Move the alien right 
        ''' Each time we update an alien’s position, we move it to the right by the
amount stored in alien_speed_factor. We track the alien’s exact position
with the self.x attribute, which can hold decimal values u. We then use
the value of self.x to update the position of the alien’s rect v. ''' 
#Move the alien left or right  according to fleet direction
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x 
    
     

    def blitme(self):
        '''Draw the alien at its current location.'''
        self.screen.blit(self.image, self.rect)

# Creating an instance of the Alien in new file = 'File1.py' and Making the Alien Appear Onscreen .
# To make the alien appear onscreen, we call its blitme() method in update_screen().  