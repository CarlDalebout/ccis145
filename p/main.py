# Import the pygame module
import pygame, random, os, math
import Asteroid_Sprite, Lazer_Sprite
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

# Createing the lazer sound to uses when the play fires a lazer
lazer_file = os.path.join("Sounds", "laser.mp3")
lazer_sound = pygame.mixer.Sound(lazer_file)

# Creating image for the player ship
png_file = os.path.join("Images", "Player_Ship2.png")
player_image_org = pygame.image.load(png_file)
player_image = pygame.transform.scale(player_image_org, (63, 63))

# creating the rect for the player ship and collision
player_rect = player_image.get_rect()
player_rect.x = SCREEN_SIZE[0]/2-player_rect.width
player_rect.y = SCREEN_SIZE[1]/2-player_rect.height

# features of the ship such as speed, looking angle, fired lazers
player_angle = 0
rect_speed = 5

# Creating projectiles from the ship
player_projectiles = [Lazer_Sprite.Laser(screen, "testLazer2", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1] + 25))]

# creating the list for the Asteroids
Test_Astteroids = [Asteroid_Sprite.Asteroid(screen, "test"), Asteroid_Sprite.Asteroid(screen, "test", (SCREEN_SIZE[0]/2, 0))]
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
                pygame.quit()
            if event.key == pygame.K_w:
                # print("w_pressed")
                PLAYER_KEYS[0] = True
            if event.key == pygame.K_s:
                # print("s_pressed")
                PLAYER_KEYS[1] = True
            if event.key == pygame.K_a:
                # print("a_pressed")
                PLAYER_KEYS[2] = True
            if event.key == pygame.K_d:
                # print("d_pressed")
                PLAYER_KEYS[3] = True
            if event.key == pygame.K_SPACE:
                if len(player_projectiles) <= 5:
                    rag_angle = player_angle * 3.1415 / 180
                    lazer_x = math.cos(rag_angle)
                    lazer_y = math.sin(rag_angle)
                    M = max(abs(lazer_x), abs(lazer_y))
                    lazer_x = (player_rect.width/2 * lazer_x / M)  + player_rect.x
                    lazer_y = (player_rect.height/2 * lazer_y / M) + player_rect.y
                    player_projectiles.append((Lazer_Sprite.Laser(screen, "lazer", (lazer_x, lazer_y), player_angle+90)))
                PLAYER_KEYS[4] = True
            if event.key == pygame.K_LEFT: 
                PLAYER_KEYS[5] = True
            if event.key == pygame.K_RIGHT:
                PLAYER_KEYS[6] = True
        if event.type == KEYUP:
            # If the Esc key is pressed, then exit the main loop
            if event.key == pygame.K_w:
                # print("w_not_pressed")
                PLAYER_KEYS[0] = False
            if event.key == pygame.K_s:
                # print("s_not_pressed")
                PLAYER_KEYS[1] = False
            if event.key == pygame.K_a:
                # print("a_not_pressed")
                PLAYER_KEYS[2] = False
            if event.key == pygame.K_d:
                # print("d_not_pressed")
                PLAYER_KEYS[3] = False
            if event.key == pygame.K_SPACE:
                PLAYER_KEYS[4] = False
            if event.key == pygame.K_LEFT: 
                PLAYER_KEYS[5] = False
            if event.key == pygame.K_RIGHT:
                PLAYER_KEYS[6] = False

def update():
    global player_rect
    global player_image
    global player_angle

    if PLAYER_KEYS[0] == True and PLAYER_KEYS[1] == True:
        {}
    elif PLAYER_KEYS[0] == True:
        # print("moved up")
        player_rect.y -= rect_speed
    elif PLAYER_KEYS[1] == True:
        # print("moved down")
        player_rect.y += rect_speed

    if PLAYER_KEYS[2] == True and PLAYER_KEYS[3] == True:
        # print("2 and 3 are pressed")
        {}
    elif PLAYER_KEYS[2] == True:
        # print("moved left")
        player_rect.x -= rect_speed
    elif PLAYER_KEYS[3] == True:
        # print("moved right")
        player_rect.x += rect_speed

    if PLAYER_KEYS[5] == True and PLAYER_KEYS[6] == True:
        {}
    elif PLAYER_KEYS[5] == True:
        # print("rotated clockwise")
        player_angle += rect_speed
    elif PLAYER_KEYS[6] == True:
        # print("rotated counter_clockwise")
        player_angle -= rect_speed

# Variable to keep the main loop running
running = True
# Main loop
while running:
    # for loop through the event queue
    keyboard(pygame.event.get())
    update()

    lenght = len(Test_Astteroids)
    if random.randint(0, 20) == 20:
        if len(Test_Astteroids) <= Asteroids_max:
            rag_angle = random.randint(0, 360) * 3.1415 / 180
            asteroid_x = math.cos(rag_angle)
            asteroid_y = math.sin(rag_angle)
            M = max(abs(asteroid_x), abs(asteroid_y))
            asteroid_x = (SCREEN_SIZE[0] * asteroid_x / M) 
            asteroid_y = (SCREEN_SIZE[0] * asteroid_y / M)
            Test_Astteroids.append(Asteroid_Sprite.Asteroid(screen, "Bolder", (asteroid_x, asteroid_y)))

    for index in range(len(Test_Astteroids)):
        Test_Astteroids[index].update(player_rect.x, player_rect.y)
    
    for index in range (len(player_projectiles)):
        if player_projectiles[index].update() == "OutOfBounds":
            player_projectiles.pop(index)
            break
    
    for i in range (lenght):
        for j in range (len(player_projectiles)):
            if(Test_Astteroids[i].rect.colliderect(player_projectiles[j].rect)):
                Test_Astteroids.pop(i)
                player_projectiles.pop(j)
                Asteroids_max += 2
                break

    # Fill the screen with black
    screen.fill((0, 0, 0))
    

    rotate_image(pygame.transform.scale(player_image_org, (63, 63)), (player_rect.x, player_rect.y), player_angle)
    # screen.blit(player_image, player_rect.topleft)

    for index in range (len(player_projectiles)):
        screen.blit(player_projectiles[index].icon, player_projectiles[index].rect.topleft)

    for index in range (len(Test_Astteroids)):
        screen.blit(Test_Astteroids[index].icon, Test_Astteroids[index].rect.topleft)


    # Update the display
    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )

pygame.quit()
