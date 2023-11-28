import pygame
import math

pygame.init()

screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('circles')

# Colors
WHITE  = (255,  255,    255)
BLACK  = (0,    0,      0)
RED    = (255,  0,      0)
GREEN  = (0,    255,    0)
BLUE   = (0,    0,      255)
PURPLE = (128,  0,      128)
ORANGE = (255,  165,    0)

def concentric_circles(x_location = screen_width/2, y_location = screen_height/2, radius = 100, circle_count = 5, radii_varity = 15):
    for i in range (circle_count):
        pygame.draw.circle(screen, BLACK, (x_location, y_location), radius-(radii_varity*i), 5)

running = True
while running:
    screen.fill(WHITE)

    concentric_circles()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
