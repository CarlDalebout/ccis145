import pygame
import sys

pygame.init()

screen_width  = 800
screen_height = 600
pygame.display.set_caption('stars')

FPS = 60 # frames per second setting
# Initialize a clock object to control frame rate
fpsClock = pygame.time.Clock ()

# set up the window
screen = pygame.display.set_mode((screen_width, screen_height) , 0 , 32)
pygame.display.set_caption('Bouncing Ball Animation')

WHITE = (255 , 255 , 255)

class ball:
    def __init__(self, x_location = screen_width/2, y_location = screen_height/2, ball_radius = 20, speed_x = 5, speed_y = 0):
        self.__x        = x_location
        self.__y        = y_location
        self.__radius   = ball_radius
        self.__speed_x  = speed_x
        self.__speed_y  = speed_y

    def get_speed_x(self, speed):
        self.__speed_x = speed
        return self.__speed_x

ball1Radius = 20
ball1X = screen_width/2 # starting horizontal position
ball1Y = screen_height/2 # starting vertical position
speed1X = 5 # speed of ball 's vertical movement

ball2Radius = 20
ball2X = screen_width/2 # starting horizontal position
ball2Y = screen_height/2 # starting vertical position
speed2X = -3 # speed of ball 's vertical movement


while True :
    screen.fill( WHITE )

    ball1X += speed1X
    ball2X += speed2X
    if(ball1X >= screen_width -ball1Radius or ball1X < ball1Radius):
        speed1X *= -1
    
    if(ball2X >= screen_width - ball2Radius or ball2X < ball2Radius):
        speed2X *= -1
    
    # Drawing the ball on the screen
    pygame.draw.circle(screen , (0 , 0 , 255) , ( ball1X , ball1Y ) , ball1Radius )
    pygame.draw.circle(screen , (0 , 0 , 255) , ( ball2X , ball2Y ) , ball2Radius )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )
