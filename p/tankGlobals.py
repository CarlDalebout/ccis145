"""
    This module contains the globals definitions for my Tank game
    A reminder to self: You still need to tell a function that you are using global versions of things or it will assume locality
Erin Brown - 2010
 """
import pygame, sys, os

# PATHS
global IMAGE_PATH
global MUSIC_PATH
global SOUND_PATH
global DATA_PATH

IMAGE_PATH          = "Images"
MUSIC_PATH          = "Music"
SOUND_PATH          = "Sounds"
DATA_PATH           = "Data"

# DEFAULT IMAGES

# RAW IMAGE LISTS

# DEFAULT SOUNDS AND AUDIO
global BACKGROUND_MUSIC

#Track01 & Track02 from Shanghai Alice Games 
#Aki Themes from Ambrosia Software
#both used to prove that music is possible
BACKGROUND_MUSIC    = [ "track01.ogg", "track02.ogg",
                        "Aki_Theme_1.ogg", "Aki_Theme_2.ogg", "Aki_Theme_3.ogg"
                      ]

# ANIMATED IMAGES   # Stores a list of images in the format of [ frames, "imagelist"... ]
global R1_TORPEDO
global R2_TORPEDO
global R1_MISSILE
global R1_SHIELD_PEN
global R1_LEECH
global R1_MINE
global R2_MINE
global R1_BULLET
global DEAD_TANK
global MAIN_READY
global AUX_READY
global ARMOR_PLATE

# rank 1's
R1_TORPEDO          = [ 3, "R1Torpedo 1", "R1Torpedo 2", "R1Torpedo 3" ]
R1_MISSILE          = [ 2, "R1Missile 1", "R1Missile 2" ]
R1_SHIELD_PEN       = [ 2, "R1Shield Pen Missile 1", "R1Shield Pen Missile 2" ]
R1_LEECH            = [ 2, "R1Leech Missile 1", "R1Leech Missile 2" ]
R1_MINE             = [ 2, "R1Prox Mine 1", "R1Prox Mine 2" ]
R1_BULLET           = [ 3, "R1Bullet 1", "R1Bullet 2", "R1Bullet 3" ]

#rank 2's (if they exist in images)
R2_TORPEDO          = [ 3, "R2Torpedo 1", "R2Torpedo 2", "R2Torpedo 3" ]
R2_MINE             = [ 2, "R2Prox Mine 1", "R2Prox Mine 2" ]

#Dead Tanks
DEAD_TANK           = [ 4, "Dead Tank 1", "Dead Tank 2", "Dead Tank 3", "Dead Tank 4" ]

#Ready Weapons              ready             -100%             -66%              -33%
MAIN_READY          = [ 4, "Ready Cannon 0", "Ready Cannon 1", "Ready Cannon 2", "Ready Cannon 3" ]     
AUX_READY           = [ 4, "Ready Aux 0", "Ready Aux 1", "Ready Aux 2", "Ready Aux 3" ]  

#Animated Armor Plate
ARMOR_PLATE         = [ 21, "Final Color Armor 100p", "Final Color Armor 95p", "Final Color Armor 90p", "Final Color Armor 85p", "Final Color Armor 80p",
                             "Final Color Armor 75p", "Final Color Armor 70p", "Final Color Armor 65p", "Final Color Armor 60p", "Final Color Armor 55p",
                             "Final Color Armor 50p", "Final Color Armor 45p", "Final Color Armor 40p", "Final Color Armor 35p", "Final Color Armor 30p",
                             "Final Color Armor 25p", "Final Color Armor 20p", "Final Color Armor 15p", "Final Color Armor 10p", "Final Color Armor 5p",
                              "Final Color Armor 0p" ]

# SOLID STATE IMAGES    # These images are non-animated on only have a single frame
global P1_TANK_IMG
global P2_TANK_IMG
global BAD_IMAGE
global SUPPLY_CRATE_IMG
global EMPTY_SPACE_IMG
global ENERGY_TANK_IMG
global STAR_FIELD_IMG
global STATUS_SCREEN_IMG
global SIMPLE_ARMOR_IMG

P1_TANK_IMG         = "Simple Tank 1"
P2_TANK_IMG         = "Simple Tank 2"
BAD_IMAGE           = "Bad Image"
SUPPLY_CRATE_IMG    = "Supply Crate"
EMPTY_SPACE_IMG     = "Empty Space"
ENERGY_TANK_IMG     = "Energy Tank"
STAR_FIELD_IMG      = "Star Field"
STATUS_SCREEN_IMG   = "Status Screen"
SIMPLE_ARMOR_IMG    = "Armor Plate"


