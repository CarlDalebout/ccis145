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

colors = [(0,    0,      0)
         ,(255,  0,      0)
         ,(0,    255,    0)
         ,(0,    0,      255)
         ,(128,  0,      128)
         ,(255,  165,    0)]

i = 0

ballRadius = 20
ballX = screen_width/2 # starting horizontal position
ballY = screen_height/2 # starting vertical position
speedX = 5 # speed of ball 's vertical movement
direction = 'right ' # ball 's starting direction

while True :
    screen.fill( (255, 255, 255))

    ballX += speedX
    if(ballX >= screen_width -ballRadius or ballX < ballRadius):
        i += 1
        speedX *= -1
    
    # Drawing the ball on the screen
    pygame.draw.circle(screen , colors[i%6] , ( ballX , ballY ) , ballRadius )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )
