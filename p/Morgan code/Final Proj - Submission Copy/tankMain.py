"""
    Tanks main Module
    A hover tank battle game between players....or against the comp, haven't decided yet
    
Erin Brown - 2010
"""

import pygame, random
import tankInit, tankMusic, tankSound, Notify, tankTank, tankBackground, tankUpgrade, tankStatus, tankCrate
from tankGlobals import *

global DoneOnce

DoneOnce = False

def core():
    global tankScreen
    global tankAudio
    global tankStatScreen
    global FRAME_RATE
    global DoneOnce
    global myClock
    global MusicPaused

    if not DoneOnce:
        debug("Setting Clock")
        myClock     = pygame.time.Clock()   #test code
        MusicPaused = False
        DoneOnce = True
    
    ClearGameLists()
    keepGoing   = True
    p1Tank      = "Empty"
    p2Tank      = "Empty"
    w_m64       = tankScreen.get_width()/2
    w_m64       = w_m64 - ( w_m64 % 64 )      # screen width evenly disible by 64
    h_m64       = tankScreen.get_height()/2
    h_m64       = w_m64 - ( w_m64 % 64 )      # screen height evenly disible by 64
    randX       = random.randrange(64,w_m64, 64)
    randY       = random.randrange(64,tankScreen.get_height(),64)
    p1Tank      = tankTank.tankPlayer( tankScreen, "Random", 1, ( randX, randY ), P1_TANK_IMG )
    randX       = random.randrange(w_m64,tankScreen.get_width(),64)
    randY       = random.randrange(64,tankScreen.get_height(),64)
    p2Tank      = tankTank.tankPlayer( tankScreen, "Random", 2, ( randX, randY ), P2_TANK_IMG )
    gameCrate   = tankCrate.tankCrate( tankScreen, SUPPLY_CRATE_IMG )
    tankStatus.iconify_status( tankScreen )
    
    while keepGoing:
        myClock.tick( FRAME_RATE )
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == TRACK_END:
                debug("Hit a TRACK_END event.")
                #tankNotify.Notification( tankScreen, "Track Ended", 24, 5, ( 320, 240 ), clr_RED, ( 2, -2) )
                tankAudio.nextTrack( True )
                debug(tankAudio)            
                #ok music ended, tell it to play next
                #pygame.mixer.music.get_endevent( TRACK_END )
            elif event.type == pygame.KEYDOWN:
                if   event.key == pygame.K_ESCAPE:
                    keepGoing = False
                elif event.key == pygame.K_m:   #end music
                    if MusicPaused:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                    MusicPaused = not MusicPaused                    
                elif event.key == pygame.K_n:
                    tankAudio.nextTrack( True )
                    MusicPaused = False
            #fi                                     #This ends the keydown event check

        # check for victory
        for tank in TankSprites:
            if tank.score.check_victory():
                #victory notify
                keepGoing = False
            
        BackgroundSprites.update( )
        StatusSprites.update( )
        BonusSprites.update( )
        TankSprites.update( )
        ShotSprites.update( )
        TextSprites.update( )
        BackgroundSprites.draw( tankScreen )
        StatusSprites.draw( tankScreen )
        BonusSprites.draw( tankScreen )
        TankSprites.draw( tankScreen )
        ShotSprites.draw( tankScreen )
        TextSprites.draw( tankScreen )
        pygame.display.flip()
        
    Pausing = True
    printContinue( tankScreen )
    while Pausing:
        myClock.tick( FRAME_RATE )
        for an_event in pygame.event.get():
            if an_event.type == pygame.QUIT:
                Pausing = False
            if an_event.type == pygame.MOUSEBUTTONDOWN:
                Pausing = False
            elif an_event.type == pygame.KEYDOWN:
                Pausing = False
    return True


