"""
This file contains the globals definitions for MailPilot v2.0
Erin Brown - Oct, 2010
"""
import pygame, sys, os

# PATHS
global IMAGE_PATH
global SOUND_PATH

IMAGE_PATH  =   "Graphics"
SOUND_PATH  =   "Sounds"

#  DEFAULT IMAGES
global HITBOX_IMG
global PLANE_IMG
global ISLAND_IMG
global OCEAN_IMG
global CLOUD_IMG

HITBOX_IMG	= [ "Transparent_HitBox_15x15.gif", "Transparent_HitBox_30x30.gif", "Transparent_HitBox_60x60.gif" ]
PLANE_IMG	= [ "plane.gif" ]
ISLAND_IMG	= [ "island.gif" ]
HAPPY_IMG       = [ "Happy-Island.gif" ]
OCEAN_IMG	= [ "ocean-calm-reduced.gif", "ocean-deep-reduced.gif", "ocean-nice-reduced.gif"]
CLOUD_IMG	= [ "cloud_smallish.gif", "cloud_medium.gif", "cloud_largish.gif" ]

# RAW IMAGE LISTS
global CLOUD_LIST
global HITBOX_LIST
global CLOUD_PRAGMA
global HITBOX_PRAGMA

CLOUD_LIST      = []
CLOUD_PRAGMA    = False
HITBOX_LIST     = []
HITBOX_PRAGMA   = False

# DEFAULT SOUNDS
global SNDYAY_AUD
global SNDTHUNDER_AUD
global SNDLIFE_AUD
global EASTEREGG_AUD

SNDYAY_AUD	    = [ "fire2.ogg", "fire3.ogg", "happy1.ogg" ]
SNDTHUNDER_AUD	= [ "friendly_fire2.ogg", "suicide.ogg" ]
SNDLIFE_AUD     = [ "bonus_life.ogg" ]
EASTEREGG_AUD   = [ "EasterEgg.ogg" ] 

# ANIMATED IMGS
global SEABIRD_ANI

SEABIRD_ANI     = { "prefix" : "seabird", "start" : 0, "frames" : 8, "suffix" : ".gif" }

#SPRITE LISTS
global CloudSprites
global HitboxSprites
global BackgroundSprites
global IslandSprites
global FriendSprites
global ScoreSprites

CloudSprites        = pygame.sprite.Group()
HitboxSprites       = pygame.sprite.Group()
BackgroundSprites   = pygame.sprite.Group()
IslandSprites       = pygame.sprite.Group()
FriendSprites       = pygame.sprite.Group()
ScoreSprites        = pygame.sprite.Group()


# CONSTANTS
global GRAZE_BONUS
global BONUS_MULTIPLIER
global TARGET_SCORE
global EXTRA_LIFE
global FRAME_RATE
global GOOD_COLOR
global BAD_COLOR
global OFF_SCREEN
global ISLANDS_PER_SCREEN          # Screen is each block of ( SCREEN_WIDTH, SCREEN_HEIGHT ) or fraction thereof of screen area we have
global SCREEN_WIDTH
global SCREEN_HEIGHT
global NORMAL_DIFFICULTY
global STORM_DIFFICULTY
global HARD_DIFFICULTY
global INSANE_DIFFICULTY
global DEATH_DIFFICULTY
global SHINIGAMI_DIFFICULTY
global MAX_BIRDS
global SMALL_HITBOX
global MEDIUM_HITBOX
global LARGE_HITBOX
global SCORE_STRING
global DEBUG_MODE
global MAX_FLOAT_TIME

DEBUG_MODE          = False
GRAZE_BONUS         = 100
BONUS_MULTIPLIER    = 50
TARGET_SCORE        = 100
EXTRA_LIFE          = 10000
FRAME_RATE          = 30
GOOD_COLOR          = (   0, 255,   0 )
LIFE_COLOR          = ( 128,   0, 255 )
BAD_COLOR           = ( 255,   0,   0 )
OFF_SCREEN          = ( -500, -500 )
ISLANDS_PER_SCREEN  = 2
SCREEN_WIDTH        = 640
SCREEN_HEIGHT       = 480
NORMAL_DIFFICULTY   = [     0,     0,  1000,  3000,  5000,  7500, 10000 ]           # Normal mode, 6 clouds
STORM_DIFFICULTY    = [ 12500, 15000, 17500, 17500, 25000, 25000, 25000, 25000 ]    # Harder mode, at 25k points it will add 4 clouds
HARD_DIFFICULTY     = [ 30000, 30000, 30000, 35000, 35000, 35000, 40000, 40000, 40000, 45000, 45000, 45000, 45000, 45000, 45000 ]   # at 45k points it will add 6 more clouds
INSANE_DIFFICULTY   = [ 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000, 50000 ]   # yes at 50k points it will add 15 more clouds
DEATH_DIFFICULTY    = [ 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000,
                        75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000, 75000 ]   # At this difficulty we want to kill the player so we add 30 more clouds
SHINIGAMI_DIFFICULTY= [ 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000,
                        100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000,
                        100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000,
                        100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000,
                        100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000 ]   # At this difficulty we want to kill the player so we add 75 more clouds
MAX_BIRDS           = 2
SMALL_HITBOX        = 0
MEDIUM_HITBOX       = 1
LARGE_HITBOX        = 2
SCORE_STRING        = "Planes: %d  Next Plane: %d  Grazes: %d  Bonus: %d  Score: %d"
MAX_FLOAT_TIME      = FRAME_RATE * 0.5

# storage lists
global HIGH_SCORE
HIGH_SCORE          = 0

def debug(text):
    if DEBUG_MODE:
        print (text)


