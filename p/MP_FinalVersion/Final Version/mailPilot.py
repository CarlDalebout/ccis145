""" mail pilot 
    first complete arcade game
    fly plane with mouse
    deliver mail to islands,
    avoid thunderstorms. 
    
    v2.0 using seperated classes and with external globals.  Modded by EDB oct, 2010
    """
    
import pygame, random
import mpClasses, sys
from mpGlobals import *

global screen
pygame.init()

#tiny
#screen = pygame.display.set_mode((640, 480))
#medium
#screen = pygame.display.set_mode((960, 720))
#large
screen = pygame.display.set_mode((1120, 840))
#huge
#screen = pygame.display.set_mode((1280, 960))

def World_Reset():
    """ This function should kill all active sprites in preparation for a new game """
    debug("Entering CloudSprites for loop in World_Reset.")
    for sprite in CloudSprites:
        sprite.kill()
        if sprite.hitbox:
            debug("Killing a cloud hitbox.")
            sprite.hitbox.kill()
    debug("Entering BackgroundSprites for loop in World_Reset.")
    for sprite in BackgroundSprites:
        sprite.kill()
        if (sprite.type == "BIRD"):
            if sprite.hitbox:
                debug("Killing a bird hitbox.")
                sprite.hitbox.kill()
    debug("Entering FriendSprites for loop in World_Reset.")
    for sprite in FriendSprites:
        sprite.kill()
    debug("Entering IslandSprites for loop in World_Reset.")
    for sprite in IslandSprites:
        sprite.kill()
    debug("Entering ScoreSprites for loop in World_Reset.")
    for sprite in ScoreSprites:
        sprite.kill()

def init_sprites(screen):
    # Mandatory to keep
    # Should contain anything that is a singleton
    BackgroundSprites.empty()
    IslandSprites.empty()
    FriendSprites.empty()
    CloudSprites.empty()
    HitboxSprites.empty()
    ScoreSprites.empty()
    
    ocean = mpClasses.Ocean( screen, -1 )               # Umm without an ocean we have no terrain, and that's boring
    scoreboard = mpClasses.Scoreboard( screen )         # we have to keep this because it's the only way to track score
    plane = mpClasses.Plane( screen )                   # Without this we aren't able to play
    
    SCREENS = 0
    S_WIDE = screen.get_width()
    S_HIGH = screen.get_height()
    while ( S_WIDE >= SCREEN_WIDTH ):
        SCREENS += 1
        S_WIDE -= SCREEN_WIDTH
    
    while ( S_HIGH >= SCREEN_HEIGHT ):
        SCREENS += 1
        S_HIGH -= SCREEN_HEIGHT
        
    islands_to_spawn = SCREENS * ISLANDS_PER_SCREEN     # How many islands to spawn
    debug("Should be spawning %d screens worth of islands at %d islands per screen.  Told to spawn %d instead." % ( SCREENS, ISLANDS_PER_SCREEN, islands_to_spawn ))
    for loopVar in range( islands_to_spawn ):
        debug( "Spawning island # %d" % loopVar )
        mpClasses.Island( screen )                      # Spawn an island
        
    for cloud_threshold in NORMAL_DIFFICULTY:
        mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
        
    for loopVar in range( MAX_BIRDS ):
        mpClasses.Bird( screen )                        # Spawn us some seabirds!
    
    return (ocean, scoreboard, plane )
      
def game():
    """ Let's play the game..."""
    global screen
    pygame.display.set_caption("Mail Pilot v2.0!")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ocean, scoreboard, plane = init_sprites( screen )
    
    clock = pygame.time.Clock()
    keepGoing = True
    expiryOrdered = False
    moreClouds = 0
    floatTime = MAX_FLOAT_TIME  # Have to live this many seconds to get grazes
    while keepGoing:
        clock.tick(FRAME_RATE)
#        debug(str(clock.get_fps()))
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
                   
            if event.type == pygame.QUIT:
                keepGoing = False
                
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    World_Reset()
                    return scoreboard.score

        # need to figure out how to do this
        """
        if unhappyCheck:      #Missed an island last pass...
            unhappyCheck = False
            mpClasses.Notification( screen, "Bonus Reduced", 3, plane.rect.center, BAD_COLOR )
            scoreboard.bonus = max( 0, scoreboard.bonus - 1 )
        """
            
        #check collisions
        #now need to add in multiple islands.
        #if plane.rect.colliderect(island.rect):
        taggedIslands = pygame.sprite.spritecollide( plane, IslandSprites, False )
