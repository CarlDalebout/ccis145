"""
    This module contains what is needed to handle bullets for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame, math
from tankGlobals import *

import tankImage, tankSound

class tankBullet( pygame.sprite.Sprite ):
    def __init__( self, screen, rank, owner, lifespan, maxrange, facing, position = (200,200) ):
        pygame.sprite.Sprite.__init__(self)
        if rank > 1:
            rank = 1                                                # at the moment, cap bullets to rank 1
        if rank == 1:                                               # Standard
            Bullet_Info = R1_BULLET                                 # Which Icon Set to use
        else:
            return
        tankSFX = tankSound.gameSound()
        tankSFX.Play_Sound( "Energy Weapon-24" )
        
        self.def_facing     = 0.0                                   # set the direction the icon describs as 0
        self.facing         = facing
        self.frames         = Bullet_Info[0]                        # set the frame number at which to wrap-around to 0
        self.cur_frame      = 0                                     # which frame are we currently on
        self.imglist        = []
        workImage           = tankImage.gameImage()
        for i in range(1, len(Bullet_Info) ):
            workImage.image = workImage.Get_Image(Bullet_Info[i])
            workImage.image = self.rot_projectile( workImage.image )
            self.imglist.append(workImage.image)
        self.image          = self.imglist[self.cur_frame]          # set image to current frame
        self.rect           = self.image.get_rect()
        self.rect.center    = position
        self.max_frame_time = FRAME_RATE / self.frames              # Animate self.frames per second
        self.frame_time     = self.max_frame_time
        self.lifespan       = FRAME_RATE * lifespan
        self.maxrange       = maxrange                              # at what range does shot expire
        self.range          = 0                                     # how far have we travelled
        self.damage         = 4                                     # bullets do little damage      12-07-2010 bullet damage doubled
        self.raw_speed      = 13
        self.owner          = owner
        self.dx             = 0.0
        self.dy             = 0.0
        self.Set_Speed()                                            # Set our speed according to facing/raw_speed
        self.alive          = True
        self.owner.cur_primary_shots += 1
        self.owner.cur_primary_ammo  -= 1
        self.owner.primary_cd_time   = FRAME_RATE * self.owner.primary_cd    # make it so we can't fire again immediately
        self.type           = "BULLET"                              # storing type of sprite
        self.add( ShotSprites )                                     # Shots track projectiles

        
    def Set_Speed( self ):
        """ Set's a projectiles speed based off heading and given raw_speed as max """
        """ Will also calc an offset from center actually start the projectile """
        """ Based off of calcVector from carVec.py book example """
        
        workFacing          = self.facing - 90
        radians             = workFacing * math.pi / 180
        work_dx             = math.cos(radians)
        work_dy             = math.sin(radians)
        
        offset_dx           = work_dx * ( self.rect.width )
        offset_dy           = work_dy * ( self.rect.height )
        self.rect.centerx  += offset_dx
        self.rect.centery  += offset_dy
        
        work_dx            *= self.raw_speed
        work_dy            *= self.raw_speed

        self.dx             = work_dx
        self.dy             = work_dy
    
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
            self.cur_frame     += 1
            if ( self.cur_frame >= self.frames ):
                self.cur_frame  = 0
            self.image          =  self.imglist[self.cur_frame]

        
    def update( self ):
        if not self.alive:
            return
        
        if self.lifespan > 0:
            self.lifespan -= 1
        else:
            self.reset()
        
        self.Animate()

        self.rect.centery += self.dy
        self.rect.centerx += self.dx
        
        work_dy = abs( self.dy )
        work_dx = abs( self.dx )
        drange = math.sqrt(math.pow(work_dx,2)+math.pow(work_dy,2))
        self.range += drange
        l_boundX = MAIN_SCREEN.left
        l_boundY = MAIN_SCREEN.top
        u_boundX = MAIN_SCREEN.right
        u_boundY = MAIN_SCREEN.bottom
        
        if self.range > self.maxrange:
            self.reset()

        if ( self.rect.bottom >= u_boundY ):
            self.rect.top = l_boundY + 1
            #self.reset()
            
        if ( self.rect.top <= l_boundY ):
            self.rect.bottom = u_boundY - 1
            #self.reset()

        if ( self.rect.right >= u_boundX ):
            self.rect.left = l_boundX + 1
            #self.reset()

        if ( self.rect.left <= l_boundX ):
            self.rect.right = u_boundX - 1
            #self.reset()
            
        # now let's test for collisions
        collisions = pygame.sprite.spritecollide( self, TankSprites, False )
        one_hit = False
        if collisions:
            for impacted in collisions:
                if one_hit:
                    continue
                if ( impacted == self.owner ):
                    debug("Safety Enabled!  Bullet ignored friendly target.")
                    continue
                else:
                    one_hit = True
                    impacted.harm_tank( self.damage, DAM_BULLET, self.owner )
                #fi
            #rof
        #fi
        if one_hit:
            self.reset()

    def reset ( self ):
        self.owner.cur_primary_shots -= 1
        self.kill( )
        
