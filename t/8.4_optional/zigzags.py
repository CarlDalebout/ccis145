import pygame , sys

# Initialize pygame
pygame.init()

# Constants
WIDTH , HEIGHT = 800, 600
SPEED_X = 2
SPEED_Y = 2
ZIGZAG_SPAN = 40 # Horizontal distance before changing direction

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize the display and clock
DISPLAYSURF = pygame.display.set_mode ((WIDTH , HEIGHT))
pygame.display.set_caption('Downward Zigzag Pattern Movement ')
fpsClock = pygame.time.Clock ()

# Ball's starting position and direction
x, y = WIDTH // 2, 25
dir_x = 1
initial_x = x

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(WHITE)

    x += SPEED_X * dir_x
    y += SPEED_Y

    # Check if the horizontal zigzag span is covered
    if abs(x - initial_x) >= ZIGZAG_SPAN:
        dir_x *= -1 # Reverse horizontal direction
        initial_x = x # Reset the initial position for the next span

    if y > HEIGHT-25 or y < 25:
        SPEED_Y *= -1

    pygame.draw.circle(DISPLAYSURF , RED , (int(x), int(y)), 25)

    pygame.display.flip()
    fpsClock.tick (60)