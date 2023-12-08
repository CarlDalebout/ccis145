# Import the pygame module
import pygame, random, os, math
import Asteroid_Sprite, Lazer_Sprite, Player_Sprite
from Globals import *

# Initialize pygame
pygame.init()
pygame.mixer.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    MOUSEBUTTONDOWN,
    QUIT,
)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
pygame.display.set_caption("final Project")

menu_screen_back_ground = pygame.transform.scale(MENU_BACKGROUND_ICON, (SCREEN_SIZE[0], SCREEN_SIZE[1]))
menu_screen_back_ground_rect = menu_screen_back_ground.get_rect()
menu_screen_back_ground_rect.x = 0
menu_screen_back_ground_rect.y = 0

game_screen_back_ground = pygame.transform.scale(GAME_BACKGROUND_ICON, (SCREEN_SIZE[0], SCREEN_SIZE[1]))
game_screen_back_ground_rect = game_screen_back_ground.get_rect()
game_screen_back_ground_rect.x = 0
game_screen_back_ground_rect.y = 0

pygame.mixer.music.load(os.path.join(MUSIC_PATH, "Music.mp3"))
pygame.mixer.music.play(-1)

# Creating image for the player ship
player = Player_Sprite.Player_Ship(screen, "Player", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))

# creating the list for the Asteroids
Test_Asteroids = ["filler", Asteroid_Sprite.Asteroid(screen, "test", (SCREEN_SIZE[0]/2, 0))]
Asteroids_max = 5
# 

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()

def rotate_image(image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = pos).center)
    
    screen.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(screen, (255, 0, 0), new_rect, 2)
    return rotated_image, new_rect 



insFont = pygame.font.SysFont("Courier New", 20)
insLabels = []
instructions = (
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
"                                   Asteroid                                    ",
"-------------------------------------------------------------------------------",
"",
"                           --== Instructions: ==--                             ",
"  This is a game that involves a carriar ship lost in space having to survive  ",
"                the onslaught of asteroids to drop off its cargo               ",    
"",
"",
"                              --== Weapon ==--                                 ",
"      The Ship is equipped is a powerfull lazer capable of blasting appart     ",
"                         asteroids with one shot how lucky                     ",
"",
"",
"                           --== Default Controls ==--                          ",
"           MOVE_UP   MOVE_DOWN   MOVE_LEFT  MOVE_RIGHT   Fire                  ",
"               W         S           A          D        Space                 ",
"",
"",
"                       <<< Press any button to start >>>                       "
)
for line in instructions:
    tempLabel = insFont.render(line, 1, GREEN )
    insLabels.append(tempLabel)

# Intro
running = True
while running: 

    # checking if the player pushes a button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            else:
                running = False
    """
        Printing of the Main Menu
    """
    # screen.fill(0, 0, 0)
    screen.blit(menu_screen_back_ground, menu_screen_back_ground_rect)

    for i in range(len(insLabels)):
        screen.blit(insLabels[i], (50, 100+( 20*i ) ))
           
    pygame.display.update()
        # Ensure the loop runs
    fpsClock.tick( FPS )

