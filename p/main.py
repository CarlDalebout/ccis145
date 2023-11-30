# Import the pygame module
import pygame, random
from Globals import *

# Initialize pygame
pygame.init()

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

player_rect = pygame.Rect(random.randint(50, SCREEN_SIZE[1]-50), random.randint(50, SCREEN_SIZE[0]-50), 50, 50)
player_image = pygame.image.load('')
rect_speed = 2

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()

def keyboard(event_list):
    for event in event_list:
        # Check for QUIT event. If QUIT, then set running to false.
        if event.type == QUIT:
            running = False
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                w_pressed = True
            if event.key == pygame.K_s:
                s_pressed = True
            if event.key == pygame.K_a:
                a_pressed = True
            if event.key == pygame.K_d:
                d_pressed = True
            if event.key == pygame.K_SPACE:
                space_pressed = True
            if event.key == pygame.K_LEFT: 
                left_pressed = True
            if event.key == pygame.K_RIGHT:
                right_pressed = True

def update():
    if PLAYER_KEYS[0] and PLAYER_KEYS[1]:
        {}
    elif PLAYER_KEYS[0]:
        player_rect.y -= rect_speed
    elif PLAYER_KEYS[1]:
        player_rect.y += rect_speed
    else:
        {}

    if PLAYER_KEYS[2] and PLAYER_KEYS[3]:
        {}
    elif player_rect[2]:
        player_rect.x -= rect_speed
    elif player_rect[3]:
        player_rect.x += rect_speed
    else:
        {}

    if PLAYER_KEYS[5] and PLAYER_KEYS[6]:
        {}
    elif PLAYER_KEYS[5]:
        {}
    elif PLAYER_KEYS[6]:
        {}

# Variable to keep the main loop running
running = True
# Main loop
while running:
    # for loop through the event queue
    keyboard(pygame.event.get())
    update()

    # Fill the screen with black
    screen.fill((0, 0, 0))


    # Update the display
    pygame.display.update()

    # Ensure the loop runs
    fpsClock.tick( FPS )
