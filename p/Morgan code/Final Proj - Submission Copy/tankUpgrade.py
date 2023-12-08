"""
    This module contains what is needed to handle gear upgrades for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
import tankTank

from tankGlobals import *

class Upgrade():
    def __init__( self, name, category, rank, mod_field_1, mod_amt_1, mod_field_2, mod_amt_2 ):
        """This class contains the definitions of an upgrade"""
        self.name       = name
        self.category   = category
        self.rank       = rank
        self.mod_field1 = mod_field_1
        self.mod_amt1   = mod_amt_1
        self.mod_field2 = mod_field_2
        self.mod_amt2   = mod_amt_2
        self.display    = False         # only used for testing, scrap code
        
    def equip( self, toWhom ):
        """This is where we actually equip an upgrade to a given tank"""
        # We don't allow downgrades first we'll check to see if it's a downgrade
        #  The only exception is aux_weapons which have a funky ranking
        # Last we'll update the toWhom.upgrades variables
        # Before we leave the function we'll apply the mods

        if self.category == "HULL":
            if self.rank <= toWhom.upgrades.hull_rank: 
                debug("Already has hull rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.hull_rank, self.rank ) )
                return
            toWhom.upgrades.hull_rank       = self.rank             #set the rank of the upgrade
            toWhom.upgrades.hull_name       = self.name             #set the upgrade name
        elif self.category == "SHIELD_CAP":
            if self.rank <= toWhom.upgrades.shield_rank: 
                debug("Already has shield rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.shield_rank, self.rank ) )
                return
            toWhom.upgrades.shield_rank     = self.rank             #set the rank of the upgrade
            toWhom.upgrades.shield_name     = self.name             #set the upgrade name
        elif self.category == "SHIELD_GEN":
            if self.rank <= toWhom.upgrades.shield_gen_rank: 
                debug("Already has shield_gen rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.shield_gen_rank, self.rank ) )
                return
            toWhom.upgrades.shield_gen_rank = self.rank             #set the rank of the upgrade
            toWhom.upgrades.shield_gen_name = self.name             #set the upgrade name
        elif self.category == "ENERGY_TANK":
            if self.rank <= toWhom.upgrades.energy_rank: 
                debug("Already has energy rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.energy_rank, self.rank ) )
                return
            toWhom.upgrades.energy_rank     = self.rank             #set the rank of the upgrade
            toWhom.upgrades.energy_name     = self.name             #set the upgrade name
        elif self.category == "ENERGY_GEN":
            if self.rank <= toWhom.upgrades.energy_gen_rank: 
                debug("Already has energy_gen rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.energy_gen_rank, self.rank ) )
                return
            toWhom.upgrades.energy_gen_rank = self.rank             #set the rank of the upgrade
            toWhom.upgrades.energy_gen_name = self.name             #set the upgrade name
        elif self.category == "REPAIR":
            if self.rank <= toWhom.upgrades.regen_rank: 
                debug("Already has regen rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.regen_rank, self.rank ) )
                return
            toWhom.upgrades.regen_rank      = self.rank             #set the rank of the upgrade
            toWhom.upgrades.regen_name      = self.name             #set the upgrade name
        elif self.category == "CANNON":
            if self.rank <= toWhom.upgrades.cannon_rank: 
                debug("Already has cannon rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.cannon_rank, self.rank ) )
                return
            toWhom.upgrades.cannon_rank     = self.rank             #set the rank of the upgrade
            toWhom.upgrades.cannon_name     = self.name             #set the upgrade name
        elif self.category == "AMMO":
            if self.rank <= toWhom.upgrades.ammo_rank: 
                debug("Already has ammo rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.ammo_rank, self.rank ) )
                return
            toWhom.upgrades.ammo_rank      = self.rank             #set the rank of the upgrade
            toWhom.upgrades.ammo_name      = self.name             #set the upgrade name
        elif self.category == "SHOT_CD":
            if self.rank <= toWhom.upgrades.shot_cd_rank: 
                debug("Already has shot_cd rank %d, ignoring 'new' rank %d." % ( toWhom.upgrades.shot_cd_rank, self.rank ) )
                return
            toWhom.upgrades.shot_cd_rank   = self.rank             #set the rank of the upgrade
            toWhom.upgrades.shot_cd_name   = self.name             #set the upgrade name
        elif self.category == "AUX_WEAPON":
            #ok what's different about aux weapons
            #first off each aux weapon has its own ranks and its own mod
            #so to test it not only do we hafta test rank but we hafta test if it's the same weapon system
            if self.mod_amt1 == toWhom.aux_weapon:      # ok same weapon system
                if self.rank <= toWhom.upgrades.aux_rank: 
                    debug("Already has aux_weapon %d at rank %d, ignoring 'new' %d at rank %d."
                    % ( toWhom.aux_weapon, toWhom.upgrades.aux_rank, self.mod_amt1, self.rank ) )
                    return
            # ok so it's either a new weapon system or an upgraded rank apply it either way
            toWhom.upgrades.aux_rank       = self.rank             #set the rank of the upgrade
            toWhom.upgrades.aux_name       = self.name             #set the upgrade name
        else:   #no idea how we got here...but we'll abort
            return
        
        #this is where the magic happens besides just renaming the system and changing the rank
        toWhom.apply_mod( self.mod_field1, self.mod_amt1 )
        toWhom.apply_mod( self.mod_field2, self.mod_amt2 )
    
    def __str__( self ):
        if self.display:
            output = "%-26s     %-12s     %d      %2d/%3d      %2d/%3d" % ( self.name, self.category, self.rank, self.mod_field1, self.mod_amt1, self.mod_field2, self.mod_amt2 )
        else:
            output = "Name- %-48s, Type- %12s, Rank- %d, Mod1- %d/%d, Mod2- %d/%d" % ( self.name, self.category, self.rank, self.mod_field1, self.mod_amt1, self.mod_field2, self.mod_amt2 )
        return output
        
        
def seek_upgrade_by_name( whichUpgrade = "none" ):
    #this seeks an upgrade by name and returns the line it's on in the table
    #p1-7 are just parameters pulled from the table
    if whichUpgrade == "none":      # nothing passed, return -1 for not found
        return -1
        
    # look thru the upgrades_table for which line has the upgrade and return that line number
    for line in range( 0, len( Upgrades_Table ) ):
        p1, p2, p3, p4, p5, p6, p7 = Upgrades_Table[line]
        if p1 == whichUpgrade:
            return line
    return -1

def seek_upgrade_by_type( whichUpgrade = "none", whichRank = 0 ):
    #this seeks an upgrade by type and rank and returns the line it's on in the table
    #As a note when looking for AUX_WEAPON types it will ONLY return AUX_1 class
    #p1-7 are just parameters pulled from the table
    if whichUpgrade == "none":      # nothing passed, return -1 for not found
        return -1
    if whichRank <= 0:              # nothing passed, return -1 for not found
        return -1
        
    # look thru the upgrades_table for which line has the upgrade and return that line number
    for line in range( 0, len( Upgrades_Table ) ):
        p1, p2, p3, p4, p5, p6, p7 = Upgrades_Table[line]
        if ( p2 == whichUpgrade ) and ( p3 == whichRank ):
            if ( whichUpgrade == "AUX_WEAPON" ) and ( p5 == AUX_1 ):
                return line
            elif ( whichUpgrade != "AUX_WEAPON" ):
                return line
    return -1
    
def equip_upgrade( toWhom, whichUpgrade = "none", whichRank = -1 ):
    """
        find an upgrade and equip it to a given tank.
        Can be called with name of the upgrade or called with type of upgrade and rank
        Should be more reliable to search by type/rank
    """
   
    #how are we going to find it first
    if ( whichUpgrade == "none" ):
        return False                # no argument passed, abort
        
    if ( whichRank <= 0 ):          # a rank was passed as well so we'll hunt by type/rank
        the_Upgrade = seek_upgrade_by_name( whichUpgrade )
    else:
        the_Upgrade = seek_upgrade_by_type( whichUpgrade, whichRank )
    
    if ( the_Upgrade == -1 ):
        debug("Upgrade %s not found, to bad." % whichUpgrade )
        return False
    else:
        p1, p2, p3, p4, p5, p6, p7 = Upgrades_Table[ the_Upgrade ]
        apply_Upgrade = Upgrade( p1, p2, p3, p4, p5, p6, p7 )
        debug("Equipping the following upgrade:\n%s" % apply_Upgrade )
        apply_Upgrade.equip( toWhom )
        return True
    #fi

#scrap code used for testing
def init_upgrades( display = False):
    for line in range( 0, len( Upgrades_Table ) ):
        p1, p2, p3, p4, p5, p6, p7 = Upgrades_Table[line]
        testUpgrade = Upgrade( p1, p2, p3, p4, p5, p6, p7 )
        testUpgrade.display = display
        if display:
            debug(testUpgrade)

def pretty_print():
    output = "Name%-26s Type%-9s Rank%1s  Mod1 %1s/%3s Mod2%2s/%3s" % ( "", "", "", "", "", "", "" )
    debug(output)
    init_upgrades(True)
#end scrap code        
        
        
Upgrades_Table = [
#            name                                    type   rank        mod field      amt             field2   amt2         
#Hulls
        [    "Standard Hull",                      "HULL",     1,      MOD_MAX_HP,      50,          MOD_NONE,     0],
        [    "Reinforced Hull",                    "HULL",     2,      MOD_MAX_HP,      75,          MOD_NONE,     0],
        [    "Extra Reinforced Hull",              "HULL",     3,      MOD_MAX_HP,      99,          MOD_NONE,     0],
#Shields    
        [    "Standard Shield Capacitor",    "SHIELD_CAP",     1,  MOD_MAX_SHIELD,      16,  MOD_SHIELD_DECAY,     2],
        [    "Advanced Shield Capacitor",    "SHIELD_CAP",     2,  MOD_MAX_SHIELD,      24,  MOD_SHIELD_DECAY,     3],
        [    "Prototype Shield Capacitor",   "SHIELD_CAP",     3,  MOD_MAX_SHIELD,      32,  MOD_SHIELD_DECAY,     4],    
        [    "Standard Shield Generator",    "SHIELD_GEN",     1,  MOD_SHIELD_GEN,       4, MOD_SHIELD_CHARGE,     8],
        [    "Turbo Shield Generator",       "SHIELD_GEN",     2,  MOD_SHIELD_GEN,       8, MOD_SHIELD_CHARGE,    12],
        [    "Prototype Shield Generator",   "SHIELD_GEN",     3,  MOD_SHIELD_GEN,      16, MOD_SHIELD_CHARGE,    16],   
#Energy Tanks and Gen
        [    "Small Energy Tank",           "ENERGY_TANK",     1,  MOD_MAX_ENERGY,     32,           MOD_NONE,     0],
        [    "Big Energy Tank",             "ENERGY_TANK",     2,  MOD_MAX_ENERGY,     48,           MOD_NONE,     0],
        [    "Huge Energy Tank",            "ENERGY_TANK",     3,  MOD_MAX_ENERGY,     64,           MOD_NONE,     0],
        [    "Standard Generator",           "ENERGY_GEN",     1,  MOD_ENERGY_GEN,      2,           MOD_NONE,     0],
        [    "Tuned Generator",              "ENERGY_GEN",     2,  MOD_ENERGY_GEN,      3,           MOD_NONE,     0],
        [    "Twin Generators",              "ENERGY_GEN",     3,  MOD_ENERGY_GEN,      4,           MOD_NONE,     0],
        [    "Twin Tuned Generators",        "ENERGY_GEN",     4,  MOD_ENERGY_GEN,      6,           MOD_NONE,     0],
#Repair Systems
        [    "No Repair System",                 "REPAIR",     1,  MOD_REGEN_TIME,      0,   MOD_ENERGY_DRAIN,     0],
        [    "L1 Regenerative Nanites",          "REPAIR",     2,  MOD_REGEN_TIME,      3,   MOD_ENERGY_DRAIN,     3],
        [    "L2 Regenerative Nanites",          "REPAIR",     3,  MOD_REGEN_TIME,      2,   MOD_ENERGY_DRAIN,     3],
        [    "L3 Regenerative Nanites",          "REPAIR",     4,  MOD_REGEN_TIME,      1,   MOD_ENERGY_DRAIN,     3],
#Munition/Cannons
        [    "Standard Firing Control",          "CANNON",     1,   MOD_MAX_SHOTS,      2,      MOD_MAX_RANGE,   400],
        [    "Advanced Firing Control",          "CANNON",     2,   MOD_MAX_SHOTS,      4,      MOD_MAX_RANGE,   450],
        [    "Prototype Firing Control",         "CANNON",     3,   MOD_MAX_SHOTS,      6,      MOD_MAX_RANGE,   500],
        [    "Single Ammunition Bays",             "AMMO",     1,    MOD_MAX_AMMO,     32,   MOD_MAX_AUX_AMMO,     2],
        [    "Double Ammunition Bays",             "AMMO",     2,    MOD_MAX_AMMO,     64,   MOD_MAX_AUX_AMMO,     4],
        [    "Triple Ammunition Bays",             "AMMO",     3,    MOD_MAX_AMMO,     99,   MOD_MAX_AUX_AMMO,     6],
        [    "Slow Ammo Feed",                  "SHOT_CD",     1,   MOD_SHOT_TIME,    1.5,           MOD_NONE,     0],
        [    "Fast Ammo Feed",                  "SHOT_CD",     2,   MOD_SHOT_TIME,    1.0,           MOD_NONE,     0],
        [    "Twin Ammo Feeds",                 "SHOT_CD",     3,   MOD_SHOT_TIME,    0.5,           MOD_NONE,     0],
#Aux Weapons
        [    "Missiles",                     "AUX_WEAPON",     1,  MOD_AUX_WEAPON,  AUX_1,      MOD_AUX_SPEED,    20],
        [    "Hyper Missiles",               "AUX_WEAPON",     2,  MOD_AUX_WEAPON,  AUX_1,      MOD_AUX_SPEED,    25],
        [    "Warp Missiles",                "AUX_WEAPON",     3,  MOD_AUX_WEAPON,  AUX_1,      MOD_AUX_SPEED,    30],
        [    "Shield Pen Missiles",          "AUX_WEAPON",     1,  MOD_AUX_WEAPON,  AUX_2,      MOD_AUX_SPEED,    20],
        [    "Hyper Shield Pen Missiles",    "AUX_WEAPON",     2,  MOD_AUX_WEAPON,  AUX_2,      MOD_AUX_SPEED,    25],
        [    "Warp Shield Pen Missiles",     "AUX_WEAPON",     3,  MOD_AUX_WEAPON,  AUX_2,      MOD_AUX_SPEED,    30],    
        [    "Leech Missiles",               "AUX_WEAPON",     1,  MOD_AUX_WEAPON,  AUX_3,      MOD_AUX_SPEED,  12.5],
        [    "Super Leech Missiles",         "AUX_WEAPON",     2,  MOD_AUX_WEAPON,  AUX_3,      MOD_AUX_SPEED,  15.0],
        [    "Plasma Torpedoes",             "AUX_WEAPON",     1,  MOD_AUX_WEAPON,  AUX_4,      MOD_AUX_SPEED,    15],
        [    "Unstable Plasma Torpedoes",    "AUX_WEAPON",     2,  MOD_AUX_WEAPON,  AUX_4,      MOD_AUX_SPEED,  17.5],
        [    "Proximity Mines",              "AUX_WEAPON",     1,  MOD_AUX_WEAPON,  AUX_5,      MOD_AUX_SPEED,     0],
        [    "IFF Prox Mines",               "AUX_WEAPON",     2,  MOD_AUX_WEAPON,  AUX_5,      MOD_AUX_SPEED,     0],
    ]

"""
notes:
Missiles deal 25% less damage to shielded targets
Shield Pen Missiles deal 25% less damage to shielded targets but always deal 25% damage to the target
Leech Missiles deal 0 damage but totally destroy shields and drain 25/50% energy reserves
Plasma Torpedoes deal 50% more damage to shields but deal 25% less damage to armor
Proximity mines take 3 seconds to arm explode when hit by weapons, but do not move and have a 100/1% chance of exploding on owner

-- Bullet Base speed is 10
-- Damage is as follows:
--	  Bullets: 2.5
--	 Missiles: 24
-- 	  Leeches: 0
--	Torpedoes: 24
--		Mines: 24
-- Expected Life spans
--	  Bullets: 40/45/50 seconds
--	 Missiles: 25/20/17 seconds
-- 	  Leeches: 29       seconds
--	Torpedoes: 33       seconds
--		Mines: 50       seconds (the current global max)

"""
