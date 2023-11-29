import pygame
import math
import random

pygame.init()

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

screen_width  = 800
screen_height = 600

# set up the window
screen = pygame.display.set_mode((screen_width, screen_height) , 0 , 32)
pygame.display.set_caption('line_motion')

RED   = (255 ,   0 ,   0)
WHITE = (255 , 255 , 255)
BLUE  = (0   ,   0 , 255)

red_circle_speed = 5
red_rect = pygame.Rect(0, screen_height - 25, 25, 25)

blue_rect_speed = 10
blue_rect = pygame.Rect(random.randint(75, screen_width), random.randint(0, screen_height-100), 75, 75)

def reset():
    red_rect.x = 25 
    red_rect.y = screen_height - 25
    blue_rect.x = random.randint(75, screen_width - 75)
    blue_rect.y = random.randint( 0, screen_height - 100)

def get_vec(orgin_x, orgin_y, destination_x, destination_y):
    vec_x = destination_x - orgin_x
    vec_y = destination_y - orgin_y
    normal_scaler = math.sqrt(pow(vec_x, 2) + pow(vec_y, 2))
    vec_x /= normal_scaler
    vec_y /= normal_scaler
    vec_x *= red_circle_speed
    vec_y *= red_circle_speed
    return vec_x, vec_y

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
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

    if up_pressed and down_pressed:
        {}
    elif up_pressed:
        blue_rect.y -= blue_rect_speed
    elif down_pressed:
        blue_rect.y += blue_rect_speed

    if left_pressed and right_pressed:
        {}
    elif left_pressed:
        blue_rect.x -= blue_rect_speed
    elif right_pressed:
        blue_rect.x += blue_rect_speed

    x_offset, y_offset = get_vec(red_rect.x, red_rect.y, blue_rect.x, blue_rect.y)
    red_rect.x += x_offset
    red_rect.y += y_offset

    if red_rect.colliderect(blue_rect):
        reset()

    

    screen.fill( WHITE )
    pygame.draw.circle(screen, RED, (red_rect.x, red_rect.y), 25)
    pygame.draw.circle(screen, BLUE, (blue_rect.x, blue_rect.y), 75)

    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )
