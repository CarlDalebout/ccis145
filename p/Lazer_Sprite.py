
import pygame, math, random, os, sys
from Globals import *

class Laser(pygame.sprite.Sprite):
    def __init__(self, screen, name = "lazer", position = (SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2), angle = 0, icon = "Lazer"):
        self.screen         = screen
        self.name           = name
        self.icon           = icon
        self.angle          = angle
        self.speed          = 5
        rad_angle = self.angle * 3.1415 / 180
        self.dx             = math.cos(rad_angle) * self.speed
        self.dy             = math.sin(rad_angle) * self.speed
        self.position       = position
        self.icon           = self.Load_Icon( icon )
        self.orig_icon      = self.icon
        self.icon           = pygame.transform.scale(self.icon, (25, 25))
        self.icon           = pygame.transform.rotate(self.icon, angle)
        self.rect           = self.icon.get_rect()
        self.rect.topleft   = self.position
        self.angle          = angle

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
            # print("Image file %s [%s] found." % ( icon, work_file ) )
            work_contents = pygame.image.load( work_file )  # ... we load it
            work_contents.convert_alpha()                   # ... and we convert it with alpha layering intact
            return work_contents                            # ... and we return it to use
        else:
            
            # print("dImage file %s [%s] could not be found." % ( icon, work_file ) )
            return False


    
    def update(self):
        # print(f"{self.name} x_pos: {self.rect.x} y_pos: {self.rect.y}")
        if self.rect.x < 0 or self.rect.x >= SCREEN_SIZE[0]:
            # print(self.name, "is out of bounds")
            return "OutOfBounds"
        if self.rect.y < 0 or self.rect.y >= SCREEN_SIZE[1]:
            # print(self.name, "is out of bounds")
            return "OutOfBounds"
        self.rect.x += self.dx
        self.rect.y -= self.dy

        
        