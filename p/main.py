# import pygame

# from pygame.locals import(
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )

# def update(self, pressed_keys):
#     if pressed_keys[K_UP]:
#         self.rect.move_ip(0, -5)
#     if pressed_keys[K_DOWN]:
#         self.rect.move_ip(0, 5)
#     if pressed_keys[K_LEFT]:
#         self.rect.move_ip(-5, 0)
#     if pressed_keys[K_RIGHT]:
#         self.rect.move_ip(5, 0)


# pygame.init()
# #setup the display
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
# pygame.display.set_caption("Test Pygame!!!")

# # Define a Player object by extending pygame.sprite.Sprite
# # The surface drawn on the screen is now an attribute of 'player'\
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()

# # setting up the offsett for moving objects
# x_offset = 400
# y_offset = 300

# running = True
# while running:

#     # Look at every event in the queue
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#         # Did the user click the window close button?
#         elif event.type == pygame.QUIT:
#             running = False

# Get all the keys currently pressed
# pressed_keys = pygame.key.get_pressed()

# # Fill the background with white
# screen.fill((255, 255, 255))

# # Create a surface and pass in a tuple  containing its length and width
# surf = pygame.Surface((50, 50))
# surf.fill((0, 0, 0))
# rect = surf.get_rect()
# suft_center = (
#     (SCREEN_WIDTH-surf.get_width())/2,
#     (SCREEN_HEIGHT-surf.get_height())/2
# )

# # Draw a solid blue circle in the center
# pygame.draw.circle(screen, (0, 0, 255), (x_offset, y_offset), 75)

# # This line says "Draw surf onto the screen at the center"
# screen.blit(surf, suft_center)
# pygame.display.flip()

# pygame.quit()
# ----------------------------------------


# Import the pygame module
import pygame


# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

def update(self, pressed_keys):
    if pressed_keys[K_UP]:
        self.rect.move_ip(0, -5)
    if pressed_keys[K_DOWN]:
        self.rect.move_ip(0, 5)
    if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)

    if self.rect.left < 0:
        self.rect.let = 0
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
        self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT

# Initialize pygame
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

    # Get all the keys currently pressed
    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the player on the screen
    screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    # Update the display
    pygame.display.flip()