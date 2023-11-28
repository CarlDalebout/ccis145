import pygame
import random
import sys

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

screen_width  = 800
screen_height = 600
pygame.display.set_caption('stars')

# set up the window
screen = pygame.display.set_mode((screen_width, screen_height) , 0 , 32)
pygame.display.set_caption('up_down_movement')

i = 0

colors = [(0,    0,      0)
         ,(255,  0,      0)
         ,(0,    255,    0)
         ,(0,    0,      255)
         ,(128,  0,      128)
         ,(255,  165,    0)]

up_pressed = False
down_pressed = False

rect_x = screen_width/2
rect_y = screen_height/2
rect_width = 50
rect_height = 30
rect_speed = 5

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()

while True :
    screen.fill((255, 255, 255))

    if up_pressed and down_pressed:
        {}
    elif up_pressed:
        rect_y -= rect_speed
    elif down_pressed:
        rect_y += rect_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
        if event . type == pygame . MOUSEBUTTONDOWN :
            # A mouse button has been pressed
            if event . button == 1:
                i = random.randint(0, 5)
    
    pygame.draw.rect(screen, colors[i], (rect_x, rect_y, rect_width, rect_height))


    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )
