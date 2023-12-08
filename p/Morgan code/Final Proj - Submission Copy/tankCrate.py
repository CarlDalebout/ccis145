"""
    This module contains what is needed to handle crates for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame, math, random
from tankGlobals import *

import tankImage, tankSound

class tankCrate( pygame.sprite.Sprite ):
    def __init__( self, screen, icon ):
        pygame.sprite.Sprite.__init__(self)
        
        self.def_facing     = 0.0                                   # set the direction the icon describs as 0
        self.facing         = self.def_facing
        workImage           = tankImage.gameImage()
        self.image          = workImage.Get_Image( icon )
        self.raw_image      = self.image
        self.rect           = self.image.get_rect()
        self.rect.center    = OFF_SCREEN
        self.max_frame_time = FRAME_RATE * 0.25
        self.frame_time     = self.max_frame_time
        self.rot_amount     = ROT_RATE
        self.raw_speed      = SPEED_MAX
        self.dx             = 0.0
        self.dy             = 0.0
        self.spawnTime      = CRATE_SPAWN_RATE
        self.type           = "SUPPLY CRATE"                        # storing type of sprite
        self.add( BonusSprites )                                    # Shots track projectiles
        self.reset()

    def Set_Speed( self ):
        """
            Randomly sets the crates speed
            combined x,y speeds will not exceed self.raw_speed
        """
        x_speed             = 0.0
        y_speed             = 0.0        
        remain_speed        = self.raw_speed * 100
        x_speed             = random.randrange(100, remain_speed, 10 )
        remain_speed        = max( 200, ( remain_speed - x_speed ) )
        y_speed             = random.randrange(100, remain_speed, 10 )
        x_speed            /= 100
        y_speed            /= 100
        
        if random.randrange(1,100) > 50:        # half the time it goes the other way
            x_speed        *= -1
        if random.randrange(1,100) > 50:        # half the time it goes the other way
            y_speed        *= -1
        
        self.dx             = x_speed
        self.dy             = y_speed
    
    def rot_projectile( self, theImage ):
        rotDegrees          = self.facing - self.def_facing
        work_image          = self.rot_center( theImage, -rotDegrees )
        return work_image

    def rot_center( self, image, angle):
        """rotate an image while keeping its center and size"""
        """code from pygame.org/docs/transform.html"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
      
    def Animate( self ):
        self.frame_time        -= 1
        if ( self.frame_time < 1 ):
            self.frame_time     = self.max_frame_time
            self.facing        += self.rot_amount
            if self.facing > 359:
                self.facing -= 360
            elif self.facing < 0:
                self.facing += 360
            self.image          =  self.rot_projectile( self.raw_image )
        
    def update( self ):
        if self.spawnTime > 0:      # we stay offscreen while spawntimer is going
            self.spawnTime -= 1
            if self.spawnTime < 1:  # we spawned!
                tankSFX     = tankSound.gameSound()
                tankSFX.Play_Sound( "Bonus" )
                
                w_m64       = MAIN_SCREEN[2]
                w_m64       = w_m64 - ( w_m64 % 64 )      # screen width evenly disible by 64
                h_m64       = MAIN_SCREEN[3]
                h_m64       = w_m64 - ( w_m64 % 64 )      # screen height evenly disible by 64

                randY   = random.randrange(64, h_m64, 64 )
                randX   = random.randrange(64, w_m64, 64 )
                self.state = "NORMAL"
                self.rect.centerx = randX
                self.rect.centery = randY
            else:
                return

        self.Animate()
        self.rect.centery += self.dy
        self.rect.centerx += self.dx
                
        l_boundX = MAIN_SCREEN.left
        l_boundY = MAIN_SCREEN.top
        u_boundX = MAIN_SCREEN.right
        u_boundY = MAIN_SCREEN.bottom

        if self.state == "NORMAL":
            if ( self.rect.bottom >= u_boundY ):
                self.rect.top = l_boundY + 1
                
            if ( self.rect.top <= l_boundY ):
                self.rect.bottom = u_boundY - 1

            if ( self.rect.right >= u_boundX ):
                self.rect.left = l_boundX + 1

            if ( self.rect.left <= l_boundX ):
                self.rect.right = u_boundX - 1
        #fi
        
        if self.state == "ARRIVING":        # it's not here yet, so don't hit it
            return
        # now let's test for collisions
        collisions = pygame.sprite.spritecollide( self, TankSprites, False )
        one_hit = False
        if collisions:
            for impacted in collisions:
                if one_hit:
                    continue
                else:
                    one_hit = True
                    impacted.crate_bonus( )
                #fi
            #rof
        #fi
        if one_hit:
            self.reset()

    def reset ( self ):
        self.spawnTime      = CRATE_SPAWN_RATE
        quarterRate         = CRATE_SPAWN_RATE / 4
        randMod             = random.randrange(1,301)
        if randMod <= 100:
            self.spawnTime -= quarterRate
        elif randMod >= 200:
            self.spawnTime += quarterRate
        debug( "Cratespawn in %d frames" % self.spawnTime )
        self.rect.center    = OFF_SCREEN
        self.facing         = 0.0
        self.frame_time     = self.max_frame_time
        self.state          = "SPAWNING"
        if random.randrange(1,100) > 50:            # half the time we change rotation directions
            self.rot_amount = -self.rot_amount
        self.Set_Speed()
        