def main():
    global tankScreen
    global tankAudio
    global tankStatScreen
    
    tankScreen = pygame.display.set_mode(SCREEN_SIZE)
    tankBackground.Background( tankScreen, MAIN_SCREEN, STAR_FIELD_IMG )
    tankStatScreen = tankBackground.Background( tankScreen, STATUS_SCREEN, STATUS_SCREEN_IMG )
    tankAudio = tankMusic.MusicPlayer(BACKGROUND_MUSIC)
    tankAudio.current = pygame.mixer.music.play( 0 )
    tankSFX = tankSound.gameSound()
    donePlaying = False
    pygame.mixer.music.pause()
    #score = 0
    #HIGH_SCORE = 0
    Instruct = True
    instClock     = pygame.time.Clock()   #test code
    printInstructions( tankScreen )
    while Instruct:
        instClock.tick( 30 )        
        for an_event in pygame.event.get():
            if an_event.type == pygame.QUIT:
                donePlaying = True
            if an_event.type == pygame.MOUSEBUTTONDOWN:
                Instruct = False
            elif an_event.type == pygame.KEYDOWN:
                if an_event.key == pygame.K_ESCAPE:
                    donePlaying = True
                    Instruct = False
                    
    pygame.mixer.music.unpause()
    while not donePlaying:
        endit = core()
        if endit == False:
            donePlaying = True
        else:
            Instruct = True
            instClock     = pygame.time.Clock()   #test code
            printInstructions( tankScreen )
            while Instruct:
                instClock.tick( 30 )        
                for an_event in pygame.event.get():
                    if an_event.type == pygame.QUIT:
                        donePlaying = True
                    if an_event.type == pygame.MOUSEBUTTONDOWN:
                        Instruct = False
                    elif an_event.type == pygame.KEYDOWN:
                        if an_event.key == pygame.K_ESCAPE:
                            donePlaying = True
                            Instruct = False
        
            
    #    donePlaying = instructions(score)
    #    if not donePlaying:
    #        score = core()
    #        if score > HIGH_SCORE:
    #            HIGH_SCORE = score
    Empty_Lists()
    pygame.mixer.music.stop()    
    pygame.display.quit()
    pygame.quit()

def printInstructions( whichScreen ):
    BackgroundSprites.update( )
    BackgroundSprites.draw( tankScreen )

    insFont = pygame.font.SysFont("Courier New", 20)
    insLabels = []
    instructions = (
    #12345678901234567890123456789012345678901234567890123456789012345678901234567890
    "                                 Tanks - EDB                                   ",
    "",
    "                           --== Instructions: ==--                             ",
    "There are a pair of dueling spacecraft duking it out in a mostly uninhabited,  ",
    " and uninteresting, section of space.  Throughout the duel there will be supply",
    " crates delivered to the area via a Deep Space Mag-Driver.  These crates, of   ",
    " course, come with a warning of 'Contents may shift during transit'.  Which,   ",
    " naturally, is a polite way of saying 'It is probably broken, but you can't    ",
    " blame us'.  In other words not every crate will have something it.            ",    
    "",
    "                              --== Weapons ==--                                ",
    "Each ship is equipped with a primary cannon firing state-of-the-art solid-state",
    " projectiles (aka bullets); and a prototype 'Alternative Use eXcelsior' System ",
    " (aka AUX).  Currently there are 5 weapons that the AUX System can use, 3 types",
    " of missiles, a plasma torpedo, and proximity mines.  However, all 5 of these  ",
    " use the same raw-matter ammunition which makes the AUX System so special.     ",
    " Each new Tank that spawns will start with a different AUX System equipped.    ",
    "",
    "                                --== AUX ==--                                  ",    
    "Missiles do 25% less damage against shielded targets                           ",
    "Shield Pen Missiles do 25% less damage against shielded targets but always do  ",
    " at least 25% of their max damage to a target regardless of shielding          ",
    "Leech Missiles do 0 damage, drain Shields by 50% and energy reserves by 25/50% ",
    "Plasma Torpedoes do 25% less damage to armor, but are 50% more effecient at    ",
    " destroying shields",
    "Proximity Mines do 25% more damage to armor but do not move, and can be blown  ",
    " up by weapons fire.  There is a 100/10% chance they will hurt friendly ships. ",
    "",
    "                           --== Default Controls ==--                          ",
    "            Accel   Decel   Left    Right   Shields   Fire    Aux              ",
    "Player 1:     W       S       A       D        E      Space   Tab              ",
    "Player 2: KP  8       2       4       6        9        +      -               ",
    "",
    "                  <<< Click to Begin, Escape to Quit >>>                       "
    )

    for line in instructions:
        tempLabel = insFont.render(line, 1, clr_GREEN )
        insLabels.append(tempLabel)
    
    for i in range(len(insLabels)):
        whichScreen.blit(insLabels[i], (50, 80+( 20*i ) ))
        pygame.display.flip()
    return
    
