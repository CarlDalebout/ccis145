"""
    This module contains what is needed to handle combat for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame, math
import tankBullets, tankMissiles, tankTorpedoes, tankMines
from tankGlobals import *

def Determine_Shot( whichTank, whichSystem ):
    """ This is a single function used to determine what shot is being fired and to fire it. """
    #These are used to fire the shot
    theTank     = whichTank
    theScreen   = whichTank.screen
    theP_Rank   = whichTank.upgrades.cannon_rank
    theA_Rank   = whichTank.upgrades.aux_rank
    theA_Weapon = whichTank.aux_weapon
    theA_Speed  = whichTank.aux_weapon_speed
    theShotLife = whichTank.max_shot_life
    thePRange   = whichTank.max_primary_range
    theARange   = whichTank.max_aux_range
    theFacing   = whichTank.facing
    thePosition = whichTank.rect.center

    #These are used to verify if a shot can be fired
    theEnergy   = whichTank.cur_energy
    theCurPShot = whichTank.cur_primary_shots
    theMaxPShot = whichTank.max_primary_shots
    theCurAShot = whichTank.cur_aux_shots
    theMaxAShot = whichTank.max_aux_shots
    theP_CD     = whichTank.primary_cd_time
    theA_CD     = whichTank.aux_cd_time
    theP_Ammo   = whichTank.cur_primary_ammo
    theA_Ammo   = whichTank.cur_aux_ammo
    
    if whichSystem == FIRE_PRIMARY:
        # Preparing to fire main battery
        if theP_CD > 0:                   # Primary cannon still on Cooldown, cancel
            return
        if theCurPShot >= theMaxPShot:    # To many primary shots on screen, cancel
            return
        if theEnergy < PRIMARY_COST:      # Insufficient energy to fire cannon, cancel
            return
        if theP_Ammo < 1:                 # insufficient ammunition remaining
            return
        # OK we weren't on CD, we have a shot 'slot' remaining, and we have enough energy, charge the shot and fire it
        # We have to charge the energy cost up here, but the ammo, shot slot and CD time are charged in the tankWeapon system
        #theTank.cur_energy -= PRIMARY_COST
        theTank.harm_tank( -PRIMARY_COST, ENERGY_FLUX, theTank )    # expend energy        
        tankBullets.tankBullet( theScreen, theP_Rank, theTank, theShotLife, thePRange, theFacing, thePosition )                
    elif whichSystem == FIRE_AUXILLARY:
        # Preparing to fire aux batteries
        if theA_CD > 0:                   # Auxillary systems still on Cooldown, cancel
            return
        if theCurAShot >= theMaxAShot:    # To many auxillary shots on screen, cancel
            return
        if theEnergy < AUXILLARY_COST:    # Insufficient energy to fire cannon, cancel
            return
        if theA_Ammo < 1:                 # insufficient ammunition remaining
            return
        # OK we weren't on CD, we have a shot 'slot' remaining, and we have enough energy, charge the shot and fire it
        # We have to charge the energy cost up here, but the ammo, shot slot and CD time are charged in the tankWeapon system
        #theTank.cur_energy -= AUXILLARY_COST        
        theTank.harm_tank( -AUXILLARY_COST, ENERGY_FLUX, theTank )    # expend energy                
        # now to figure out which aux weapon to fire and fire it
        if   theA_Weapon == AUX_1:        # Missiles
            tankMissiles.tankMissile( theScreen, theA_Rank, theTank, theA_Speed, theShotLife, theARange, theFacing, thePosition )
        elif theA_Weapon == AUX_2:        # Shield Pens
            tankMissiles.tankShieldPen( theScreen, theA_Rank, theTank, theA_Speed, theShotLife, theARange, theFacing, thePosition )
        elif theA_Weapon == AUX_3:        # Leeches
            tankMissiles.tankLeech( theScreen, theA_Rank, theTank, theA_Speed, theShotLife, theARange, theFacing, thePosition )
        elif theA_Weapon == AUX_4:        # Torpedoes
            tankTorpedoes.tankTorpedo( theScreen, theA_Rank, theTank, theA_Speed, theShotLife, theARange, theFacing, thePosition )
        elif theA_Weapon == AUX_5:        # Mines
            tankMines.tankMine( theScreen, theA_Rank, theTank, theA_Speed, theShotLife, theARange, theFacing, thePosition )
        #fi
    #fi

