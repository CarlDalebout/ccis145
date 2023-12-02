"""
    this is the class for the player ship and will contain the sounds its plays
    WIP: working on scan_keys function to detect if there are keys being pushed down
Carl Dalebout    
"""

import pygame, math, random, os, sys
from Globals import *

class Player_Ship( pygame.sprite.Sprite ):
    def __init__(self, screen, name = "Ship Name", position = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), icon = "Player Ship2"):
        self.screen         = screen
        self.name           = name
        self.icon           = icon
        self.angle          = 0
        self.dx             = 0.0
        self.dy             = 0.0
        self.position       = position
        self.icon           = self.Load_Icon( icon )
        self.icon           = pygame.transform.scale(self.icon, (63, 63))
        self.rect           = self.icon.get_rect()
        self.rect.topleft   = self.position
        self.orig_icon      = self.icon
        self.shots_fired    = 0
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
            debug("Image file %s [%s] found." % ( icon, work_file ) )
            work_contents = pygame.image.load( work_file )  # ... we load it
            work_contents.convert_alpha()                   # ... and we convert it with alpha layering intact
            return work_contents                            # ... and we return it to use
        else:
            debug("Image file %s [%s] could not be found." % ( icon, work_file ) )
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
        KeyDown = pygame.key.get_pressed()
        ScanKeys = []
        self.pAction = False     # Storage to see if we have done an action this check?
        if self.pAction:
            pass            # We've done an action, stop looking
        if KeyDown[ScanKeys[P_FORWARD]]:         #move player forward
            # self.Accelerate()
            self.pAction = True
        if KeyDown[ScanKeys[P_BACKWARD]]:        #reverse player
            # self.Decelerate()
            self.pAction = True
        if KeyDown[ScanKeys[P_STRAFE_LEFT]]:     #move player left
            self.pAction = True
        if KeyDown[ScanKeys[P_STRAFE_RIGHT]]:    #move player right
            self.pAction = True
        if KeyDown[ScanKeys[P_TURN_LEFT]]:       #rotate player CounterClockwise
            self.rotateTank(False)
            self.pAction = True
        if KeyDown[ScanKeys[P_TURN_RIGHT]]:      #rotate player clockwise
            self.pAction = True
        if KeyDown[ScanKeys[P_FIRE_MAIN]]:       #fire tank's main guns
            self.pAction = True
       

def main():
    global player
    playerScreen = pygame.display.set_mode((SCREEN_SIZE[0], SCREEN_SIZE[1]))
    player = Player_Ship(playerScreen, "Hello World", (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2))

    running = True
    while running:
        playerScreen.fill((0, 0, 0))

        playerScreen.blit(player.icon, player.rect.topleft)
        pygame.display.update()

main()