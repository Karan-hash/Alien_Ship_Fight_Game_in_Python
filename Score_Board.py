# To display the score on the screen, we first create a new class, Scoreboard. For
# now this class will just display the current score, but we’ll use it to report
# the high score, level, and number of ships remaining as well.
import pygame.font
from pygame.sprite import Group

from Ship_File import Ship
class ScoreBoard():
    def __init__(self, ai_settings, screen, stats):
        self.ai_settings = ai_settings
        self.screen = screen
        self.stats = stats
        self.screen_rect = screen.get_rect()

        # # Font settings for scoring information.
        self.text_color = (45, 45, 45)
        self.font = pygame.font.SysFont(None, 48)

        # # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):

        #Turn the score into an rendered image
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #Display the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        higher_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(higher_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
    def prep_level(self):
        """Turn the level into a rendered image."""
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10    
    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
    def show_score(self):
        # Draw score to the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        # Draw ships.
        self.ships.draw(self.screen)
        # This method draws the score image to the screen at the location specified
# by score_rect.

'''
Because Scoreboard writes text to the screen, we begin by importing the
pygame.font module. Next, we give __init__() the parameters ai_settings,
screen, and stats so it can report the values we’re tracking u. Then, we set a
text color v and instantiate a font object w.
To turn the text to be displayed into an image, we call prep_score() 
We’ll position the score in the upper-right corner of the screen and
have it expand to the left as the score increases and the width of the number
grows. To make sure the score always lines up with the right side of the
screen, we create a rect called score_rect w and set its right edge 20 pixels
from the right screen edge x. We then place the top edge 20 pixels
down from the top of the screen y. '''

'''
Making a Scoreboard
To display the score, we’ll create a Scoreboard instance in alien_invasion.py: '''