# SPRITE LISTS
global BackgroundSprites
global StatusSprites
global BonusSprites
global TankSprites
global ShotSprites
global TextSprites

BackgroundSprites   = pygame.sprite.Group()
StatusSprites       = pygame.sprite.Group()
BonusSprites        = pygame.sprite.Group()
TankSprites         = pygame.sprite.Group()
ShotSprites         = pygame.sprite.Group()
TextSprites         = pygame.sprite.Group()

# EVENT CODES
global TRACK_END

TRACK_END           = 25

# DEFAULT KEY LISTS and POSITION CODES
"""
    Stored in the following order:
    Accel, Decel, Turn Left, Turn Right, Fire Main, Fire Aux
"""
global P_ACCEL
global P_DECEL
global P_TURN_LEFT
global P_TURN_RIGHT
global P_FIRE_MAIN
global P_FIRE_AUX
global P_CHARGE_SHIELD
global PLAYER_1_KEYS
global PLAYER_2_KEYS

P_ACCEL             = 0
P_DECEL             = 1
P_TURN_LEFT         = 2
P_TURN_RIGHT        = 3
P_FIRE_MAIN         = 4
P_FIRE_AUX          = 5
P_CHARGE_SHIELD     = 6
PLAYER_1_KEYS       = [ pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE, pygame.K_TAB, pygame.K_e ]
PLAYER_2_KEYS       = [ pygame.K_KP8, pygame.K_KP2, pygame.K_KP4, pygame.K_KP6, pygame.K_KP_PLUS, pygame.K_KP_MINUS, pygame.K_KP9 ]

# Tank Mod Fields
global MOD_NONE
global MOD_MAX_HP
global MOD_MAX_SHIELD
global MOD_SHIELD_DECAY
global MOD_SHIELD_GEN
global MOD_SHIELD_CHARGE
global MOD_MAX_ENERGY
global MOD_ENERGY_GEN
global MOD_REGEN_TIME
global MOD_ENERGY_DRAIN
global MOD_MAX_SHOTS
global MOD_MAX_RANGE
global MOD_MAX_AMMO
global MOD_MAX_AUX_AMMO
global MOD_SHOT_TIME
global MOD_AUX_WEAPON
global MOD_AUX_SPEED
global AUX_1
global AUX_2
global AUX_3
global AUX_4
global AUX_5

MOD_NONE            =  0    # modifies nothing, placeholder
MOD_MAX_HP          =  1    # modifies tank's max hp
MOD_MAX_SHIELD      =  2    # modifies tank's max shields
MOD_SHIELD_DECAY    =  3    # modifies shield decay in -1 shields per X seconds
MOD_SHIELD_GEN      =  4    # modifies how many shields are gained per charge
MOD_SHIELD_CHARGE   =  5    # modifies how much energy is consumed to charge shields once
MOD_MAX_ENERGY      =  6    # modifies maximum energy tank can hold
MOD_ENERGY_GEN      =  7    # modifies how fast energy is recharged in X energy per second
MOD_REGEN_TIME      =  8    # modifies how fast health is restored in 1 health per X seconds
MOD_ENERGY_DRAIN    =  9    # modifies how much energy is drained per second while health is regenerating
MOD_MAX_SHOTS       = 10    # modifies maximum number of shots allowed on screen by that player
MOD_MAX_RANGE       = 11    # modifies maximum range of main cannon shots
MOD_MAX_AMMO        = 12    # modifies maximum amount of bullet ammunition storage
MOD_MAX_AUX_AMMO    = 13    # modifies maximum amount of auxillary ammunition storage
MOD_SHOT_TIME       = 14    # modifies cooldown required between shots in the form of 1 shot per X seconds
MOD_AUX_WEAPON      = 15    # mosifies which aux weapon a tank has equipped
MOD_AUX_SPEED       = 16    # modifies the aux weapon's shot's speed
AUX_1               =  1    # Auxillary Weapon System Categories
AUX_2               =  2    # Auxillary Weapon System Categories
AUX_3               =  3    # Auxillary Weapon System Categories
AUX_4               =  4    # Auxillary Weapon System Categories
AUX_5               =  5    # Auxillary Weapon System Categories
MAX_MOD             = 16    # maximum mod number

