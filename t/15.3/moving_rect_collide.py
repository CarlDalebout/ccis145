import pygame
import random
import sys

pygame.init()
pygame.mixer.init() # Initialize the mixer module

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

# set up the window
screen = pygame.display.set_mode((screen_width, screen_height) , 0 , 32)
pygame.display.set_caption('moving_rect_collide')

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

player_rect = pygame.Rect(random.randint(50, screen_height-50), random.randint(50, screen_width-50), 50, 50)
rect_speed = 2

static_rect = pygame.Rect(screen_width/2 - 50, screen_height/2 - 50, 100, 100)
static_rect_color = (0, 0, 255)

coin_sound = pygame.mixer.Sound('coin_effect.wav')

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()

while True :
    screen.fill((255, 255, 255))

    if up_pressed and down_pressed:
        {}
    elif up_pressed:
        player_rect.y -= rect_speed
    elif down_pressed:
        player_rect.y += rect_speed
    else:
        {}

    if left_pressed and right_pressed:
        {}
    elif left_pressed:
        player_rect.x -= rect_speed
    elif right_pressed:
        player_rect.x += rect_speed
    else:
        {}

    if player_rect.colliderect(static_rect):
        coin_sound.play()
        static_rect_color = (255, 0, 0)
        if(player_rect.bottom >= static_rect.top and player_rect.top < static_rect.top):
            player_rect.y -= rect_speed
        if(player_rect.top <= static_rect.bottom and player_rect.bottom > static_rect.bottom):
            player_rect.y += rect_speed
        if(player_rect.left <= static_rect.right and player_rect.right > static_rect.right):
            player_rect.x += rect_speed
        if(player_rect.right >= static_rect.left and player_rect.left < static_rect.left):
            player_rect.x -= rect_speed
    else:
        static_rect_color = (0, 0, 255)

    if player_rect.right >= screen_width:
        player_rect.x = screen_width - player_rect.width
    if player_rect.left < 0:
        player_rect.x = 0
    if player_rect.bottom >= screen_height:
        player_rect.y = screen_height - player_rect.height
    if player_rect.top < 0:
        player_rect.y = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
            if event.key == pygame.K_RIGHT:
                right_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False

        if event . type == pygame . MOUSEBUTTONDOWN :
            # A mouse button has been pressed
            if event . button == 1:
                rect_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    pygame.draw.rect(screen, (0, 0, 255), player_rect)
    pygame.draw.rect(screen, static_rect_color, static_rect)

    pygame.display.update()

    # Ensure the loop runs
    fpsClock.tick( FPS )
