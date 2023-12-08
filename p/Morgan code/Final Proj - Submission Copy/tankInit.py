"""
    This module is used to generate a sanity check for all necessary core components of the game.  Ideally this should provide
    cleaner exits for missing files then is normally provided.
    If certain core components are missing the program will end, however not all modules are critical and the game will still
    run without them, however it may still break as a result.
Erin Brown - 2010
"""

import os, sys, pygame
from tankGlobals import *

def sanity_init( ):
    # First we set everything to not sane, then we'll go from there.    
    PYGAME_SANITY       = False
    DISPLAY_SANITY      = False
    AUDIO_SANITY        = False
    MUSIC_SANITY        = False
    FONT_SANITY         = False
    SPRITE_SANITY       = False
    CLOCK_SANITY        = False
    
    # Testing pygame sanity, if we have sanity, init pygame
    if not pygame and not PYGAME_SANITY:
        debug("No pygame module.")
        PYGAME_SANITY   = False
    else:
        pygame.init()
        PYGAME_SANITY   = True

    # Testing display sanity, if we have sanity, init display        
    if not pygame.display and not DISPLAY_SANITY:
        debug("No display module.")
        DISPLAY_SANITY  = False
    else:
        pygame.display.init()
        DISPLAY_SANITY  = True
        
    # Testing audio sanity, if we have sanity, init audio
    if not pygame.mixer and not AUDIO_SANITY:
        debug("No audio module.")
        AUDIO_SANITY    = False
    else:
        pygame.mixer.init()
        AUDIO_SANITY    = True

    # Testing music sanity, if we have sanity, note it
    if (not pygame.mixer.music and not MUSIC_SANITY) or not AUDIO_SANITY:
        debug("No music module.")
        MUSIC_SANITY    = False
    else:
        MUSIC_SANITY    = True

    # Testing font sanity, if we have sanity, init fonts
    if not pygame.font and not FONT_SANITY:
        debug("No font module.")
        FONT_SANITY     = False
    else:
        pygame.font.init()
        FONT_SANITY     = True
        
    # Testing sprite sanity, if we have sanity, note it
    if not pygame.sprite and not SPRITE_SANITY:
        debug("No sprite module.")
        SPRITE_SANITY   = False
    else:
        SPRITE_SANITY   = True

    # Testing clock sanity, if we have sanity, update our clock and note it
    if not pygame.time and not CLOCK_SANITY:
        debug("No time module.")
        CLOCK_SANITY    = False
    else:
        GAME_CLOCK      = pygame.time.Clock()
        CLOCK_SANITY    = True

    # With sanities checked, process any necessary aborts or report failures.
    if not PYGAME_SANITY:
        debug("Core module <PYGAME> was not found.  Program will now end.")
        raw_input("Press any key to quit...")
        exit(1)
        return False
    
    if not DISPLAY_SANITY or not SPRITE_SANITY or not CLOCK_SANITY:
        debug("At least 1 of the following sub-modules <DISPLAY, SPRITE, TIME> were not found.  Progam will now end.")
        raw_input("Press any key to quit...")
        exit(1)
        return False
    
    if not AUDIO_SANITY or not MUSIC_SANITY:
        debug("At least 1 of the following sub-modules <MIXER, MUSIC> were not found.  Program will function in a reduced state.")

    if not FONT_SANITY:
        debug("Decorative module <FONT> was not found.  Progam will function in a reduced state.")

    #report sanities
    if AUDIO_SANITY:
        debug("AUDIO_SANITY-T")
    else:
        debug("AUDIO_SANITY-F")
        
    if MUSIC_SANITY:
        debug("MUSIC_SANITY-T")
    else:
        debug("MUSIC_SANITY-F")

    if PYGAME_SANITY:
        debug("PYGAME_SANITY-T")
    else:
        debug("PYGAME_SANITY-F")

    if DISPLAY_SANITY:
        debug("DISPLAY_SANITY-T")
    else:
        debug("DISPLAY_SANITY-F")

    if FONT_SANITY:
        debug("FONT_SANITY-T")
    else:
        debug("FONT_SANITY-F")

    if SPRITE_SANITY:
        debug("SPRITE_SANITY-T")
    else:
        debug("SPRITE_SANITY-F")

    if CLOCK_SANITY:
        debug("CLOCK_SANITY-T")
    else:
        debug("CLOCK_SANITY-F")

    return True
#fed
