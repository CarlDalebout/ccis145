"""
    This Module will contain all the globals for the final projuct 
    such as what buttons are being pushed, Images, Music, and Sounds
Carl Dalebout - 2023
"""

import pygame, sys

# PATHS
global IMAGE_PATH

IMAGE_PATH = "Images"

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
global SPEED_DELTA
global OFF_SCREEN

GAME_CLOCK      = 0
FRAME_RATE      = 30
SCREEN_SIZE     = (1080, 860)
MAIN_SCREEN     = pygame.Rect( 0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1] - 128 )
OFF_SCREEN      = (-200, -200)

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