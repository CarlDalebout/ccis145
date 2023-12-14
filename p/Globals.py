"""
    This Module will contain all the globals for the final projuct 
    such as what buttons are being pushed, Images, Music, and Sounds
Carl Dalebout - 2023
"""

import pygame, sys, os

# PATHS
global IMAGE_PATH
global SOUND_PATH
global MUSIC_PATH

IMAGE_PATH = "Images"
SOUND_PATH = "Sounds"
MUSIC_PATH = "Music"

# Default Key list
global P_FORWARD     
global P_BACKWARD    
global P_STRAFT_LEFT 
global P_STRAFT_RIGHT
global P_TURN_LEFT   
global P_TURN_RIGHT  
global P_FIRE_MAIN   
global PLAYER_KEYS   

P_FORWARD       = 0
P_BACKWARD      = 1
P_STRAFE_LEFT   = 2
P_STRAFE_RIGHT  = 3
P_TURN_LEFT     = 4
P_TURN_RIGHT    = 5
P_FIRE_MAIN     = 6
PLAYER_KEYS     = 7

PLAYER_KEYS = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_LEFT, pygame.K_RIGHT,]

# CONSTANTS
global GAME_CLOCK
global FRAME_RATE
global SCREEN_SIZE
global MAIN_SCREEN
global PLAYER_SPEED
global OFF_SCREEN

GAME_CLOCK      = 0
FRAME_RATE      = 30
SCREEN_SIZE     = (1080, 860)
MAIN_SCREEN     = pygame.Rect( 0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1] - 128 )
PLAYER_SPEED    = 5
OFF_SCREEN      = (-200, -200)

# CONST Icons
global MENU_BACKGROUND_ICON
global GAME_BACKGROUND_ICON
global PLAYER_SHIP_ICON
global ASTEROID_ICON
global LAZER_ICON

MENU_BACKGROUND_ICON    = pygame.image.load(os.path.join(IMAGE_PATH, "Main_Menu.png"))
GAME_BACKGROUND_ICON    = pygame.image.load(os.path.join(IMAGE_PATH, "BackGround.png"))
PLAYER_SHIP_ICON        = pygame.image.load(os.path.join(IMAGE_PATH, "Player_Ship2.png"))
ASTEROID_ICON           = pygame.image.load(os.path.join(IMAGE_PATH, "Asteroid_Brown.png"))
LAZER_ICON              = pygame.image.load(os.path.join(IMAGE_PATH, "Lazer.png"))

# COLOR CONSTANTS
global RED
global GREEN
global BLUE
global CYAN
global PURPLE
global YELLOW
global BLACK
global WHITE

RED             = ( 255,   0,   0 )
GREEN           = (   0, 255,   0 )
BLUE            = (   0,   0, 255 )
CYAN            = (   0, 255, 255 )
PURPLE          = ( 255,   0, 255 )
YELLOW          = ( 255, 255,   0 )
BLACK           = (   0,   0,   0 )
WHITE           = ( 255, 255, 255 )