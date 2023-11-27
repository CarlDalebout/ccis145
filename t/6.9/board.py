import pygame
import math

pygame.init()

screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('board')

# Colors
WHITE  = (255,  255,    255)
BLACK  = (0,    0,      0)
RED    = (255,  0,      0)
GREEN  = (0,    255,    0)
BLUE   = (0,    0,      255)
PURPLE = (128,  0,      128)
ORANGE = (255,  165,    0)

def checkerboard(x_location = screen_width/2, y_location = screen_height/2, board_width = 100, board_height = 100, n_squares = 4, dark_square_color = BLACK, light_squre_color = WHITE):

    x_offset = board_width/n_squares
    y_offset = board_height/n_squares

    for i in range (n_squares):
        for j in range (n_squares):
            if((j + i)%2 == 0):
                pygame.draw.polygon(screen, dark_square_color, [(j * x_offset + x_location, i * y_offset + y_location), ((j+1)*x_offset + x_location, i*y_offset + y_location), ((j+1)*x_offset + x_location, (i+1)*y_offset + y_location), (j*x_offset + x_location, (i+1)*y_offset + y_location)])
            else:
                pygame.draw.polygon(screen, light_squre_color, [(j * x_offset + x_location, i * y_offset + y_location), ((j+1)*x_offset + x_location, i*y_offset + y_location), ((j+1)*x_offset + x_location, (i+1)*y_offset + y_location), (j*x_offset + x_location, (i+1)*y_offset + y_location)])

running = True
while running:
    screen.fill(WHITE)

    checkerboard()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
