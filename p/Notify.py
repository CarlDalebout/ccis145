"""
    This module contains the on screen pop-ups subsystem for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from Globals import *

class Notification( pygame.sprite.Sprite ):
    def __init__( self, screen, text = "yay", textSize = 24, duration = 1, position = (250, 250), color = WHITE, speed = (0,-3) ):
        """
            This will spawn a text notifier at a given 'position' on screen for 'duration' seconds or until it leaves the screen.
            Uses the following 
            .screen         = Stores which screen it is appearing on
            .text           = Stores what the text of the notification is
            .textSize       = Stores what fontsize to use for the notification
            .duration       = Stores how long the notification should be on screen
            .rect           = Stores the position of the notification
            .dy             = Stores the movement delta of the y-axis
            .dx             = Stores the movement delta of the x-axis
            .color          = Stores the fontcolor used to generate the notification
            .type           = Stores the sprite type, used for testing during updates
        """
        pygame.sprite.Sprite.__init__(self)
        self.font           = pygame.font.SysFont("None", textSize )
        self.screen         = screen
        self.duration       = duration * FRAME_RATE
        self.text           = text
        self.textSize       = textSize
        self.image          = self.font.render( self.text, 1, color )       
        self.rect           = self.image.get_rect()
        self.rect.center    = position
        self.dx, self.dy    = speed
        self.type           = "TEXT"
        self.color          = color
        
        FreeSpawn = False
        while ( FreeSpawn == False ):
            overlapping_text = pygame.sprite.spritecollideany( self, pygame.sprite.Group() )
            if not overlapping_text:
                FreeSpawn = True
            else:
                self.rect.centery += self.rect.height * 1.5
            #fi
        #wend        
        self.add(pygame.sprite.Group())
        
    def update( self ):
        self.duration -= 1
        if ( self.duration <= 0 ):
            self.reset()
        else:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            
            l_boundX = MAIN_SCREEN.left
            l_boundY = MAIN_SCREEN.top
            u_boundX = MAIN_SCREEN.right
            u_boundY = MAIN_SCREEN.bottom

            if self.rect.bottom >= u_boundY:
                self.reset()
            if self.rect.top <= l_boundY:
                self.reset()
            if self.rect.right >= u_boundX:
                self.rect.left = l_boundX + 1
            if self.rect.left <= l_boundX:
                self.rect.right = u_boundX - 1
            
            
    def reset( self ):
        self.text = "Empty"
        self.image = self.font.render( self.text, 1, (255, 255, 0 ) )
        self.rect = self.image.get_rect()
        self.rect.center = OFF_SCREEN
        self.kill()
