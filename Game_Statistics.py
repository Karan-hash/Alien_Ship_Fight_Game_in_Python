class GameStatistics():
    # Keeping track of alien ship hit 
    def __init__(self, ai_settings):
        #Initializing 
        self.ai_settings = ai_settings 
        
        self.reset_stats()

        # Start File1 in active state 
        
        self.game_active = False

        #Keeping track of high score
        self.high_score =0

    def reset_stats(self):
        #Initialize the statistics that can change during game 
        self.ship_left = self.ai_settings.ship_limit
        # To reset the score each time a new game starts, we initialize score in reset_stats()
        self.score = 0 
        self.level = 1