# Main Game
death_counter = 0
font = pygame.font.SysFont('freesansbold', 36)
# Variable to keep the main loop running
running = True
# Main loop
while running:

    # check for player pushing buttons
    player.scan_keys()
    # moving player location and checking to firing of lazers
    player.update()
    text = font.render(f"Killed Asteroids: {Asteroids_max-5}", True , YELLOW)
    #spawning asteroids
    
    spawn_rate = 16 +len(Test_Asteroids) - (Asteroids_max//10) #// Asteroids_max
    
    if spawn_rate < 1:
        spawn_rate = 1
    if random.randint(0, spawn_rate) == spawn_rate:
        if len(Test_Asteroids) <= Asteroids_max:
            rag_angle = random.randint(0, 360) * 3.1415 / 180

            asteroid_x = math.cos(rag_angle)
            asteroid_y = math.sin(rag_angle)
            
            M = max(abs(asteroid_x), abs(asteroid_y))
            asteroid_x = (SCREEN_SIZE[0] * asteroid_x / M) 
            asteroid_y = (SCREEN_SIZE[0] * asteroid_y / M)
            Test_Asteroids.append(Asteroid_Sprite.Asteroid(screen, "Bolder", (asteroid_x, asteroid_y), random.randint(63, 255)))

    # moving asteroids
    for index in range(len(Test_Asteroids)-1, 0, -1):
        Test_Asteroids[index].update(player.rect.x, player.rect.y)
    
    # moving lazers
    for index in range (len(player.projectile_list)-1, 0, -1):
        if player.projectile_list[index].update() == "OutOfBounds":
            player.projectile_list.remove(player.projectile_list[index])
            
    # checking collision of Asteroids and lazers
    for i in range (len(Test_Asteroids)-1, 0, -1):
        for j in range (len(player.projectile_list)-1, 0, -1):
            if(Test_Asteroids[i].rect.colliderect(player.projectile_list[j].rect)):
                player.projectile_list.remove(player.projectile_list[j])
                Test_Asteroids.remove(Test_Asteroids[i])
                Asteroids_max += 1

    # Checkig for collison of Asteroids and the player
    for i in range (len(Test_Asteroids)-1, 0, -1):
        if Test_Asteroids[i].rect.colliderect(player.rect):
            print(f"you have died {death_counter} times")
            death_counter += 1
            if death_counter >= 20:
                running = False

    """
        printing the screen the the player sees
    """
    # Fill the screen with black
    screen.fill((0, 0, 0))
    
    # Dipslay the Background icon
    screen.blit(game_screen_back_ground, game_screen_back_ground_rect)

    # printing of the player
    rotate_image(pygame.transform.scale(player.icon, (63, 63)), (player.rect.x, player.rect.y), player.angle)
    # screen.blit(player.icon, player.rect.topleft)

    # printing of the lazers
    for index in range (len(player.projectile_list)):
        screen.blit(player.projectile_list[index].icon, player.projectile_list[index].rect.topleft)

    # printing of the asteroids
    for index in range (len(Test_Asteroids)-1, 0, -1):
        screen.blit(Test_Asteroids[index].icon, (Test_Asteroids[index].rect.x - Test_Asteroids[index].rect.width/2, Test_Asteroids[index].rect.y - Test_Asteroids[index].rect.height/2))
        pygame.draw.rect(screen, (255, 0, 0), Test_Asteroids[index].rect, 2)

    screen.blit(text, (SCREEN_SIZE[0]-(text.get_width() + 5), 0))

    # Update the display
    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )

print("Show the death screen")

insFont = pygame.font.SysFont("Courier New", 20)
insLabels = []
instructions = (
#12345678901234567890123456789012345678901234567890123456789012345678901234567890
"                                   Game Over                                   ",
"-------------------------------------------------------------------------------",
"",
"   Your ship has crashed and your cargo has been scattured throughout space    ",
"",
"  during your fight for your life you managed to destroy those pesky asteroids ",
"",
"",
"                        Lets see how many you destroyed                        ",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
"                       <<< Press any button to start >>>                       "
)

for line in instructions:
        tempLabel = insFont.render(line, 1, GREEN )
        insLabels.append(tempLabel)

text = font.render(f"Killed Asteroids: {Asteroids_max-5}", True , BLUE)

running = True
while running:

    # checking if the player pushes a button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            else:
                running = False

    screen.fill((0, 0, 0))

    for i in range(len(insLabels)):
        screen.blit(insLabels[i], (50, 200+( 20*i )))

    screen.blit(text, (SCREEN_SIZE[0]/2-(text.get_width() + 5)/2, SCREEN_SIZE[1]/2))

    pygame.display.update()
        # Ensure the loop runs
    fpsClock.tick( FPS )


pygame.quit()
