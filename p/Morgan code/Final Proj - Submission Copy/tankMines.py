"""
    This module contains what is needed to handle torpedoes for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame, math, random
from tankGlobals import *

import tankImage, tankSound

class tankMine( pygame.sprite.Sprite ):
    def __init__( self, screen, rank, owner, raw_speed, lifespan, maxrange, facing, position = (200,200) ):
        pygame.sprite.Sprite.__init__(self)
        if rank == 1:                                               # Standard
            Mine_Info = R1_MINE                                     # Which Icon Set to use
            self.IFF_Works  = 0                                     # Never works
        elif rank == 2:                                             # IFF Enabled
            Mine_Info = R2_MINE                                     # Which Icon Set to use
            self.IFF_Works  = 90                                    # Works 90% of the time
        else:
            return
        tankSFX = tankSound.gameSound()
        tankSFX.Play_Sound( "Energy Weapon-16" )
            
        self.def_facing     = 0.0                                   # set the direction the icon describs as 0
        self.facing         = facing
        self.frames         = Mine_Info[0]                          # set the frame number at which to wrap-around to 0
        self.cur_frame      = 0                                     # which frame are we currently on
        self.imglist        = []
        workImage           = tankImage.gameImage()
        for i in range(1, len(Mine_Info) ):
            workImage.image = workImage.Get_Image(Mine_Info[i])
            workImage.image = self.rot_projectile( workImage.image )
            self.imglist.append(workImage.image)
        self.image          = self.imglist[self.cur_frame]          # set image to current frame
        self.rect           = self.image.get_rect()
        self.rect.center    = position
        self.max_frame_time = FRAME_RATE * 3                        # Animate self.frames per second
        self.frame_time     = self.max_frame_time
        self.lifespan       = FRAME_RATE * lifespan
        self.maxrange       = maxrange                              # at what range does shot expire
        self.range          = 0                                     # how far have we travelled
        self.damage         = 24
        self.raw_speed      = raw_speed
        self.owner          = owner
        self.dx             = 0.0
        self.dy             = 0.0
        #Variables specific to Mines
        self.safety_timer   = FRAME_RATE * MINE_SAFETY              # How many seconds before mine is 'armed'
        #self.Set_Speed()                                           # Mines don't have a speed, they sit and stay.
        self.alive          = True
        self.owner.cur_aux_shots += 1
        self.owner.cur_aux_ammo  -= 1
        self.owner.aux_cd_time = FRAME_RATE * self.owner.aux_cd    # make it so we can't fire again immediately
        self.type           = "MINE"                                # storing type of sprite
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
        
        if self.safety_timer > 0:
            self.safety_timer  -= 1
            self.lifespan      += 1         # Refund the shot lifespan while in safety mode
        
        
        self.Animate()

        # self.rect.centery += self.dy      # Mines don't move
        # self.rect.centerx += self.dx      # Mines don't move
            
        # now let's test for collisions
        collisions = pygame.sprite.spritecollide( self, TankSprites, False )
        one_hit = False
        #IFF_Works determines what percentage the IFF stops the mine from detonating on friendly tanks
        if collisions:
            for impacted in collisions:
                if self.safety_timer > 0:       # skip checks while in safety
                    continue
                if one_hit:
                    continue
                if ( impacted == self.owner ) and ( random.randrange(0,100) < self.IFF_Works ):
                    debug("IFF Worked!  Prox Mine ignored friendly target.")
                    if self.safety_timer < 1:
                        self.safety_timer += FRAME_RATE / 2     # We stop checking against collisions for 1/2 of a second
                    continue
                else:
                    one_hit = True
                    impacted.harm_tank( self.damage, DAM_MINE, self.owner )
                #fi
            #rof
        #fi
        shotCollisions = pygame.sprite.spritecollide( self, ShotSprites, False )
        shot_hit       = False
        kill_shot      = None
        if shotCollisions:
            for impacted in shotCollisions:
                if shot_hit or one_hit:         # can only detonate once.
                    continue
                if impacted == self:            # Do not detonate early on self
                    continue
                if impacted.type == "TANK":     # Do not detonate early on tanks
                    continue
                if impacted.type == "CRATE":    # Do not detonate on crates
                    continue
                shot_hit = True                 # Guess we hit something lethal to the mine...time to go boom
                kill_shot = impacted
            #rof
        #fi
        if shot_hit:
            kill_shot.reset()
        if one_hit or shot_hit:
            self.reset()

    def reset ( self ):
        self.owner.cur_aux_shots -= 1
        self.kill( )
        
