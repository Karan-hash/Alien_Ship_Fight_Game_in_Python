class Settings():
    
    def __init__(self):
        #Initialize the game settings and addings bullet settings
        
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        # Limiting the Number of Bullets
        self.bullets_allowed = 10

        #Alien Settings for moving the aliens right
        self.alien_speed_factor = 1

        #Now we’ll create the settings that will make the fleet move down the screen
        #and to the left when it hits the right edge of the screen.
        self.fleet_drop_speed = 70

        # How quickly the game speeds up and Levelling up
        self.speedup_scale = 1.1

        # How quickly the alien point value increases as we move to next level
        self.score_scale = 1.5

        # we call initialize_dynamic_settings() to initialize
        # the values for attributes that need to change throughout the course of a game v.
        self.initialize_dynamic_settings()

        # Fleet direction of 1 represents right and -1 represents left 
        self.fleet_direction = 1
        
    '''To make an instance of Settings and use it to access our settings, modify Project_description run_game
    method. '''
    def initialize_dynamic_settings(self):
        #Initialize the settings that change through out the game 
        self.ship_speed_factor = 1.5 
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1 

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring for every alien hit
        # To write a live score to the screen, we update the value of stats.score whenever
        # an alien is hit, and then call prep_score() to update the score image.

        # We’ll increase the point value of each alien as the game progresses. To
        # make sure this point value is reset each time a new game starts, we set the
        # value in initialize_dynamic_settings().
        self.alien_points = 10
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points*self.score_scale)
        print(self.alien_points)