"""
    This module contains the background image module for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from tankGlobals import *

class Background( pygame.sprite.Sprite ):
    def __init__( self, screen, position = MAIN_SCREEN, imageFile = "none" ):
        """
            This will spawn a background 'imageFile' Sprite onto the 'screen' at 'position'.
            Uses the following 
            .screen         = Stores which screen it is appearing on
            .rect           = Stores the position of the background
            .type           = Stores the sprite type, used for testing during updates
        """
        pygame.sprite.Sprite.__init__(self)
        self.screen         = screen
        self.image          = self.Load_Image( imageFile )
        self.rect           = self.image.get_rect()
        self.rect           = position
        self.type           = "BACKGROUND"
        self.name           = str(imageFile)
        self.add(BackgroundSprites)

    def Load_Image( self, image ):
        """
            This should attempt to construct an image name from the image string given and load it
            First it will smash all spaces and turn them into _
            Uses IMAGE_PATH
        """
        work_name = image.replace( " ", "_" )               # spaces converted to underscores
        gif_name  = work_name + ".gif"                      # we'll attach a gif ending as default to image,
        png_name  = work_name + ".png"                      # we'll attach a png ending as default to image,
        gif_file  = os.path.join( IMAGE_PATH, gif_name )    # path pre-pended
        png_file  = os.path.join( IMAGE_PATH, png_name )    # path pre-pended
        if os.path.exists( gif_file ):
            work_file = gif_file
        else:
            work_file = png_file
        if os.path.exists(work_file):                       # If the file actually exists...
            debug("Image file %s [%s] found." % ( image, work_file ) )
            work_contents = pygame.image.load( work_file )  # ... we load it
            work_contents.convert()                         # ... and we convert it without alpha layering intact
            return work_contents                            # ... and we return it to use
        else:
            debug("Image file %s [%s] could not be found." % ( image, work_file ) )
            return False
            
    def update( self ):     # nothing to update really
        pass
