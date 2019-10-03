'''
1. The line pygame.init() initializes background settings that Pygame needs to work properly.
2. We call pygame.display.set_mode() to create a display window called screen, on which we’ll draw all of the game’s graphical 
elements.
3. The argument (800, 800) is a tuple that defines the dimensions of the game window. By passing these dimensions to 
pygame.display.set_mode(), we create a game window 800 pixels wide by 800 pixels high.
4. The screen object is called a surface. A surface in Pygame is a part of the screen where you display a game element. Each 
element in the game, like the aliens or the ship, is a surface. The surface returned by display.set_mode() represents the entire 
game window.
5. The game is controlled by a while loop w that contains an event loop and code that manages screen updates. An event is an 
action that the user performs while playing the game, such as pressing a key or moving the mouse. To make our program respond to 
events, we’ll write an event loop to listen for an event and perform an appropriate task depending on the kind of event that 
occurred.
6. For loop is an event loop.
7. To access the events detected by Pygame, we’ll use the pygame.event.get() method. Any keyboard or mouse event will cause the 
for loop to run. Inside the loop, we’ll write a series of if statements to detect and respond to specific events. For example, 
when the player clicks the game window’s close button, a pygame.QUIT event is detected and we call sys.exit() to exit the game.
8. The call to pygame.display.flip() at z tells Pygame to make the most recently drawn screen visible. In this case it draws an 
empty screen each time through the while loop to erase the old screen so that only the new screen is visible. When we move the 
game elements around, pygame.display.flip() will continually update the display to show the new positions of elements and
hide the old ones, creating the illusion of smooth movement.
9. run the run_game function
'''
import pygame
from pygame.sprite import Group
from Game_All_Settings import Settings
from Ship_File import Ship
import gamefunctions as gf
from Game_Statistics import GameStatistics
from Buttons import Button
from Score_Board import ScoreBoard
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    
    game_set = Settings() #Making an instance of settings class
    
    screen = pygame.display.set_mode((game_set.screen_width, game_set.screen_height)) # Here screen has been created
    
    pygame.display.set_caption("Alien Ship Fight Game")
    
    ship_set = Ship(game_set, screen) #Making an instance of Ship class
    
    #Creating an instance to store the game_statistics 
    game_stats = GameStatistics(game_set)

    # # Create an instance to store game statistics and create a scoreboard.
    sb = ScoreBoard(game_set,screen,game_stats)
    #Make a group to store bullet
    bullets = Group()

    play_button = Button(game_set,screen, "Play")
    '''
    Creating Rows of Aliens
    To create a row, first create an empty group called aliens in alien_invasion.py
    to hold all of our aliens, and then call a function in game_functions.py to
    create a fleet. '''
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(game_set,screen,ship_set,aliens)
    
    # Set the background color
    
    #bg_color = (246, 221, 204)
    
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gf.check_events(game_set,screen, ship_set, bullets, play_button, game_stats, aliens, sb)
        if game_stats.game_active:

                ship_set.update()
                gf.update_bullets(bullets, aliens, game_set,screen,ship_set, game_stats, sb )
                #In the main while loop we will update the position of each alien as well 
                gf.update_aliens(game_set,aliens , ship_set, game_stats, bullets, screen, sb)
        gf.update_screen(game_set, screen, ship_set, aliens, bullets, game_stats, play_button, sb)
        
run_game()

# Here we’re importing the new Alien class and creating an instance of
# Alien just before entering the main while loop. Because we’re not changing
# the alien’s position yet, we aren’t adding anything new inside the loop; however,
# we do modify the call to update_screen() to pass it the alien instance.
