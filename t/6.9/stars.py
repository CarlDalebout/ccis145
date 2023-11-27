import pygame
import math

pygame.init()

screen_width  = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('stars')

# Colors
WHITE  = (255,  255,    255)
BLACK  = (0,    0,      0)
RED    = (255,  0,      0)
GREEN  = (0,    255,    0)
BLUE   = (0,    0,      255)
PURPLE = (128,  0,      128)
ORANGE = (255,  165,    0)

def filled_star(x_location = screen_width/2, y_location = screen_height/2, radius = 75, color = RED, points = 5):
    theta = (2 * 3.1415926) / (points * 2)
    c = math.cos(theta)
    s = math.sin(theta)
    t = 0

    x = 1
    y = 0

    points_list = list()
    for i in range (points*2):
        if(i % 2 == 0):
            new_point = [x * radius + x_location, y * radius + y_location]
            points_list.append(new_point)
        else:
            new_point = [x * (radius/3) + x_location, y * (radius/3) + y_location]
            points_list.append(new_point)

        t = x
        x = c * x - s * y
        y = s * t + c * y

    pygame.draw.polygon(screen, color, points_list)

def unfilled_star(x_location = screen_width/2, y_location = screen_height/2, radius = 75, color = BLACK, width = 5):
    theta = (2 * 3.1415926) / 5
    c = math.cos(theta)
    s = math.sin(theta)
    t = 0

    x = 1
    y = 0

    points_list = list()
    for i in range (5):
        
        new_point = [x * radius + x_location, y * radius + y_location]
        points_list.append(new_point)
        
        t = x
        x = c * x - s * y
        y = s * t + c * y

    for i in range (5):
        pygame.draw.line(screen, color, (points_list[i][0], points_list[i][1]), (points_list[(i+2)%5][0], points_list[(i+2)%5][1]), width)



running = True
while running:
    screen.fill(WHITE)


    unfilled_star(screen_width/4, screen_height/2, 75, BLACK, 1)
    filled_star()
    unfilled_star(screen_width*0.75, screen_height/2, 75, BLACK, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
    
