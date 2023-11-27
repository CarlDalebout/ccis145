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
ballRadius = 20
ballX = screen_width/2 # starting horizontal position
ballY = screen_height/2 # starting vertical position
speedX = 5 # speed of ball 's vertical movement
radius_growth = 5
direction = 'right ' # ball 's starting direction

while True :
    screen.fill( WHITE )

    ballX += speedX
    if(ballX >= screen_width - (ballRadius+radius_growth) or ballX < ballRadius):
        speedX *= -1
        ballRadius += radius_growth
        ballX += speedX
        if(ballRadius >= 100 or ballRadius < 20):
            radius_growth *= -1
        
    
    # Drawing the ball on the screen
    pygame.draw.circle(screen , (0 , 0 , 255) , ( ballX , ballY ) , ballRadius )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    # Ensure the loop runs
    fpsClock.tick( FPS )
