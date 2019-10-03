# 1. The __init__() method of Ship takes two parameters: the self reference and the screen where we’ll draw the ship.
# 2. To load the image we call pygame.image.load(). This function returns a surface representing the ship, which we store in 
# self.image.
# 3. Once the image is loaded, we use get_rect() to access the surface’s rect attribute v. One reason Pygame is so efficient is 
# that it lets you treat game elements like rectangles (rectangles).
# 4.Treating an element as a rectangle is efficient because rectangles are simple geometric shapes. This approach usually works 
# well enough that no one playing the game will notice that we’re not working with the exact shape of each game element.

# 5. In Pygame, the origin (0, 0) is at the top-left corner of the screen, and coordinates increase as you go down and to the 
# right. On a 1200 by 800 screen, the origin is at the top-left corner, and the bottom-right corner has the coordinates 
# (1200, 800).

# 6.We’ll position the ship at the bottom center of the screen. To do so, first store the screen’s rect in self.screen_rect w, 
# and then make the value of self.rect.centerx (the x-coordinate of the ship’s center) match the centerx attribute of the 
# screen’s rectangle.
# Pygame will use these rect attributes to position the ship image so it’s centered horizontally and aligned with the bottom of 
# the screen.
# 7. At y we define the blitme() method, which will draw the image to the screen at the position specified by self.rectangle.
import pygame
from pygame.sprite import Sprite
# First, we need to make Ship inherit from Sprite so we can create a group of sprites
class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        
        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        
        # Load the ship image and get its rect
        
        self.image = pygame.image.load('S:\JP_MORGAN_Python_PROJECTS\MY_ALIEN_PROJECT\images/ship.bmp')
        
        self.rect = self.image.get_rect()
        
        self.screen_rect = screen.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        
        self.rect.centerx = self.screen_rect.centerx
        
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for ship's center
        self.center = float(self.rect.centerx)

    def update(self):
        
        #Update the ship's position based on the movement flag
        
        if self.moving_right and self.rect.right < self.screen_rect.right : #Check the x coordinate
            
            self.center +=self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left >0:
            self.center -=self.ai_settings.ship_speed_factor

        #Update rect object from self.center
        self.rect.centerx = self.center
    def center_ship(self):
        #Center the ship on the screen
        self.center = self.screen_rect.centerx
    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
