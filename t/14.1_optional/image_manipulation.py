import pygame
import random
import sys
    
pygame.init()
pygame.mixer.init() # Initialize the mixer module

screen_width  = 800
screen_height = 600

# Screen setup
screen = pygame.display.set_mode((screen_width , screen_height))
pygame . display . set_caption ('Text-Animation-and-Sound-Effects')

def rotate_image(image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = pos).center)

    screen.blit(rotated_image, new_rect.topleft)
    pygame.draw.rect(screen, (255, 0, 0), new_rect, 2)
    return rotated_image, new_rect 

def rotate_image_center(image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

    rotated_offset = offset_center_to_pivot.rotate(-angle)

    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

    screen.blit(rotated_image, rotated_image_rect)
    pygame.draw.rect(screen, (255, 0, 0), rotated_image_rect, 2)
    return rotated_image, rotated_image_rect

# Initialize the player image
player_image = pygame.image.load('cat.png')
player_rect = player_image.get_rect()
player_width, player_height = player_image.get_size()
player_x = screen_width/2
player_y = screen_height/2
player_rect.x = player_x
player_rect.y = player_y

r_pressed = False
e_pressed = False

# Initialize a clock object to control frame rate
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

angle = 0
running = True
while running :


    if   r_pressed and e_pressed:
        {}
    elif r_pressed:
        angle -= 5
    elif e_pressed:
        angle += 5

    for event in pygame . event . get () :
        if event . type == pygame . QUIT :
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                r_pressed = True
            if event.key == pygame.K_e:
                e_pressed = True
            if event.key == pygame.K_UP:
                player_image = pygame.transform.scale(player_image, (player_width*2, player_height*2))
                player_width = player_image.get_width()
                player_height = player_image.get_height()
            if event.key == pygame.K_DOWN:
                player_image = pygame.transform.scale(player_image, (player_width*0.5, player_height*0.5))
                player_width = player_image.get_width()
                player_height = player_image.get_height()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                r_pressed = False
            if event.key == pygame.K_e:
                e_pressed = False

    screen.fill((0, 0, 0))

    rotate_image(player_image, (player_x, player_y), angle)

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit ()
sys.exit ()