# COMBAT CONSTANTS
global DAM_NONE
global DAM_COLLISION
global DAM_BULLET
global DAM_MISSILE
global DAM_SHIELD_PEN
global DAM_LEECH
global DAM_TORPEDO
global DAM_MINE
global MINOR_ENERGY_FLUX
global ENERGY_FLUX
global HEALTH_FLUX
global SHIELD_FLUX
global MINE_SAFETY
global FIRE_PRIMARY
global FIRE_AUXILLARY
global PRIMARY_COST
global AUXILLARY_COST

DAM_NONE            = 0x00000000
DAM_COLLISION       = 0x00000001    # Non-Specific type
DAM_BULLET          = 0x00000010    # bullet type
DAM_MISSILE         = 0x00000100    # missile type
DAM_SHIELD_PEN      = 0x00000200    # missile type
DAM_LEECH           = 0x00000400    # missile type
DAM_TORPEDO         = 0x00001000    # torpedo type
DAM_MINE            = 0x00010000    # mine type
MINOR_ENERGY_FLUX   = 0x10000000    # Energy Fluctuations
ENERGY_FLUX         = 0x20000000    # Energy Fluctuations
HEALTH_FLUX         = 0x40000000    # Health Fluctuations
SHIELD_FLUX         = 0x80000000    # Shield Fluctuations

MINE_SAFETY         = 3             # Time expressed in seconds
FIRE_PRIMARY        = 1
FIRE_AUXILLARY      = 2
PRIMARY_COST        = 4
AUXILLARY_COST      = 8


# CONSTANTS
global GAME_CLOCK
global FRAME_RATE
global DEBUG_MODE
global SCREEN_SIZE
global MAIN_SCREEN
global STATUS_SCREEN
global OFF_SCREEN
global ROT_RATE
global SPEED_DELTA
global SPEED_DAMAGE_MIN
global SPEED_PER_DAMAGE
global SPEED_MAX
global CRATE_SPAWN_RATE

GAME_CLOCK          = 0
FRAME_RATE          = 30
DEBUG_MODE          = False
SCREEN_SIZE         = ( 2400, 1800 )
MAIN_SCREEN         = pygame.Rect( 0, 0, SCREEN_SIZE[0], SCREEN_SIZE[1] - 128 )     # left, top, wide, high
STATUS_SCREEN       = pygame.Rect( 0, MAIN_SCREEN[3]+1, SCREEN_SIZE[0], 128 )   # left, top, wide, high
OFF_SCREEN          = ( -500, -500 )
ROT_RATE            = 10        # how much facing to change per rotation command.
SPEED_DELTA         = 0.5       # how many pixels of acceleration per button press
SPEED_DAMAGE_MIN    = 1.0       # Require how much damage from speed before actual damage
SPEED_PER_DAMAGE    = 2.0       # How many units of speed per point of speed damage when you hit something
SPEED_MAX           = 8.0       # Max pixel movement per frame
CRATE_SPAWN_RATE    = FRAME_RATE * 1.0

# COLOR CONSTANTS
global clr_RED
global clr_GREEN
global clr_BLUE
global clr_CYAN
global clr_PURPLE
global clr_YELLOW
global clr_BLACK
global clr_WHITE

clr_RED             = ( 255,   0,   0 )
clr_GREEN           = (   0, 255,   0 )
clr_BLUE            = (   0,   0, 255 )
clr_CYAN            = (   0, 255, 255 )
clr_PURPLE          = ( 255,   0, 255 )
clr_YELLOW          = ( 255, 255,   0 )
clr_BLACK           = (   0,   0,   0 )
clr_WHITE           = ( 255, 255, 255 )

# Active Game Storage for Universal Components
global tankScreen           # This will store the mainscreen used to display the game
global tankAudio            # This will store the main background music used in the game
global tankScores           # This will store the scoreboard used in the game
global tankSFX              # This will store the sound system used to play sound effects in the game
global tankStatScreen       # This will store the status screen used in the game

tankScreen          = 0
tankAudio           = 0
tankScores          = 0
tankSFX             = 0

# Global Functions
def debug(text):
    if DEBUG_MODE:
        print(text)

# The Following 4 functions are used for bitwise math
def IS_SET(flag, bit):
    out = flag & bit
    return out

def SET_BIT( var, bit):
    out = var | bit
    return out

def REMOVE_BIT( var, bit):
    out = var & ~bit
    return out
    
def TOGGLE_BIT( var, bit):
    out = var ^ bit
    return out

# Global Classes    
class var_storage():
    """This is an empty class to allow variable storage"""
    def __init__( self ):
        pass
    