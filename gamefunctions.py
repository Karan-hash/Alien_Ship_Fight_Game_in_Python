# It is used to manage events separately from other aspects of game
import sys

import pygame
from time import *
# Responding to a Keypress
'''
Each keypress is registered as a KEYDOWN event.
When a KEYDOWN event is detected, we need to check whether the key
that was pressed is one that triggers a certain event.
If right arrow key is pressed, we increase the ship’s rect.centerx value to
move the ship to the right
'''
from Bullet import Bullet
from Alien import Alien
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # Respond to keypresses.

    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullets(event, ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q: #Let’s quickly add a keyboard shortcut to end the game when the user presses Q
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
def check_events(ai_settings, screen, ship, bullets, play_button, game_stats, aliens, sb):
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type ==pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() 
            check_play_button(ai_settings, screen, ship, aliens, bullets, game_stats, play_button, mouse_x, mouse_y, sb)

def check_play_button(ai_settings, screen, ship, aliens, bullets, game_stats, play_button, mouse_x, mouse_y, sb):
    # Starts a new game when player clicks play. 
    # Set the game to start only when game_active is False:
    ''' The flag button_clicked stores a True or False value u, and the game
will restart only if Play is clicked and the game is not currently active v. '''
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not game_stats.game_active:

        ai_settings.initialize_dynamic_settings()
        #Hide the mouse cursor 
        pygame.mouse.set_visible(False) #It tells to hide the cursor when the mouse is over the game window
        # Reset the game statistics 
        game_stats.reset_stats()
        game_stats.game_active = True


        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        #Empty the aliens and bullets
        aliens.empty()
        bullets.empty()

        #Create a new fleet of alien and make ship at the center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
#Update Screen Function
def update_screen(ai_settings, screen, ship, aliens, bullets, game_stats, play_button, sb):
    """Update images on screen and flip to the new screen."""
    # Redraw all bullets behind ship and aliens.
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    #Make the most recently drawn screen visible 
    # Draw the play button if is in inactive state 
    # Draw the score information.
    sb.show_score()
    if not game_stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

''' Repopulating the Fleet
One key feature of Alien Invasion is that the aliens are relentless: every time
the fleet is destroyed, a new fleet should appear. 
To make a new fleet of aliens appear after a fleet has been destroyed, first
check to see whether the group aliens is empty. If it is, we call create_fleet().
We’ll perform this check in update_bullets() because that’s where individual
aliens are destroyed. '''
def check_bullet_alien_collision(ai_settings, screen, ship, aliens , bullets, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_highScores(stats, sb)

    #print(len(bullets)) 
    if len(aliens)==0: #If aliens grp is empty
        # Destroy existing bullets and creat new fleet 
        bullets.empty()
        ai_settings.increase_speed()

        #Increase the level
        stats.level += 1 
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)
def update_bullets(bullets, aliens, ai_settings, screen,ship, stats, sb):
    ''' Update position of bullets and get rid of old bullets'''
    # Update bullet positions

    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)

    ''' The sprite.groupcollide() method compares each bullet’s rect with each
alien’s rect and returns a dictionary containing the bullets and aliens that
have collided. Each key in the dictionary is a bullet, and the corresponding
value is the alien that was hit. 
The new line we added loops through each bullet in the group bullets
and then loops through each alien in the group aliens. Whenever the rects
of a bullet and alien overlap, groupcollide() adds a key-value pair to the dictionary
it returns. The two True arguments tell Pygame whether to delete
the bullets and aliens that have collided.
'''
    #Detecting collisions
    check_bullet_alien_collision(ai_settings, screen, ship, aliens, bullets, stats, sb)


def fire_bullets(event, ai_settings, screen, ship, bullets):
    #Limit the number of bullets
    if len(bullets) < ai_settings.bullets_allowed:
            #Create a new bullet and add it to the bullets group
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
'''def get_number_of_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - 3*(alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows   '''     
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 
def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height -
                            (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien, and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x

    aliens.add(alien)
      
def create_fleet(ai_settings, screen, ship, aliens):
    # Create a full fleet of aliens.
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.

    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    ''' Adding Rows
To finish the fleet, determine the number of rows that fit on the screen
and then repeat the loop (for creating the aliens in one row) that number
of times. To determine the number of rows, we find the available vertical
space by subtracting the alien height from the top, the ship height from the
bottom, and two alien heights from the bottom of the screen: '''
    for row_no in range(number_rows):
        #Create an Alien and place it in a row
        for alien_no in range(number_aliens_x):

            create_alien(ai_settings,screen,aliens,alien_no, row_no)
def check_fleet_edges(ai_settings,aliens):
    #Respond appropriately if aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():

            change_fleet_direction(ai_settings, aliens)
            break  
def change_fleet_direction(ai_settings, aliens):
    # Drop the entire fleet and change the fleet direction
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.fleet_drop_speed 
    ai_settings.fleet_direction *= -1
def ship_hit(ai_settings, game_stats, bullets, aliens, ship, screen, sb):
    #Responding to ship being hit by alien 
    #Decreasing ship count 
    if game_stats.ship_left>0:
        game_stats.ship_left -=1
        sb.prep_ships()


        #Empty the list of aliens and bullets 
        aliens.empty()
        bullets.empty() 
        #Creating new fleet and ship at the centre 
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)
    else:
        game_stats.game_active = False
        pygame.mouse.set_visible(True)
def check_aliens_bottom(ai_settings, game_stats, screen, ship, aliens, bullets, sb):
    ''' Checking if any aliens have reached the bottom of the screen. ''' 
    screen_rect = screen.get_rect() 
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #Treat this the same as if ship got hit 
            ship_hit(ai_settings, game_stats, bullets, aliens, ship, screen, sb)
            break
def update_aliens(ai_settings,aliens,ship, game_stats, bullets, screen, sb):
    """Update the postions of all aliens in the fleet."""
    """
Check if the fleet is at an edge,
and then update the postions of all aliens in the fleet.
"""
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

    #Look for alien sheep collisions 
    '''
    The method spritecollideany() takes two arguments: a sprite and a
group. The method looks for any member of the group that’s collided with
the sprite and stops looping through the group as soon as it finds one member
that has collided with the sprite. Here, it loops through the group aliens
and returns the first alien it finds that has collided with ship. '''
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, game_stats, bullets, aliens,ship, screen, sb)
    #Look for aliens hitting the bottom of the screen 
    check_aliens_bottom(ai_settings, game_stats, screen, ship, aliens, bullets, sb)

def check_highScores(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()