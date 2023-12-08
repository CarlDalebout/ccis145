"""
    This module contains the sound subsystem for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame, math, random

import tankUpgrade, Notify, tankCombat, tankSound, tankScore
from tankGlobals import *

class tankPlayer( pygame.sprite.Sprite ):
    def __init__( self, screen, name = "Random", player = 1, position = ( 300, 300), icon = "Simple Tank 1" ):
        """
            This will spawn a tank with ICON named 'name' for PLAYER at a given 'position'
            Uses the following 
            .screen         = Stores which screen it is appearing on
            .name           = Stores what the name of the tank is
            .player         = Stores which team the tank is on
            .rect           = Stores the position of the notification
            .dy             = Stores the movement delta of the y-axis
            .dx             = Stores the movement delta of the x-axis
            .type           = Stores the sprite type, used for testing during updates
            .icon           = Stores the icon base used to generate the tank
            .facing         = Stores which direction the tank is facing in degrees
            .def_facing     = Stores the original direction the tank image was
            .type           = Stores the sprite type, used for testing during updates
            .upgrades       = Stores sub variables of various types regarding upgrades
        """
        pygame.sprite.Sprite.__init__(self)
        self.upgrades           = var_storage()
        self.screen             = screen
        self.name               = name
        self.player             = player
        self.icon               = icon
        self.def_facing         = 0.0
        self.facing             = 0.0
        self.dx                 = 0.0
        self.dy                 = 0.0
        self.position           = position
        self.icon               = self.Load_Icon( icon )
        self.rect               = self.icon.get_rect()
        self.rect.center        = self.position
        self.orig_icon          = self.icon
        self.cur_primary_shots  =   0   # Cur primary shots on screen
        self.cur_aux_shots      =   0   # Cur Aux shots on screen
        self.type               = "TANK"
        self.state              = "NORMAL"
        self.score              = tankScore.tankScore( self, 10 )
        self.Set_Image( self.icon, self.facing )
        self.clear_stats()
        self.base_equip()
        self.add( TankSprites )
        
    def clear_stats( self ):
        #we'll init ALL variables real quick first time through
        #these should mostly be overwritten by base_equip
        self.max_health         =  50   # Max hp    
        self.cur_health         =  50   # cur hp
        self.max_shield         =  16   # max sp
        self.cur_shield         =   0   # cur sp
        self.shield_decay_rate  =   2   # how many shields are lost when decay pulses
        self.shield_decay_time  =   0   # cur time till next shield decay pulse
        self.shield_charge_rate =   4   # how many shields gained when charged once
        self.shield_charge_cost =   8   # how much energy consumed to charge shields
        self.shield_charge_time =   0   # how long before we can charge shields again
        self.max_energy         =  32   # max ep
        self.cur_energy         =  32   # cur ep
        self.energy_charge_rate =   2   # how much energy regained in one pulse
        self.energy_charge_time =   0   # cur time till next energy charge pulse
        self.health_regen_rate  =   0   # how much hp regained in one pulse
        self.health_regen_time  =   1   # cur time till next health regen pulse
        self.health_regen_cost  =   0   # Only charged when regenerating hp
        self.max_primary_shots  =   2   # Max primary shots on screen at once
        self.max_primary_range  = 400   # Max primary shot range
        self.max_primary_ammo   =  64   # Max Pri Ammo
        self.cur_primary_ammo   =  32   # Cur Pri Ammo
        self.max_aux_shots      =   6   # Max Aux shots on screen at once  -- We're not really going to cap this
        self.max_aux_range      = 500   # Max aux shot range
        self.max_shot_life      =  50   # This is used for both Primary and Aux lifespans
        self.max_aux_ammo       =   2   # Max aux ammo
        self.cur_aux_ammo       =   1   # cur aux ammo
        self.primary_cd         = 1.5   # Seconds between primary shots
        self.primary_cd_time    =   0   # Cur time till next primary shot available
        self.aux_cd             = 1.5   # Seconds between auxillary shots
        self.aux_cd_time        =   0   # cur time till next auxillary shot available
        self.aux_weapon         =   1   # Cur Aux Weapon - Missiles
        self.aux_weapon_speed   =  20   # Cur Aux Weapon Speed 
        self.second_timer       =   0   # just counts time between seconds
        
    def clear_upgrades( self ):
        # Resets all upgrades to -1 prior to base_equip
        self.upgrades.hull_rank         = -1
        self.upgrades.hull_name         = ""
        self.upgrades.shield_rank       = -1
        self.upgrades.shield_name       = ""
        self.upgrades.shield_gen_rank   = -1
        self.upgrades.shield_gen_name   = ""
        self.upgrades.energy_rank       = -1
        self.upgrades.energy_name       = ""
        self.upgrades.energy_gen_rank   = -1
        self.upgrades.energy_gen_name   = ""
        self.upgrades.regen_rank        = -1
        self.upgrades.regen_name        = ""
        self.upgrades.cannon_rank       = -1
        self.upgrades.cannon_name       = ""
        self.upgrades.ammo_rank         = -1
        self.upgrades.ammo_name         = ""
        self.upgrades.shot_cd_rank      = -1
        self.upgrades.shot_cd_name      = ""
        self.upgrades.aux_rank          = -1
        self.upgrades.aux_name          = ""
        
    def base_equip( self ):
        """
            This should do basic default equippage of a tank, should only be called 
            during initial spawn and after death
        """
        #New tank has no upgrades
        self.clear_upgrades()
        #now we'll equip the tank with the basics
        tankUpgrade.equip_upgrade( self, "HULL", 1 )
        tankUpgrade.equip_upgrade( self, "SHIELD_CAP", 1 )
        tankUpgrade.equip_upgrade( self, "SHIELD_GEN", 1 )
        tankUpgrade.equip_upgrade( self, "ENERGY_TANK", 1 )
        tankUpgrade.equip_upgrade( self, "ENERGY_GEN", 1 )
        tankUpgrade.equip_upgrade( self, "REPAIR", 1 )
        tankUpgrade.equip_upgrade( self, "CANNON", 1 )
        tankUpgrade.equip_upgrade( self, "AMMO", 1 )
        tankUpgrade.equip_upgrade( self, "SHOT_CD", 1 )
        tankUpgrade.equip_upgrade( self, "AUX_WEAPON", 1 )
        
        #We'll forcibly restore the health to max as a generousity
        self.cur_health         = self.max_health

        #we reset shields to 0 along with time till next shield decay tick
        self.cur_shield         = 0
        self.shield_decay_time  = 0
        
        #we'll even give a full tank of E as a bonus and set time till next energy pulse to 0
        self.cur_energy         = self.max_energy
        self.energy_charge_time = 0
        
        #but due to budget cuts, ammunition only starts at half
        self.cur_primary_ammo   = self.max_primary_ammo / 2
        self.cur_aux_ammo       = self.max_aux_ammo / 2
        
        #We will let you fire immediately to use up your few shots
        self.primary_cd_time    = 0
        self.aux_cd_time        = 0
        
        #that should be it, the new tank is ready to be blown up
        #we're going to be nice and start tanks out with a random special weapon
        # of a courtesy it will NOT be leeches tho
        randWeapon = random.randrange(1,8)
        if   ( randWeapon >= 1 and randWeapon <= 2 ):
            newAux = AUX_5
        elif ( randWeapon >= 3 and randWeapon <= 4 ):
            newAux = AUX_4
        elif ( randWeapon >= 5 and randWeapon <= 6 ):
            newAux = AUX_1
        elif ( randWeapon >= 7 and randWeapon <= 8 ):
            newAux = AUX_2
    
        if   newAux == AUX_1:
            newSystem = "Missiles"
        elif newAux == AUX_2:
            newSystem = "Shield Pen Missiles"
        elif newAux == AUX_3:
            newSystem = "Leech Missiles"
        elif newAux == AUX_4:
            newSystem = "Plasma Torpedoes"
        elif newAux == AUX_5:
            newSystem = "Proximity Mines"
        tankUpgrade.equip_upgrade( self, newSystem )
        
    def apply_mod( self, field, amount ):
        if   field > MAX_MOD:
            debug("Attempted to apply mod #%d which doesn't exist." % field )
            return
        elif field == MOD_NONE:                             #placeholder
            return
        elif field == MOD_MAX_HP:                           #+Max HP also increases +Cur HP
            cur_max                 = self.max_health
            cur_cur                 = self.cur_health
            cur_dif                 = cur_max - cur_cur     #how much HP are we missing            
            self.max_health         = amount
            self.cur_health         = self.max_health - cur_dif
        elif field == MOD_MAX_SHIELD:                       #+Max SP destroys current shields
            self.max_shield         = amount
            self.cur_shield         = 0
        elif field == MOD_SHIELD_DECAY:                     #Changing shield decay forces 1 decay tick
            self.shield_decay_rate  = amount
            self.shield_decay_time  = 0                     #Force a decay
        elif field == MOD_SHIELD_GEN:                       #Changing shield gen rate
            self.shield_charge_rate = amount
        elif field == MOD_SHIELD_CHARGE:                    #Changing shield gen cost
            self.shield_charge_cost = amount
        elif field == MOD_MAX_ENERGY:                       #+Max Energy does not affect Cur Energy
            self.max_energy         = amount
        elif field == MOD_ENERGY_GEN:                       #+Energy charge forces an energy charge pulse
            self.energy_charge_rate = amount
            self.energy_charge_time = 0                     #Force a charge pulse
        elif field == MOD_REGEN_TIME:                       #+Healing Rate forces a healing pulse
            self.health_regen_rate  = amount
            self.health_regen_time  = 0                     #force a regen pulse
        elif field == MOD_ENERGY_DRAIN:                     #Modifying HP Regen Energy drain
            self.health_regen_cost  = amount
        elif field == MOD_MAX_SHOTS:                        #+Max shots has no other affect
            self.max_primary_shots  = amount
        elif field == MOD_MAX_RANGE:                        #+Max Range only applies to new shots fired
            self.max_primary_range  = amount
        elif field == MOD_MAX_AMMO:                         #+Max ammo also increases cur ammo by amount gained
            cur_max                 = self.max_primary_ammo
            new_max                 = amount
            max_dif                 = new_max - cur_max     #How much ammo are we gaining
            self.max_primary_ammo   = amount
            self.cur_primary_ammo  += max_dif
        elif field == MOD_MAX_AUX_AMMO:                     #+Max aux ammo also increases cur aux ammo by same amount
            cur_max                 = self.max_aux_ammo
            new_max                 = amount
            max_dif                 = new_max - cur_max     #How much ammo are we gaining
            self.max_aux_ammo       = amount
            self.cur_aux_ammo      += max_dif
        elif field == MOD_SHOT_TIME:                        #-CD between shots and also reduces current CD
            cur_cd                  = self.primary_cd
            new_cd                  = amount
            cd_dif                  = cur_cd - new_cd       #how much faster does it CD
            if cur_cd <= 1:
                cd_dif              = 0                     #If we're already ready to fire again, don't change CD
            self.primary_cd         = amount
            self.primary_cd_time   -= (cd_dif * FRAME_RATE) #This should reduce it by 1-2 seconds
        elif field == MOD_AUX_WEAPON:                       #Changing auxillary weapon does not change aux_ammo
            self.aux_weapon         = amount
        elif field == MOD_AUX_SPEED:                        #changing aux_weapon travel speed only applies to new shots fired
            self.aux_weapon_speed   = amount
        else:
            debug("Unknown mod field #%d." % field )
        #fi
        return
        
    def __str__( self ):
        """String representation of our tanks status"""
        output = ( "%s's tank has %d/%d hp, %d/%d shields, %d/%d energy, %d/%d bullets, %d/%d auxammo"
        % ( self.name,
            self.cur_health, self.max_health,
            self.cur_shield, self.max_shield,
            self.cur_energy, self.max_energy,
            self.cur_primary_ammo, self.max_primary_ammo,
            self.cur_aux_ammo, self.max_aux_ammo ) )
        return output            

    def Set_Image( self, image, facing ):
        rotDegrees          = facing - self.def_facing
        #tempSurface         = pygame.Surface( ( 64, 64 ) )
        #tempSurface.blit( image, ( 0, 0 ) )
        #tempSurface         = pygame.transform.rotate( tempSurface, rotDegrees )
        #self.image          = tempSurface
        #self.rect           = self.image.get_rect()
        #self.rect.center    = self.position
        self.image          = self.rot_center( self.icon, -rotDegrees )

    def Accelerate( self ):
        """ Accelerates a tank based on it's current facing and speedMod """
        """ Based off of calcVector from carVec.py book example """
        
        workFacing          = self.facing - 90
        radians             = workFacing * math.pi / 180
        work_dx             = math.cos(radians)
        work_dy             = math.sin(radians)
        
        work_dx            *= SPEED_DELTA
        work_dy            *= SPEED_DELTA
        energy_cost         = 0.0
        energy_cost         = -( abs( work_dx ) + abs( work_dy ) )
        energy_cost        /= 4.0

        if ( self.dx + work_dx ) > SPEED_MAX:
            work_dx         = SPEED_MAX - self.dx
        if ( self.dx + work_dx ) < -SPEED_MAX:
            work_dx         = -SPEED_MAX + self.dx
        if ( self.dy + work_dy ) > SPEED_MAX:
            work_dy         = SPEED_MAX - self.dy
        if ( self.dy + work_dy ) < -SPEED_MAX:
            work_dy         = -SPEED_MAX + self.dy
        
        if ( work_dx == 0 ) and ( work_dy == 0 ):
            return
            
        if self.cur_energy == 0:
            return            
        elif self.cur_energy < energy_cost:
            while energy_cost > self.cur_energy:
                work_dx    *= .9
                work_dy    *= .9
                energy_cost = -( abs( work_dx ) + abs( work_dy ) )
                energy_cost /= 4.0
                if abs( work_dx ) < 0.1:
                    work_dx = 0.0
                if abs( work_dy ) < 0.1:
                    work_dy = 0.0
                if ( work_dx == 0 ) and ( work_dy == 0 ):
                    return
        
        self.dx            += work_dx
        self.dy            += work_dy

        if self.dx > SPEED_MAX:
            self.dx         = SPEED_MAX
        if self.dx < -SPEED_MAX:
            self.dx         = -SPEED_MAX
        if self.dy > SPEED_MAX:
            self.dy         = SPEED_MAX
        if self.dy < -SPEED_MAX:
            self.dy         = -SPEED_MAX

        self.harm_tank( energy_cost, MINOR_ENERGY_FLUX, self )
        #debug("wX:%2.2f wY:%2.2f" % ( work_dx, work_dy ))
        #debug("dX:%2.2f dY:%2.2f" % ( self.dx, self.dy ))

    def Decelerate( self ):
        """ Decelerates a tank """

        work_dx = -self.dx * .05
        work_dy = -self.dy * .05

        energy_cost         = 0.0
        energy_cost         = -( abs( work_dx ) + abs( work_dy ) )
        energy_cost        /= 4.0        
        
        if abs(self.dx) <= SPEED_DELTA:
            work_dx = -self.dx
        if abs(self.dy) <= SPEED_DELTA:
            work_dy = -self.dy

        if self.cur_energy == 0:
            return            
        elif self.cur_energy < energy_cost:
            while energy_cost > self.cur_energy:
                work_dx    *= .9
                work_dy    *= .9
                energy_cost = -( abs( work_dx ) + abs( work_dy ) )
                energy_cost /= 4.0
                if abs( work_dx ) < 0.1:
                    work_dx = 0.0
                if abs( work_dy ) < 0.1:
                    work_dy = 0.0
                if ( work_dx == 0 ) and ( work_dy == 0 ):
                    return
  
        self.dx += work_dx
        self.dy += work_dy

        self.harm_tank( energy_cost, MINOR_ENERGY_FLUX, self )
        #debug("Trying to decelerate from %2.2f/%2.2f by %2.2f/%2.2f." % ( self.dx, work_dx, self.dy, work_dy ) )

    def Charge_Shields( self ):
        work_amt        = self.shield_charge_rate               # how many shields gained when charged once
        work_cost       = self.shield_charge_cost               # how much energy consumed to charge shields
        
        if self.cur_energy < work_cost:                         # insufficient energy, cancel        
            return
        if self.cur_shield + work_amt >= self.max_shield:       # already charged to near full
            return
        if self.shield_charge_time > 0:                         # we recently charged, waiting a moment
            return

        # we have the energy, we have non-full shields...let's charge!
        self.harm_tank( work_amt, SHIELD_FLUX, self )     # boost shields
        self.harm_tank( -work_cost, ENERGY_FLUX, self )    # expend energy        
        self.shield_charge_time     = FRAME_RATE                # Defaulting to 1 second between charges
        
    def rot_center( self, image, angle):
        """rotate an image while keeping its center and size"""
        """code from pygame.org/docs/transform.html"""
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
        
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
            
    def rotateTank( self, clockwise = True ):
        if ( clockwise ):
            self.facing += ROT_RATE
        else:
            self.facing -= ROT_RATE
        
        if ( self.facing > 359 ):
            self.facing -= 360
        
        if ( self.facing < 0 ):
            self.facing += 360
         
        self.Set_Image( self.image, self.facing )

    def scan_keys( self ):
       
        KeyDown = pygame.key.get_pressed() #Now going to scan player keys and handle that
        # first which player are we scanning...
        ScanKeys = []
        if self.player == 1 or self.player == 3:
            ScanKeys = PLAYER_1_KEYS
        elif self.player == 2 or self.player == 4:
            ScanKeys = PLAYER_2_KEYS
            
        self.pAction = False     # Storage to see if we have done an action this check?
        if self.pAction:
            pass            # We've done an action, stop looking
        if KeyDown[ScanKeys[P_ACCEL]]:           #accel tank
            self.Accelerate()
            self.pAction = True
        if KeyDown[ScanKeys[P_DECEL]]:           #decel tank
            self.Decelerate()
            self.pAction = True
        if KeyDown[ScanKeys[P_TURN_LEFT]]:       #turn tank left
            self.rotateTank(False)
            self.pAction = True
        if KeyDown[ScanKeys[P_TURN_RIGHT]]:      #turn tank right
            self.rotateTank(True)
            self.pAction = True
        if KeyDown[ScanKeys[P_FIRE_MAIN]]:       #fire tank's main guns
            tankCombat.Determine_Shot( self, FIRE_PRIMARY )
            self.pAction = True
        if KeyDown[ScanKeys[P_FIRE_AUX]]:        #fire tank's aux guns
            tankCombat.Determine_Shot( self, FIRE_AUXILLARY )
            self.pAction = True
        if KeyDown[ScanKeys[P_CHARGE_SHIELD]]:  #charge tank shields
            #tankNotify.Notification( self.screen, "+"+str(self.player)+" Shields", 18, 5, ( 320, 240 ), clr_PURPLE, ( 2, -2) )
            self.Charge_Shields()
            self.pAction = True
 
    def timer_cd( self ):
        """ This functions just reduces timers to 0 and triggers their effects"""
        second_pulsed               = False         # sadly we really only use this to track HP regen because it heals in 1-3 seconds but drains energy every second
        self.second_timer          -= 1
        delta_energy                = 0             # this tracks energy regen
        delta_hp                    = 0             # this could allow for 'poison' effects

        if self.second_timer <= 0:                  # is this a 1 second mark since tank birth?
            second_pulsed           = True          # It is! 
            self.second_timer       = FRAME_RATE    # Refresh time till next second mark

        if self.primary_cd_time > 0:                # this goes to 0 then waits till shot is fired
            self.primary_cd_time   -= 1             # Cur time till next primary shot available
            
        if self.aux_cd_time > 0:                    # this goes to 0 then waits till shot is fired
            self.aux_cd_time       -= 1             # cur time till next auxillary shot available

        if self.shield_charge_time  > 0:            # time till next shield charge available
            self.shield_charge_time -= 1
            
        self.energy_charge_time    -= 1             # cur time till next energy charge pulse
            
        if self.health_regen_rate > 0:              # only decrement health regen timer if we can regen health
            self.health_regen_time -= 1             # cur time till next health regen pulse
            
            if self.cur_health < self.max_health:   # We only trigger when hurt
                if second_pulsed:
                    if self.cur_energy >= 1:        # if we don't have 3 energy but we won't burn off the energy
                        delta_energy   -= 1         # It costs 1 energy per second to regen health