def printContinue( whichScreen ):
    BackgroundSprites.update( )
    BackgroundSprites.draw( tankScreen )

    insFont = pygame.font.SysFont("Courier New", 30)
    insLabels = []
    instructions = (
    "                        <<< The Match Is Over >>>                              ",
    "               <<< Click any button, or press any key >>>                      "
    )

    for line in instructions:
        tempLabel = insFont.render(line, 1, clr_GREEN )
        insLabels.append(tempLabel)
    
    for i in range(len(insLabels)):
        whichScreen.blit(insLabels[i], (50, 360+( 40*i ) ))
        pygame.display.flip()
    return
            
def Empty_Lists():
    debug("Preparing to kill %d BackgroundSprites" % ( len(BackgroundSprites) ) )
    if (len(BackgroundSprites)>0):
        for sprite in BackgroundSprites:
            sprite.kill()
            debug("Killed a BackgroundSprite, %d remain!" % (len(BackgroundSprites)) )

    debug("Preparing to kill %d StatusSprites" % ( len(StatusSprites) ) )
    if (len(StatusSprites)>0):
        for sprite in StatusSprites:
            sprite.kill()
            debug("Killed a StatusSprites, %d remain!" % (len(StatusSprites)) )

    debug("Preparing to kill %d BonusSprites" % ( len(BonusSprites) ) )
    if (len(BonusSprites)>0):
        for sprite in BonusSprites:
            sprite.kill()
            debug("Killed a BonusSprites, %d remain!" % (len(BonusSprites)) )

    debug("Preparing to kill %d TankSprites" % ( len(TankSprites) ) )
    if (len(TankSprites)>0):
        for sprite in TankSprites:
            sprite.kill()
            debug("Killed a TankSprite, %d remain!" % (len(TankSprites)) )

    debug("Preparing to kill %d ShotSprites" % ( len(ShotSprites) ) )
    if (len(ShotSprites)>0):
        for sprite in ShotSprites:
            sprite.kill()
            debug("Killed a ShotSprites, %d remain!" % (len(ShotSprites)) )

    debug("Preparing to kill %d TextSprites" % ( len(TextSprites) ) )
    if (len(TextSprites)>0):
        for sprite in TextSprites:
            sprite.kill()
            debug("Killed a TextSprite, %d remain!" % (len(TextSprites)) )
           
def ClearGameLists():
    """ This destroys all sprites BUT background """

    debug("Preparing to kill %d StatusSprites" % ( len(StatusSprites) ) )
    if (len(StatusSprites)>0):
        for sprite in StatusSprites:
            sprite.kill()
            debug("Killed a StatusSprites, %d remain!" % (len(StatusSprites)) )

    debug("Preparing to kill %d BonusSprites" % ( len(BonusSprites) ) )
    if (len(BonusSprites)>0):
        for sprite in BonusSprites:
            sprite.kill()
            debug("Killed a BonusSprites, %d remain!" % (len(BonusSprites)) )

    debug("Preparing to kill %d TankSprites" % ( len(TankSprites) ) )
    if (len(TankSprites)>0):
        for sprite in TankSprites:
            sprite.kill()
            debug("Killed a TankSprite, %d remain!" % (len(TankSprites)) )

    debug("Preparing to kill %d ShotSprites" % ( len(ShotSprites) ) )
    if (len(ShotSprites)>0):
        for sprite in ShotSprites:
            sprite.kill()
            debug("Killed a ShotSprites, %d remain!" % (len(ShotSprites)) )

    debug("Preparing to kill %d TextSprites" % ( len(TextSprites) ) )
    if (len(TextSprites)>0):
        for sprite in TextSprites:
            sprite.kill()
            debug("Killed a TextSprite, %d remain!" % (len(TextSprites)) )

            
if __name__ == "__main__":
    SANITY = tankInit.sanity_init( )         # before we launch the main program, we'll do a sanity check
    Empty_Lists()

    if not SANITY:
        exit(1)
    else:
        debug("Calling Main")
        main()