#        if plane.rect.colliderect(island.rect):
        if taggedIslands:
            for island in taggedIslands:
                if ( island.happy == False ):
                    event1 = 0
                    event2 = 0
                    plane.sndYay.play()
                    plane.snd_refresh()
                    island.make_happy()
                    event1 = scoreboard.increment_score(  )
                    scoreText = "+ %d" % event1
                    mpClasses.Notification( screen, scoreText, 5, plane.rect.center, GOOD_COLOR )
                    midScreen = ( screen.get_width()/2, screen.get_height()/2 )

                    if ( ( ( scoreboard.score + event1 ) >= STORM_DIFFICULTY[0] ) and ( moreClouds < 1 ) ):     # Entering hard Mode
                        mpClasses.Notification( screen, "Welcome to the Storm!", 5, midScreen, BAD_COLOR )
                        mpClasses.Notification( screen, "-= +8 Clouds (15) =- ", 5, midScreen, BAD_COLOR )
                        moreClouds = 1
                        for cloud_threshold in STORM_DIFFICULTY:
                            mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
                        #rof
                    #fi
                    
                    if ( ( ( scoreboard.score + event1 ) >= HARD_DIFFICULTY[0] ) and ( moreClouds < 2 ) ):     # Entering hard Mode
                        mpClasses.Notification( screen, "HARD MODE!", 5, midScreen, BAD_COLOR )
                        mpClasses.Notification( screen, "-= +15 Clouds (30) =- ", 5, midScreen, BAD_COLOR )
                        moreClouds = 2
                        for cloud_threshold in HARD_DIFFICULTY:
                            mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
                        #rof
                    #fi
                    if ( ( ( scoreboard.score + event1 ) >= INSANE_DIFFICULTY[0] ) and ( moreClouds < 3 ) ):     # Entering insane Mode
                        mpClasses.Notification( screen, "INSANITY MODE!", 5, midScreen, BAD_COLOR )
                        mpClasses.Notification( screen, "-= +15 Clouds (45) =- ", 5, midScreen, BAD_COLOR )
                        moreClouds = 3
                        for cloud_threshold in INSANE_DIFFICULTY:
                            mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
                        #rof
                    #fi
                    if ( ( ( scoreboard.score + event1 ) >= DEATH_DIFFICULTY[0] ) and ( moreClouds < 4 ) ):     # Entering insane Mode
                        mpClasses.Notification( screen, "WILL YOU DIE ALREADY MODE!", 5, midScreen, BAD_COLOR )
                        mpClasses.Notification( screen, "-= +30 Clouds (75) =- ", 5, midScreen, BAD_COLOR )
                        moreClouds = 4
                        for cloud_threshold in DEATH_DIFFICULTY:
                            mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
                        #rof
                    #fi
                    if ( ( ( scoreboard.score + event1 ) >= SHINIGAMI_DIFFICULTY[0] ) and ( moreClouds < 5 ) ):     # Entering insane Mode
                        mpClasses.Notification( screen, "<<< SHINIGAMI NO SHINIGAMI >>>", 5, midScreen, BAD_COLOR )
                        mpClasses.Notification( screen, "-= +75 Clouds (150) =- ", 5, midScreen, BAD_COLOR )
                        moreClouds = 5
                        for cloud_threshold in  SHINIGAMI_DIFFICULTY:
                            mpClasses.Cloud( screen, random.randrange(0,2), cloud_threshold )      # Spawn a cloud with a difficulty threshold per the list 
                        
                        #rof
                    #fi
                #fi happy
            #rof

        #making the birds useful
        for birds in BackgroundSprites:
            if birds.type != "BIRD":
                continue
            else:
                BirdDestroy = pygame.sprite.spritecollide( birds, CloudSprites, False, pygame.sprite.collide_rect )
                
                #ok the bird MIGHT have hit a cloud, now to see if it hit the heart of the cloud
                if BirdDestroy:
                    for cloud in BirdDestroy:
                        if ( birds.rect.colliderect( cloud.hitbox.rect ) ):
                            #yep we hit the cloud!  goodie we get to 'reset it'
                            cloud.reset()
                    #rof
                #fi
            #fi
        #rof
            
        hitClouds = pygame.sprite.spritecollide(plane, CloudSprites, False, pygame.sprite.collide_rect)
        if hitClouds:
            #okie we MIGHT have hit a cloud, now let's find out if we actually hit the heart of the cloud
            toasted = False
            floatTime = MAX_FLOAT_TIME          # Float_time get's constantly reset while in a cloud
            
            for theCloud in hitClouds:
                if toasted:
                    continue
                elif plane.rect.colliderect(theCloud.hitbox.rect):        #checking the clouds Hitbox
                    #crud we DID actually hit the cloud..oh well, there's always next life to do better!
                    plane.sndThunder.play()
                    plane.snd_refresh()
                    scoreboard.float_grazes = 0  # We lose ALL floating Grazes when we die
                    scoreboard.lives -= 1
                    scoreboard.bonus = 0    # reset the consecutive bonus
                    mpClasses.Notification( screen, "Bonus Reset", 3, plane.rect.center, BAD_COLOR )
                    toasted = True
                else:
                    #woots we DIDN'T hit the cloud for real, let's give ourselves a grazing bonus
                    if not theCloud.grazed:
                        theCloud.grazed = True
                        scoreboard.float_grazes += theCloud.graze_value
                        mpClasses.Notification( screen, "Graze!", 2, plane.rect.center, GOOD_COLOR )
                #fi
            #rof
                    
            if toasted:
                for theCloud in hitClouds:
                    theCloud.reset()
        else:
            #we've gone a frame without hitting a cloud, decrement the float timer
            if ( scoreboard.float_grazes > 0 ):
                # we only take time off if we actually have grazes floating.
                floatTime -= 1
                if ( floatTime < 1 ):
                    #we ran out of float time!  GREAT award grazes
                    scoreboard.grazes       += scoreboard.float_grazes
                    scoreText               = "Graze Bonus!"
                    scoreText2              = "+ %d" % (scoreboard.float_grazes * GRAZE_BONUS)
                    floatTime               = MAX_FLOAT_TIME
                    scoreboard.float_grazes = 0
                    mpClasses.Notification( screen, scoreText, 5, plane.rect.center, LIFE_COLOR )
                    mpClasses.Notification( screen, scoreText2, 5, plane.rect.center, GOOD_COLOR )            
                #fi float_time
            #fi float_grazes
        #fi hitClouds
                    
                    
        event2 = scoreboard.check_extra_life(  )
        if ( event2 != 0 ):
            mpClasses.Notification( screen, "+1 Plane", 7, plane.rect.center, LIFE_COLOR )
            scoreboard.sndBonusLife.play()
            scoreboard.snd_refresh()
        #fi event2
                    
        if scoreboard.lives <= 0:
            #ok we ran out of lives...sad panda
            #let's calculate the bonus!
            #oops no more graze bonus now at the end, it's all during the game!
            #graze_score = scoreboard.grazes * GRAZE_BONUS
            #graze_text  = "+ %d" % graze_score
            #mpClasses.Notification( screen, graze_text, 5, plane.rect.center, GOOD_COLOR )
            expiryOrdered = True
            keepGoing = False
        
        BackgroundSprites.update()
        IslandSprites.update()
        FriendSprites.update()
        CloudSprites.update( scoreboard.score )
        ScoreSprites.update()

        BackgroundSprites.draw(screen)
        IslandSprites.draw(screen)
        FriendSprites.draw(screen)
        CloudSprites.draw(screen)
        HitboxSprites.draw(screen)
        ScoreSprites.draw(screen)

        pygame.display.flip()
    #wend
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
        
    debug("Checking for easteregg.")
    if ( random.randrange(1,4) == 1 ):
        scoreboard.sndEasterEgg.play()
    debug("Calling World_Reset from End of Game.")
    World_Reset()
    debug("Finished World_Reset from End of Game.")
    return scoreboard.score
    