#                        delta_energy   -= 3         # It costs 3 energy per second to regen health
                    else:
                        #delta_energy = self.cur_energy
                        self.health_regen_time += FRAME_RATE    # And the next healing pulse is pushed back 1 second

                if self.health_regen_time <= 0:         # Ok we have a regen pulse waiting...
                    self.health_regen_time  = FRAME_RATE * self.health_regen_rate
                    delta_hp           += 1             # We regen 1 hp every X seconds                
                            
        if self.energy_charge_time <= 0:            # hooray we get more energy!
            self.energy_charge_time = FRAME_RATE    # energy pulses once a second 
            delta_energy           += self.energy_charge_rate
            if ( delta_energy + self.cur_energy ) > self.max_energy:
                delta_energy = self.max_energy - self.cur_energy

        if self.cur_shield > 0:                     # shields only decay while charged
            self.shield_decay_time -= 1             # cur time till next shield decay pulse
            if self.shield_decay_time <= 0:         # awww our shield drained
                self.shield_decay_time = FRAME_RATE * self.shield_decay_rate
                self.cur_shield    -= 1
                debug("P%1d Shield drained by 1, %d remain, next decay in %d" % ( self.player, self.cur_shield, self.shield_decay_time) )
        
        if delta_energy != 0:
            self.harm_tank( delta_energy, MINOR_ENERGY_FLUX, self )
        if delta_hp != 0:
            self.harm_tank( delta_hp, HEALTH_FLUX, self )
        #That should be all the timers
        
    def update( self ):
        if self.state == "EXPLODING":
            if self.state_time > 0:
                self.state_time -= 1
                if self.state_time <= 0:
                    self.state_time = FRAME_RATE / 6
                    self.state_frame += 1
                    if self.state_frame > self.state_max_frame:     # are we done animating explosion?
                        self.icon = self.orig_icon
                        self.state = "NORMAL"                       # go back to normal state
                        self.respawn_tank()                         # and we respawn
                    else:
                        self.icon        = self.Load_Icon( DEAD_TANK[self.state_frame] )
                    self.Set_Image( self.icon, self.facing )        # either way we set our facing properly
                #fi
            #fi
            return
        #fi
                       
        self.timer_cd()
        self.scan_keys()
        self.rect.centery += self.dy
        self.rect.centerx += self.dx
        l_boundX = MAIN_SCREEN.left
        l_boundY = MAIN_SCREEN.top
        u_boundX = MAIN_SCREEN.right
        u_boundY = MAIN_SCREEN.bottom

        if self.rect.bottom >= u_boundY:
            self.rect.top = l_boundY + 1
        if self.rect.top <= l_boundY:
            self.rect.bottom = u_boundY - 1
        if self.rect.right >= u_boundX:
            self.rect.left = l_boundX + 1
        if self.rect.left <= l_boundX:
            self.rect.right = u_boundX - 1
                
    def harm_tank( self, damage, type = DAM_NONE, damageSource = "None" ):
        """ this function actually does damage to the tank based on the type"""
        if type == DAM_NONE:        # no valid damage, leaving
            dam_type = "None"
            return
        if damageSource == "None":  # no valid damage source, leaving
            dam_type = "None"
            return
        if self.state == "EXPLODING":   #already exploding don't register more damage
            dam_type = "None"
            return
        base_damage     = damage
        shield_delta    = 0
        armor_delta     = 0
        energy_delta    = 0
            
        if IS_SET( type, DAM_COLLISION ):   # ok Collision Damage only ever impacts armor
            armor_delta -= damage           # track the damage we've done            
            self.cur_health -= damage       # do damage to armor
            damage -= damage                # collisions do not have any residual damage
            dam_type = "Collision"

        if IS_SET( type, DAM_BULLET ):      # Bullets do normal damage to shields and carries thru to armor
            if self.cur_shield >= damage:   # Shields present that can stop all the damage
                shield_delta -= damage
                self.cur_shield -= damage
                damage -= damage
            elif self.cur_shield > 0:       # shields present that can stop some of the damage
                shield_delta -= self.cur_shield
                damage -= self.cur_shield
                self.cur_shield = 0
            armor_delta -= damage
            self.cur_health -= damage       # do any remaining damage to armor
            damage -= damage
            dam_type = "Bullet"
        
        if IS_SET( type, DAM_MISSILE ):     # missiles do 25% less damage to shielded targets
            if self.cur_shield > 0:         # they will do full damage to non-shielded
                damage -= ( damage / 4 )    # missile damage will carry thru shields
            if self.cur_shield >= damage:   # shields present that can stop all the damage
                shield_delta -= damage
                self.cur_shield -= damage
                damage -= damage
            elif self.cur_shield > 0:       # shields present that can absorb some of the damage
                shield_delta -= self.cur_shield
                damage -= self.cur_shield
                self.cur_shield = 0
            armor_delta -= damage
            self.cur_health -= damage       # do any remaining damage to armor
            damage -= damage
            dam_type = "Missile"
            
        if IS_SET( type, DAM_SHIELD_PEN ):  # Shield penetrators do 25% less damage to shields & shielded targets but always deal 25% damage to a target
            pen_damage = ( damage / 4 )     # guaranteed 25% damage to armor
            armor_delta -= pen_damage
            self.cur_health -= pen_damage   # pen_damage is dealt first        
            damage -= pen_damage            
            
            if self.cur_shield > 0:         # reduce damage for hitting a shielded target
                damage -= ( damage / 4 )
            
            if self.cur_shield >= damage:   # shields present that can stop all the damage
                shield_delta -= damage
                self.cur_shield -= damage
                damage -= damage
            elif self.cur_shield > 0:       # shields present that can stop some of the damage
                shield_delta -= self.cur_shield
                damage -= self.cur_shield
                self.cur_shield = 0
            armor_delta -= damage
            self.cur_health -= damage       # do any remaining damage to armor
            damage -= damage
            dam_type = "Shield Penetrator"
        
        if IS_SET( type, DAM_LEECH ):       # leeches do all damage to energy and reduce by 50% shields
            shield_delta -= self.cur_shield / 2
            energy_delta -= damage
            self.cur_shield /= 2
            self.cur_energy -= damage
            damage -= damage
            dam_type = "Leech"
        
        if IS_SET( type, DAM_TORPEDO ):     # torpedoes are 50% more efficient at destroying shields but deal 25% less damage to armor
            shield_damage = 0
            if self.cur_shield > 0:         # if there are shields, compute how much potential is consumed to destroy them
                shield_damage = self.cur_shield / (3/2)
                while ( shield_damage * 1.5 ) < self.cur_shield:
                    shield_damage += 1      # consumes 2 potential for every 3 shields or portion there of
            if shield_damage > damage:      # make sure that potential used only equals at most potential we started with
                shield_damage = damage
            
            if self.cur_shield > 0:         # Shielded target
                shield_delta -= shield_damage * 1.5
                self.cur_shield -= shield_damage * 1.5
                damage -= shield_damage     # reduce remaining damage accordingly
            
            damage -= ( damage / 4 )        # torpedoes deal 25% less damage to armor
            armor_delta -= damage
            self.cur_health -= damage       # do any remaining damage to armor
            damage -= damage
            dam_type = "Torpedo"
        
        if IS_SET( type, DAM_MINE ):        # mines deal +25% damage to unshielded targets
            if self.cur_shield == 0:        # no shields present
                damage += ( damage / 4 )    # bonus damage
            elif self.cur_shield >= damage: # shields present that can stop all the damage
                shield_delta -= damage
                self.cur_shield -= damage
                damage -= damage
            elif self.cur_shield > 0:       # shields present that can stop some of the damage
                shield_delta -= self.cur_shield
                damage -= self.cur_shield
                self.cur_shield = 0
             
            armor_delta -= damage
            self.cur_health -= damage       # do any remaining damage to armor
            damage -= damage
            dam_type = "Prox Mine"
            
        # now good "harm"
        if IS_SET( type, MINOR_ENERGY_FLUX ):     # Minor Energy flux's do NOT echo to screen
            self.cur_energy += damage       # this will typically result in energy gain, not loss
            damage -= damage                # hehe "damage"
            if base_damage >= 0:
                dam_type = "Energy Charge"
            else:
                dam_type = "Energy Drain"

        if IS_SET( type, ENERGY_FLUX ):
            energy_delta    += damage
            self.cur_energy += damage       # this will typically result in energy gain, not loss
            damage -= damage                # hehe "damage"
            if base_damage >= 0:
                dam_type = "Energy Charge"
            else:
                dam_type = "Energy Drain"

        if IS_SET( type, HEALTH_FLUX ):
            armor_delta += damage
            self.cur_health += damage       # this will typically result in health gain, not loss
            damage -= damage                # Woohoo more "damage"
            if base_damage >= 0:
                dam_type = "Health Regen"
            else:
                dam_type = "Health Drain"

        if IS_SET( type, SHIELD_FLUX ):
            shield_delta += damage
            self.cur_shield += damage       # this will typically result in shield gain, not loss
            damage -= damage                # Woohoo more "damage"
            if base_damage >= 0:
                dam_type = "Shield Regen"
            else:
                dam_type = "Shield Drain"
        

        # now let's print some numbers, 0 amounts do not get echoed
        if self.dx > 0:
            txtDx = 2
        elif self.dx == 0:
            txtDx = 0
        else:
            txtDx = -2
        displaySize = 20
        txtDy = -2
        txtLoc = self.rect.midtop
        if ( self.rect.top - ( self.rect.height + displaySize + 4 ) ) < 1:
            txtDy = 2
            txtLoc = ( self.rect.centerx, self.rect.bottom + displaySize )
            
        if armor_delta > 0:
            outString = "+%d AP" % ( armor_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_GREEN, ( txtDx, txtDy ) )
        elif armor_delta < 0:
            outString = "%d AP" % ( armor_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_RED, ( txtDx, txtDy ) )
        
        if shield_delta > 0:
            outString = "+%d SP" % ( shield_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_GREEN, ( txtDx, txtDy ) )
        elif shield_delta < 0:
            outString = "%d SP" % ( shield_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_RED, ( txtDx, txtDy ) )
        
        if energy_delta > 0:
            outString = "+%d EP" % ( energy_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_YELLOW, ( txtDx, txtDy ) )
        elif energy_delta < 0:
            outString = "%d EP" % ( energy_delta )
            Notify.Notification( self.screen, outString, displaySize, 3, txtLoc, clr_YELLOW, ( txtDx, txtDy ) )
        
        # damage is dealt to let's make sure things are within bounds and handle deaths.
        if self.cur_health < 1:                 # health can't go below 1
            self.explode( damageSource )        # blow the tank up

        if self.cur_health > self.max_health:   # health can't go above max
            #self.explode( damageSource )       # blow the tank up!  MUHAHAH....just kidding.
            self.cur_health = self.max_health

        if self.cur_energy < 0:                 # energy can't go below 0
            self.cur_energy = 0

        if self.cur_energy > self.max_energy:   # energy can't go above max
            self.cur_energy = self.max_energy
            
        if self.cur_shield < 0:                 # shields can't go below 0
            self.cur_shield = 0

        if self.cur_shield > self.max_shield:   # shields can't go above max
            self.cur_shield = self.max_shield
        """
        if base_damage < 0:
            debug ("P%1d tank - HP:%2d/%2d   SP:%2d/%2d  EP:%2d/%2d afer taking %3d base %s damage from P%1d." % ( self.player, self.cur_health, self.max_health, self.cur_shield, self.max_shield, self.cur_energy, self.max_energy, base_damage, dam_type, damageSource.player ) )
        else:
            debug ("P%1d tank - HP:%2d/%2d   SP:%2d/%2d  EP:%2d/%2d afer receiving %3d base %s from P%1d." % ( self.player, self.cur_health, self.max_health, self.cur_shield, self.max_shield, self.cur_energy, self.max_energy, base_damage, dam_type, damageSource.player ) )
        """

    def explode( self, scorer ):
        # now let's print some scoreboard stuff (only here temporarily)
        if self.dx > 0:
            txtDx = 3
        elif self.dx == 0:
            txtDx = 0
        else:
            txtDx = -3
        displaySize = 32
        txtDy = -3
        txtLoc = scorer.rect.midtop
        if ( scorer.rect.top - ( scorer.rect.height + displaySize + 4 ) ) < 1:
            txtDy = 3
            txtLoc = ( scorer.rect.centerx, scorer.rect.bottom + displaySize )

        if scorer == self:                  # suicide?
            outString = "-1 Kill"
            Notify.Notification( scorer.screen, outString, displaySize, 3, txtLoc, clr_RED, ( txtDx, txtDy ) )
            scorer.score.modify_score( -1 )
            if scorer.score.score < 0:
                scorer.score.score = 0
        else:
            outString = "+1 Kill"
            Notify.Notification( scorer.screen, outString, displaySize, 3, txtLoc, clr_GREEN, ( txtDx, txtDy ) )
            scorer.killtank_bonus()           # Give them a bonus for killing us.
            scorer.score.modify_score( 1 )
            
        debug ("P%1d blew up P%1d's tank!  Oh well, better luck next spawn." % ( scorer.player, self.player ) )
        tankSFX = tankSound.gameSound()
        if random.randrange(1,5) > 2:
            tankSFX.Play_Sound( "explosion2" )
        else:
            tankSFX.Play_Sound( "explosion" )
            
        self.state              = "EXPLODING"
        self.state_time         = ( FRAME_RATE / 6 )
        self.state_max_frame    = DEAD_TANK[0]
        self.state_frame        = 1
        self.icon               = self.Load_Icon( DEAD_TANK[self.state_frame] )
        self.Set_Image( self.icon, self.facing )
        
    def respawn_tank( self ):
        w_m64 = self.screen.get_width()
        w_m64 = w_m64 - ( w_m64 % 64 )      # screen width evenly disible by 64
        h_m64 = self.screen.get_height()
        h_m64 = w_m64 - ( w_m64 % 64 )      # screen height evenly disible by 64
        
        randX = random.randrange( 64, w_m64, 64)
        randY = random.randrange( 64, h_m64, 64)
        self.dx           = 0.0
        self.dy           = 0.0
        self.rect.centerx = randX
        self.rect.centery = randY
        self.clear_stats()
        self.base_equip()
    
    def crate_bonus( self, secondChance = False ):
        if self.dx > 0:
            txtDx = 3
        elif self.dx == 0:
            txtDx = 0
        else:
            txtDx = -3
        displaySize = 20
        txtDy = -3
        txtLoc = self.rect.midtop
        if ( self.rect.top - ( self.rect.height + displaySize + 4 ) ) < 1:
            txtDy = 3
            txtLoc = ( self.rect.centerx, self.rect.bottom + displaySize )

        deltaString = "Crate Bonus!"
        randLoot = random.randrange( 1, 100 )
        debug("Random Loot: %d" % randLoot )
        # most common loots: ammunition ( 42 slots )
        if   randLoot >= 41 and randLoot <= 62:     # bullets (22 slots)
            deltaAmount = random.randrange(8,24)
            if ( self.cur_primary_ammo + deltaAmount ) > self.max_primary_ammo:
                deltaAmount = self.max_primary_ammo - self.cur_primary_ammo
            if deltaAmount == 0:
                deltaString = "Nothing."
            else:
                deltaString = "+%d Bullets" % deltaAmount
            self.cur_primary_ammo += deltaAmount
        elif ( randLoot >= 31 and randLoot <= 40 ) or ( randLoot >= 63 and randLoot <= 72 ): # Special Ammo (20 slots)
            deltaAmount = random.randrange(1,7)
            if ( self.cur_aux_ammo + deltaAmount ) > self.max_aux_ammo:
                deltaAmount = self.max_aux_ammo - self.cur_aux_ammo
            if deltaAmount == 0:
                deltaString = "Nothing."
            else:
                deltaString = "+%d Aux Ammo" % deltaAmount
            self.cur_aux_ammo += deltaAmount
        # generators are 1-30 - 10% chance per
        elif ( randLoot >= 21 and randLoot <= 30 ): # Energy
            didUpgrade = tankUpgrade.equip_upgrade( self, "ENERGY_GEN", self.upgrades.energy_gen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Faster Energy Gain."
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 11 and randLoot <= 20 ): # Shields
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHIELD_GEN", self.upgrades.shield_gen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Slower Shield Drain"
            else:
                deltaString = "Nothing."
        elif ( randLoot >=  1 and randLoot <= 10 ):  # Health
            didUpgrade = tankUpgrade.equip_upgrade( self, "REPAIR", self.upgrades.regen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Faster Armor Repair"
            else:
                deltaString = "Nothing."
        # other boosts are 73-100 - 4% chance per
        elif ( randLoot >= 73 and randLoot <=  76 ): # Ammo (more of both types of shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "AMMO", self.upgrades.ammo_rank + 1 )
            if didUpgrade:
                deltaString = "Max Ammo Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 77 and randLoot <=  80 ): # Hull (more hp)
            didUpgrade = tankUpgrade.equip_upgrade( self, "HULL", self.upgrades.hull_rank + 1 )
            if didUpgrade:
                deltaString = "Max Armor Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 81 and randLoot <=  84 ): # Energy Tank (more energy)
            didUpgrade = tankUpgrade.equip_upgrade( self, "ENERGY_TANK", self.upgrades.energy_rank + 1 )
            if didUpgrade:
                deltaString = "Max Energy Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 85 and randLoot <=  88 ): # Shield Cap (more shields)
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHIELD_CAP", self.upgrades.shield_rank + 1 )
            if didUpgrade:
                deltaString = "Max Shields Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 89 and randLoot <=  92 ): # Cannon (more max shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "CANNON", self.upgrades.cannon_rank + 1 )
            if didUpgrade:
                deltaString = "Max Shots Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 93 and randLoot <=  96 ): # Shot CD (faster shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHOT_CD", self.upgrades.shot_cd_rank + 1 )
            if didUpgrade:
                deltaString = "Rapid Fire Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 97 and randLoot <= 100 ): # weaponsystem
            randWeapon = random.randrange(1,10)
            if   ( randWeapon >= 1 and randWeapon <=  2 ):
                newAux = AUX_1
            elif ( randWeapon >= 3 and randWeapon <=  4 ):
                newAux = AUX_2
            elif ( randWeapon >= 5 and randWeapon <=  6 ):
                newAux = AUX_3
            elif ( randWeapon >= 7 and randWeapon <=  8 ):
                newAux = AUX_4
            elif ( randWeapon >= 9 and randWeapon <= 10 ):
                newAux = AUX_5
        
            if newAux == self.aux_weapon:   # we have the weapon, attempt to rank it up
                oldRank = self.upgrades.aux_rank
                self.upgrades.aux_rank += 1
                if self.upgrades.aux_rank >= 3:
                    if ( self.aux_weapon >= AUX_3 ) and (self.aux_weapon <= AUX_5 ):
                        self.upgrades.aux_rank = 2
                if self.upgrades.aux_rank >= 4:
                    self.upgrades.aux_rank = 3
                diffRank = self.upgrades.aux_rank - oldRank
                if diffRank < 1:
                    diffRank = 0
                if diffRank == 0:
                    deltaString = "Nothing."
                else:
                    deltaString = "Aux Weapon Power-Up!"
            else:                           # new aux weapon...
                if   newAux == AUX_1:
                    newSystem = "Missiles"
                elif newAux == AUX_2:
                    newSystem = "Shield Pen Missiles"
                elif newAux == AUX_3:
                    newSystem = "Leech Missiles"
                elif newAux == AUX_4:
                    newSystem = "Plasma Torpedoes"
                elif newAux == AUX_5:
                    newSystem = "Proximity Mines"
                tankUpgrade.equip_upgrade( self, newSystem )
                deltaString = "%s Equipped!" % newSystem
            #fi
        #fi
        #print out what we got
        debug("Crate Bonus: %s" % deltaString )
        #let's be nice
        if deltaString == "Nothing." and not secondChance:       # awwww 
            self.crate_bonus( True )                             # flag this as a second chance
        else:
            Notify.Notification(self.screen, deltaString, displaySize, 3, txtLoc, clr_CYAN, ( txtDx, txtDy ) )
    #fed crate_bonus
                
    def killtank_bonus( self, secondChance = False ):
        """ this function ONLY gives upgrades to the tank."""
        if self.dx > 0:
            txtDx = 3
        elif self.dx == 0:
            txtDx = 0
        else:
            txtDx = -3
        displaySize = 20
        txtDy = -3
        txtLoc = self.rect.midtop
        if ( self.rect.top - ( self.rect.height + displaySize + 4 ) ) < 1:
            txtDy = 3
            txtLoc = ( self.rect.centerx, self.rect.bottom + displaySize )

        deltaString = "Kill Tank  Bonus!"
        randLoot = random.randrange( 1, 100 )
        debug("Random Loot: %d" % randLoot )

        # generators are 1-44 - 15% chance per but repairs which are 14%
        if ( randLoot >= 30 and randLoot <= 44 ): # Energy
            didUpgrade = tankUpgrade.equip_upgrade( self, "ENERGY_GEN", self.upgrades.energy_gen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Faster Energy Gain."
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 15 and randLoot <= 29 ): # Shields
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHIELD_GEN", self.upgrades.shield_gen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Slower Shield Drain"
            else:
                deltaString = "Nothing."
        elif ( randLoot >=  1 and randLoot <= 14 ):  # Health
            didUpgrade = tankUpgrade.equip_upgrade( self, "REPAIR", self.upgrades.regen_rank + 1 )
            if didUpgrade:
                deltaString = "Upgrade! Faster Armor Repair"
            else:
                deltaString = "Nothing."
        # other boosts are 45-100 , 7% chance per for all but weapons which are 14%
        elif ( randLoot >= 59 and randLoot <=  65 ): # Ammo (more of both types of shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "AMMO", self.upgrades.ammo_rank + 1 )
            if didUpgrade:
                deltaString = "Max Ammo Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 66 and randLoot <=  72 ): # Hull (more hp)
            didUpgrade = tankUpgrade.equip_upgrade( self, "HULL", self.upgrades.hull_rank + 1 )
            if didUpgrade:
                deltaString = "Max Armor Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 73 and randLoot <=  79 ): # Energy Tank (more energy)
            didUpgrade = tankUpgrade.equip_upgrade( self, "ENERGY_TANK", self.upgrades.energy_rank + 1 )
            if didUpgrade:
                deltaString = "Max Energy Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 80 and randLoot <=  86 ): # Shield Cap (more shields)
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHIELD_CAP", self.upgrades.shield_rank + 1 )
            if didUpgrade:
                deltaString = "Max Shields Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 87 and randLoot <=  93 ): # Cannon (more max shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "CANNON", self.upgrades.cannon_rank + 1 )
            if didUpgrade:
                deltaString = "Max Shots Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 94 and randLoot <=  100 ): # Shot CD (faster shots)
            didUpgrade = tankUpgrade.equip_upgrade( self, "SHOT_CD", self.upgrades.shot_cd_rank + 1 )
            if didUpgrade:
                deltaString = "Rapid Fire Upgrade!"
            else:
                deltaString = "Nothing."
        elif ( randLoot >= 45 and randLoot <= 58 ): # weaponsystem
            randWeapon = random.randrange(1,10)
            if   ( randWeapon >= 1 and randWeapon <=  2 ):
                newAux = AUX_1
            elif ( randWeapon >= 3 and randWeapon <=  4 ):
                newAux = AUX_2
            elif ( randWeapon >= 5 and randWeapon <=  6 ):
                newAux = AUX_3
            elif ( randWeapon >= 7 and randWeapon <=  8 ):
                newAux = AUX_4
            elif ( randWeapon >= 9 and randWeapon <= 10 ):
                newAux = AUX_5
        
            if newAux == self.aux_weapon:   # we have the weapon, attempt to rank it up
                oldRank = self.upgrades.aux_rank
                self.upgrades.aux_rank += 1
                if self.upgrades.aux_rank >= 3:
                    if ( self.aux_weapon >= AUX_3 ) and (self.aux_weapon <= AUX_5 ):
                        self.upgrades.aux_rank = 2
                if self.upgrades.aux_rank >= 4:
                    self.upgrades.aux_rank = 3
                diffRank = self.upgrades.aux_rank - oldRank
                if diffRank < 1:
                    diffRank = 0
                if diffRank == 0:
                    deltaString = "Nothing."
                else:
                    deltaString = "Aux Weapon Power-Up!"
            else:                           # new aux weapon...
                if   newAux == AUX_1:
                    newSystem = "Missiles"
                elif newAux == AUX_2:
                    newSystem = "Shield Pen Missiles"
                elif newAux == AUX_3:
                    newSystem = "Leech Missiles"
                elif newAux == AUX_4:
                    newSystem = "Plasma Torpedoes"
                elif newAux == AUX_5:
                    newSystem = "Proximity Mines"
                tankUpgrade.equip_upgrade( self, newSystem )
                deltaString = "%s Equipped!" % newSystem
            #fi
        #fi
        #print out what we got
        debug("Kill Tank Bonus: %s" % deltaString )
        #let's be nice
        if deltaString == "Nothing." and not secondChance:       # awwww 
            self.killtank_bonus( True )                          # flag this as a second chance
        else:
            if deltaString != "Nothing.":
                Notify.Notification(self.screen, deltaString, displaySize, 3, txtLoc, clr_CYAN, ( txtDx, txtDy ) )
            else:
                debug("Nothing awarded for kill bonus, oh well.")
    #fed killtank_bonus
            
                
def main():
    global p1Tank
    tankScreen = pygame.display.set_mode((640,480))
    p1Tank = tankPlayer( tankScreen, "Random", 1, ( 200, 200 ), "Simple Tank_1" )
    
if __name__ == "__main__":
    main()
    
        
