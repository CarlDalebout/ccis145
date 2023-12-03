"""
    this is the class for the player ship and will contain the sounds its plays
    WIP: working on scan_keys function to detect if there are keys being pushed down
Carl Dalebout    
"""

import pygame, math, random, os, sys
from Globals import *
import Lazer_Sprite

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

class Player_Ship( pygame.sprite.Sprite ):
    def __init__(self, screen, name = "Ship Name", position = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), icon = "Player Ship2"):
        self.screen         = screen
        self.name           = name
        self.icon           = icon
        self.angle          = 0
        self.speed          = 5
        self.position       = position
        self.icon           = self.Load_Icon( icon )
        self.orig_icon      = self.icon
        self.icon           = pygame.transform.scale(self.icon, (63, 63))
        self.rect           = self.icon.get_rect()
        self.rect.topleft   = self.position
        self.shots_fired    = 0
        self.projectile_list = [Lazer_Sprite.Laser(screen, "testLazer2", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1] + 25))]
        self.lazer_sound    = pygame.mixer.Sound(os.path.join(SOUND_PATH, "laser.mp3"))
        self.type           = "PLAYER"
        
    def Load_Icon( self, icon ):
        """
            This should attempt to construct an icon name from the icon string given and load it
            First it will smash all spaces and turn them into _
            Uses IMAGE_PATH
        """
        work_name = icon.replace( " ", "_" )                # spaces converted to underscores
        gif_name  = work_name + ".gif"                      # we'll attach a gif ending as default to image,
        png_name  = work_name + ".png"                      # we'll attach a png ending as default to image,
        gif_file  = os.path.join( IMAGE_PATH, gif_name )    # path pre-pended
        png_file  = os.path.join( IMAGE_PATH, png_name )    # path pre-pended
        if os.path.exists( gif_file ):
            work_file = gif_file
        else:
            work_file = png_file

        if os.path.exists(work_file):                       # If the file actually exists...
            # debug("Image file %s [%s] found." % ( icon, work_file ) )
            work_contents = pygame.image.load( work_file )  # ... we load it
            work_contents.convert_alpha()                   # ... and we convert it with alpha layering intact
            return work_contents                            # ... and we return it to use
        else:
            # debug("Image file %s [%s] could not be found." % ( icon, work_file ) )
            return False
        
    def rot_center( self, image, angle):
        """rotate an image while keeping its center and size"""
        """code from pygame.org/docs/transform.html"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
        
    def scan_keys(self):
        for event in pygame.event.get():
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
                    if len(self.projectile_list) <= 5:
                        self.lazer_sound.play()
                        rag_angle = self.angle * 3.1415 / 180
                        lazer_x = math.cos(rag_angle)
                        lazer_y = math.sin(rag_angle)
                        M = max(abs(lazer_x), abs(lazer_y))
                        lazer_x = (self.rect.width/2 * lazer_x / M)  + self.rect.x
                        lazer_y = (self.rect.height/2 * lazer_y / M) + self.rect.y
                        self.projectile_list.append((Lazer_Sprite.Laser(self.screen, "lazer", (lazer_x, lazer_y), self.angle+90)))
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
                self.pAction = True

    def update(self):
        if PLAYER_KEYS[0] == True and PLAYER_KEYS[1] == True:
            {}
        elif PLAYER_KEYS[0] == True:
            # print("moved up")
            self.rect.y -= self.speed
        elif PLAYER_KEYS[1] == True:
            # print("moved down")
            self.rect.y += self.speed

        if PLAYER_KEYS[2] == True and PLAYER_KEYS[3] == True:
            # print("2 and 3 are pressed")
            {}
        elif PLAYER_KEYS[2] == True:
            # print("moved left")
            self.rect.x -= self.speed
        elif PLAYER_KEYS[3] == True:
            # print("moved right")
            self.rect.x += self.speed

        if PLAYER_KEYS[5] == True and PLAYER_KEYS[6] == True:
            {}
        elif PLAYER_KEYS[5] == True:
            # print("rotated clockwise")
            self.angle += self.speed
        elif PLAYER_KEYS[6] == True:
            # print("rotated counter_clockwise")
            self.angle -= self.speed

def main():
    global player
    playerScreen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    player = Player_Ship(playerScreen, "Hello World", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))

    running = True
    while running:
        playerScreen.fill((0, 0, 0))

        playerScreen.blit(player.icon, player.rect.topleft)
        pygame.display.update()
