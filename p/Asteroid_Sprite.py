
import pygame, math, random, os, sys
from tankGlobals import *

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, screen, name = "bolder", position = (0, 0), icon = "Asteroid Brown"):
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

    def icon(self):
        return self.icon

    def rect(self):
        return self.rect

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