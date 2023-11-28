import pygame
import random
import sys

pygame.init()
pygame.mixer.init() # Initialize the mixer module

screen_width  = 800
screen_height = 600

# Screen setup
screen = pygame . display . set_mode ((screen_width , screen_height) )
pygame . display . set_caption ('Text-Animation-and-Sound-Effects')

pygame.font.init()
font = pygame.font.SysFont('freesansbold ', 36)

text = font.render("Hello , Pygame!", True , (0, 0, 255))
text_location_x = 400 - text.get_width () // 2
text_location_y = 300 - text.get_height () // 2
text_speed_x = 0.02
text_speed_y = 0.015

# Load sound effect and background music
running = True
coin_sound = pygame.mixer.Sound('coin_effect.wav')
pygame.mixer.music.load('game_background_music.mp3')

# Play background music on loop
pygame.mixer.music.play(-1)
pygame.mixer.music.set_valume(0.5)

running = True
while running :
    for event in pygame . event . get () :
        if event . type == pygame . QUIT :
            running = False

    text_location_x += text_speed_x
    text_location_y += text_speed_y

    if text_location_x + text.get_width() >= screen_width or text_location_x < 0:
        text_speed_x *= -1 
        coin_sound.play()
        text = font.render("Hello , Pygame!", True , (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    if text_location_y + text.get_height() >= screen_height or text_location_y < 0:
        text_speed_y *= -1
        coin_sound.play() 
        text = font.render("Hello , Pygame!", True , (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    screen . fill ((0, 0, 0))

    screen.blit(text, (text_location_x, text_location_y))
    

    pygame.display.update()

pygame . mixer . music . stop () # Stop background music
pygame . quit ()
sys . exit ()