def instructions(score):
    global screen
    pygame.display.set_caption("Mail Pilot!")

    plane = mpClasses.Plane( screen )
    ocean = mpClasses.Ocean( screen, 0 )
    bird  = mpClasses.Bird ( screen )
    allSprites = pygame.sprite.Group(ocean, plane, bird )
    insFont = pygame.font.SysFont(None, 50)
    insLabels = []
    instructions = (
    "Mail Pilot.     Last Score: %d    High Score: %d" % ( score, HIGH_SCORE ),
    "Instructions:  You are a mail pilot,",
    "delivering mail to the islands.",
    "",
    "Fly over an island to drop the mail,",
    "but be careful not to fly too close",    
    "to the clouds. Your plane will fall ",
    "apart if it is hit by lightning too",
    "many times. Steer with the mouse.",
    "",
    "good luck!",
    "",
    "click to start, escape to quit..."
    )
    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 0))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
                pygame.display.quit()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
   
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
        
    # Ok we left the loop, gonna start a game
    pygame.mouse.set_visible(True)
    World_Reset()
    return donePlaying
        
def main():
    donePlaying = False
    score = 0
    HIGH_SCORE = 0
    
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()
            if score > HIGH_SCORE:
                HIGH_SCORE = score


if __name__ == "__main__":
    main()
