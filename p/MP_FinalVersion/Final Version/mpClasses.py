"""
This file contains the class definitions for MailPilot v2.0
Erin Brown - Oct, 2010
"""

import pygame, sys, random
from mpGlobals import *

def getListObj ( objList = [], which = 0 ):
    """ This function returns a xth element of an objList """
    if ( ( len(objList) == 0 ) or ( not objList ) ):
        debug("Empty objList passed.  Failing gracefully.")
        pygame.display.quit()
        pygame.quit()
        sys.exit()
    elif ( which > len( objList ) ):
        debug("Request to retrieve object from objList exceeds sizeof objList.  Failing gracefully.")
        pygame.display.quit()
        pygame.quit()
        sys.exit()
    else:
        if ( which < 0 ):
            """ We'll mod it by -length of the list then return that element
                 For example if objList has 3 elements and we request element -5
                  we'll return element 2 of the list..
                   -1    -2
             -3    -4    -5
              0     1     2
            obj_A obj_B obj_C
            """
            which = abs(which % -len(objList))
        return objList[which]            

def getRandListObj ( objList = [] ):
    """ This function returns a rand element of an objList """
    if ( ( len(objList) == 0 ) or ( not objList ) ):
        debug("Empty objList passed.  Failing gracefully.")
        pygame.display.quit()
        pygame.quit()
        sys.exit()
    else:
        maxWhich = len(objList)
        whichOne = random.randrange(0, maxWhich )
        return getListObj( objList, whichOne )
        
def preload_Clouds ( ):
    global CLOUD_PRAGMA

    if CLOUD_PRAGMA:
        return
    else:
        CLOUD_PRAGMA = True     # we only need to do this once
        for loadCloud in CLOUD_IMG:
            filePath    = os.path.join( IMAGE_PATH, loadCloud )
            loadImg     = pygame.image.load( filePath )
            loadImg.convert()
            CLOUD_LIST.append( loadImg )
    #fi

def preload_Hitboxes ( ):
    global HITBOX_PRAGMA

    if HITBOX_PRAGMA:
        return
    else:
        HITBOX_PRAGMA = True     # we only need to do this once
        for loadHitbox in HITBOX_IMG:
            filePath    = os.path.join( IMAGE_PATH, loadHitbox )
            loadImg     = pygame.image.load( filePath )
            loadImg.convert()
            HITBOX_LIST.append( loadImg )
    #fi
            
class Hitbox( pygame.sprite.Sprite ):
    def __init__( self, screen, center, parent = False, size = 2):
        global HITBOX_PRAGMA

        if not HITBOX_PRAGMA:
            preload_Hitboxes()

        debug( str(parent.type + " tried to create a hitbox..." ) )
        pygame.sprite.Sprite.__init__(self)
        self.type               = "HITBOX"
        self.complained         = False
        if not parent :
            self.parent         = "NONE"
            self.parent.type    = "NONE"
        else:
            self.parent         = parent
        self.image              = HITBOX_LIST[  size ]
        self.rect               = self.image.get_rect()
        self.category           = size
        self.screen             = screen
        self.center             = OFF_SCREEN
        self.update( size, center )
        self.add( HitboxSprites )
        debug( "Hitboxes: " + str( len( HitboxSprites ) ) )
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        pygame.sprite.Sprite.kill(self)
        
    def update( self, size, center ):
        if not self.parent:
            #we didn't have a parent..this is bad.  We're going to kill the object
            self.kill()
            #throw up a complaint
            if ( not self.complained ):
                self.complained = True
                print("Orphaned Hitbox!  Complaining!")
        #fi
        
        if ( self.parent.type == "CLOUD" ):             #only do this part if the hitbox is for a cloud
            if ( self.category != size ):               #resize ourselves if we don't match the clouds size
                self.category   = size
                self.image      = HITBOX_LIST[ self.parent.cloudCategory ]

        self.rect               = self.image.get_rect()
        self.rect.center        = self.parent.rect.center  #move this to be at the center of the parent object
                
class Bird( pygame.sprite.Sprite):
    def __init__( self, screen ):
        pygame.sprite.Sprite.__init__(self)
        self.screen         = screen
        anim                = SEABIRD_ANI
        prefix              = anim["prefix"]
        suffix              = anim["suffix"]
        start_frame         = anim["start"]
        num_frames          = anim["frames"]
        img_name            = "%s_%d%s" % ( prefix, start_frame, suffix )
        filePath            = os.path.join( IMAGE_PATH, img_name )
        self.image          = pygame.image.load( filePath )
        self.image          = pygame.transform.scale( self.image, ( 35, 35 ) )
        self.image          = self.image.convert()
        self.rect           = self.image.get_rect()
        self.raw_height     = 70
        self.raw_width      = 70
        self.rect.height    = 35
        self.rect.width     = 35
        self.spawnx         = 100
        self.spawny         = 430
        self.image_list     = []
        self.frame          = anim["start"]
        self.start_paws     = 3
        self.loop_paws      = self.start_paws
        self.dx             = random.randrange(1,5)
        self.dy             = random.randrange(-1,2)*5
        self.delay          = random.randrange(-1,3)*FRAME_RATE
        self.type           = "BIRD"
        self.hitbox         = Hitbox( screen, self.rect.center, self, MEDIUM_HITBOX  )
        self.init_imgs( anim )
        self.add(BackgroundSprites)     # For now Birdies will just be decoration
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(BackgroundSprites)  # When passed a kill command, it will remove the sprite

    def init_imgs( self, anim = SEABIRD_ANI ):
        prefix = anim["prefix"]
        suffix = anim["suffix"]
        start_frame = anim["start"]
        num_frames = anim["frames"]
        
        for loadList in range ( start_frame, num_frames ):
            img_name    = "%s_%d%s" % ( prefix, loadList, suffix )
            filePath    = os.path.join( IMAGE_PATH, img_name )
            loadImg     = pygame.image.load( filePath )
            halfHigh    = self.raw_height / 2     #should be 35
            halfWide    = self.raw_width / 2      # should be 35
            loadImg     = pygame.transform.scale( loadImg, ( halfHigh, halfWide ) )
            loadImg.convert()
            self.image_list.append( loadImg )

    def update( self ):
        if ( self.delay > 0 ):              # if we have a delay, we wait
            self.delay -= 1
            if ( self.delay < 1 ):          # if the delay has expired, spawn the birdie
                self.rect.centerx = self.spawnx
                self.rect.centery = self.spawny
                self.hitbox.update( self.hitbox.category , self.rect.center ) 
            else:
                return
        else:
            self.loop_paws -= 1

            if ( self.loop_paws <= 0 ):
                self.loop_paws = self.start_paws

                self.frame += 1
                if ( self.frame >= len(self.image_list) ):
                    self.frame = 0
                    self.dy = random.randrange(-1,2)*5

                self.image = self.image_list[self.frame]

            self.rect.centerx += self.dx
            self.rect.centery += self.dy

            if ( self.rect.centerx >= self.screen.get_width() ):
                self.reset()
            if ( self.rect.centery >= self.screen.get_height() ):
                self.reset()
            if ( self.rect.centerx <= -self.rect.width ):
                self.reset()
            if ( self.rect.centery <= -self.rect.height ):
                self.reset()
            self.hitbox.update( self.hitbox.category , self.rect.center ) 
        #fi
                    
    def reset( self ):
        self.dx             = random.randrange(1,5)
        self.dy             = random.randrange(-1,2)*5
        self.rect.center    = OFF_SCREEN
        self.spawnx         = 0
        self.spawny         = random.randrange( self.rect.height, ( self.screen.get_height()  - self.rect.height) )
        self.delay          = random.randrange(-1,3)*FRAME_RATE

class Plane(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        filePath        = os.path.join( IMAGE_PATH, getRandListObj( PLANE_IMG ) )
        self.image      = pygame.image.load( filePath )
        self.image      = self.image.convert()
        self.rect       = self.image.get_rect()
#        pygame.draw.rect( self.image, ( 255, 0, 0 ), self.rect, 2 )       #debugline        
        self.image      = self.image.convert()
        self.screen     = screen
        self.type       = "PLANE"
        #self.hitbox     = Hitbox( screen, self.rect.center, self, MEDIUM_HITBOX  )
        self.snd_refresh()
        self.add(FriendSprites)         # Planes are friendly...we hope
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(FriendSprites)      # When passed a kill command, it will remove the sprite

    def snd_refresh( self ):
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            filePath        = os.path.join( SOUND_PATH, getRandListObj( SNDYAY_AUD ) )            
            self.sndYay     = pygame.mixer.Sound( filePath )
            filePath        = os.path.join( SOUND_PATH, getRandListObj( SNDTHUNDER_AUD ) )            
            self.sndThunder = pygame.mixer.Sound( filePath )
            
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
        #self.hitbox.update( self.hitbox.category , self.rect.center ) 
                
class Island(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        filePath            = os.path.join( IMAGE_PATH, getListObj( ISLAND_IMG, 0 ) )
        self.unhappy_image  = pygame.image.load( filePath )
        self.unhappy_image  = self.unhappy_image.convert()
        filePath            = os.path.join( IMAGE_PATH, getListObj( HAPPY_IMG, 0 ) )
        self.happy_image    = pygame.image.load( filePath )
        self.happy_image    = self.happy_image.convert()
        self.image          = self.unhappy_image
        self.rect           = self.image.get_rect()
        self.screen         = screen
        self.happy          = False
        self.rect.top       = -random.randrange(3,30, 3)*self.rect.height
        self.rect.centerx   = random.randrange(0, self.screen.get_width())
        self.dy             = 5
        self.type           = "ISLAND"
        #self.hitbox         = Hitbox( screen, self.rect.center, self, LARGE_HITBOX  )
        self.reset( False )
        self.add(IslandSprites)     # Islands are friends too...  Not that you'll feel that way after crashing into one
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(IslandSprites)  # When passed a kill command, it will remove the sprite

    
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > self.screen.get_height():
            self.reset()

    def reset(self, CheckPosition = True):
        if ( CheckPosition ):
            self.remove(IslandSprites)
            FreeSpawn = False
            while ( FreeSpawn == False ):
                self.rect.top = -random.randrange(2,10,2)*self.rect.height
                self.rect.centerx = random.randrange(0, self.screen.get_width())
                badIslands = pygame.sprite.spritecollideany( self, IslandSprites )
                if not badIslands:
                    FreeSpawn = True
                #fi
            #wend
            self.add( IslandSprites )
        
        self.image = self.unhappy_image
        self.happy = False
      
    def make_happy( self ):
        self.image = self.happy_image
        self.happy = True
    
class Cloud(pygame.sprite.Sprite):
    def __init__(self, screen, which = 0, threshold = 0):
        global CLOUD_PRAGMA
        """
            which refers to which cloud image to load.
            threshold refers to the minimum score necessary for it spawn the cloud
        """
        if not CLOUD_PRAGMA:
            preload_Clouds()
            
        pygame.sprite.Sprite.__init__(self)
#		filePath            = os.path.join( IMAGE_PATH, getListObj( CLOUD_IMG, which ) )
#        self.image          = pygame.image.load( filePath )
#        self.image          = self.image.convert()
        self.image          = CLOUD_LIST[ which ]
        self.rect           = self.image.get_rect()
        self.raw_height     = self.rect.height
        self.raw_width      = self.rect.width
        self.screen         = screen
        self.threshold      = threshold
        self.cloudCategory  = which
        self.type           = "CLOUD"
        self.hitbox         = Hitbox( screen, self.rect.center, self, self.cloudCategory  )
        self.grazed         = False
        if ( self.cloudCategory == 0 ):
            self.graze_value    = 3
        else:
            self.graze_value    = 1
        self.reset()
        self.add(CloudSprites)     # Clouds...we hates them..and they hates us
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(CloudSprites)  # When passed a kill command, it will remove the sprite
        self.hitbox.rect.center = OFF_SCREEN
        self.hitbox.remove(CloudSprites)    #kill the clouds hitbox too

    def update(self, score = 0):
        if ( score < self.threshold ):
            if self.rect.center != OFF_SCREEN:
                self.rect.center = OFF_SCREEN
                self.hitbox.update( self.cloudCategory, self.rect.center )
            else:
                return
        else:
            self.rect.centerx += self.dx
            self.rect.centery += self.dy
            if self.rect.top > self.screen.get_height():
                self.reset()
            self.hitbox.update( self.cloudCategory, self.rect.center )
    
    def resize_self( self, category = 0 ):
        raw_center          = self.rect.center
        self.rect.center    = raw_center
        self.hitbox.update( self.cloudCategory, self.rect.center )
    
    def reset(self):
        self.cloudCategory      = random.randrange( 0, len(CLOUD_IMG ) )
#		filePath                = os.path.join( IMAGE_PATH, getListObj( CLOUD_IMG, self.cloudCategory ) )
#        self.image              = pygame.image.load( getListObj( filePath )
#        self.image              = pygame.transform.rotate( self.image, random.randrange(0,360,45) )
        self.image              = CLOUD_LIST[ self.cloudCategory ]
        self.image              = self.image.convert()
        self.rect               = self.image.get_rect()
        self.resize_self( self.cloudCategory )
        self.image.convert()
        self.rect.bottom        = random.randrange(-3,0)* self.raw_height
        self.rect.centerx       = random.randrange(0, self.screen.get_width())
        self.dy                 = random.randrange(5, 10)
        self.dx                 = random.randrange(-2, 2)
        self.grazed             = False
        if ( self.cloudCategory == 0 ):
            self.graze_value    = 3
        else:
            self.graze_value    = 1
    
class Ocean(pygame.sprite.Sprite):
    def __init__(self, screen, which = 0):
        pygame.sprite.Sprite.__init__(self)
        if ( which == -1 ):
            filePath    = os.path.join( IMAGE_PATH, getRandListObj( OCEAN_IMG ) )
            self.image  = pygame.image.load( filePath )
        else:
            filePath    = os.path.join( IMAGE_PATH, getListObj( OCEAN_IMG, which ) )
            self.image  = pygame.image.load( filePath )
        self.image      = self.image.convert()
        self.rect       = self.image.get_rect()
        self.dy = 5
        self.screen     = screen
        self.type       = "OCEAN"
        self.add(BackgroundSprites)     # For now the Ocean will just be decoration, after all we wouldn't want it to be an Enemy!
        self.reset()
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(BackgroundSprites)  # When passed a kill command, it will remove the sprite

        
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= self.rect.height:
            self.reset() 
    
    def reset(self):
        self.rect.top = -(self.rect.height - self.screen.get_height())

class Scoreboard(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.lives          = 5
        self.score          = 0
        self.font           = pygame.font.SysFont("None", 40)       # was 50, trying it a touch smaller
        self.screen         = screen
        self.text           = "High Score: %d" % ( self.score )
        self.image          = self.font.render(self.text, 1, (255, 255, 0))
        self.rect           = self.image.get_rect()
        self.bonus          = 0
        self.grazes         = 0
        self.float_grazes   = 0
        self.life_timer     = 0
        self.next_plane     = EXTRA_LIFE
        self.type           = "SCOREBOARD"
        self.add(ScoreSprites)          # This is a very boring sprite.
        self.snd_refresh()
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(ScoreSprites)  # When passed a kill command, it will remove the sprite
        
    def update(self):
#        self.text           = "planes: %d, next plane: %d, bonus: %d, score: %d" % (self.lives, self.next_plane, self.bonus, self.score)
        self.text           = SCORE_STRING  % (self.lives, self.next_plane, self.grazes, self.bonus, self.score)
        self.image          = self.font.render(self.text, 1, (255, 255, 0))
        self.rect           = self.image.get_rect()
        self.rect.centerx   = self.screen.get_width()/2

    def snd_refresh( self ):
        if not pygame.mixer:
            print ("problem with sound")
        else:
            pygame.mixer.init()
            filePath        = os.path.join( SOUND_PATH, getRandListObj( SNDLIFE_AUD ) )            
            self.sndBonusLife = pygame.mixer.Sound( filePath )
            filePath        = os.path.join( SOUND_PATH, getRandListObj( EASTEREGG_AUD ) )            
            self.sndEasterEgg = pygame.mixer.Sound( filePath )
        
    def increment_score( self ):
        score_boost = TARGET_SCORE + ( BONUS_MULTIPLIER * self.bonus )
        self.bonus += 1
        self.score += score_boost
        self.life_timer += score_boost
        return score_boost
    
    def check_extra_life( self ):
        if ( self.life_timer >= EXTRA_LIFE ):
            self.lives += 1
            self.life_timer -= EXTRA_LIFE
            self.next_plane += EXTRA_LIFE
            return 1
        return 0

class Notification( pygame.sprite.Sprite ):
    def __init__( self, screen, text = "yay", duration = 1, position = (250, 250), color = GOOD_COLOR ):
        """
            This will spawn a text notifier at a given 'position' on screen for 'duration' seconds or until it leaves the screen.
        """
        pygame.sprite.Sprite.__init__(self)
        self.font           = pygame.font.SysFont("None", 24 )
        self.screen         = screen
        self.duration       = duration * FRAME_RATE
        self.text           = text
        self.image          = self.font.render( self.text, 1, color )
        self.rect           = self.image.get_rect()
        self.rect.center    = position
        self.dy             = -7
        self.type           = "TEXT"
        
        FreeSpawn = False
        while ( FreeSpawn == False ):
            overlapping_text = pygame.sprite.spritecollideany( self, ScoreSprites )
            if not overlapping_text:
                FreeSpawn = True
            else:
                self.rect.centery += self.rect.height * 1.5
            #fi
        #wend        
        self.add(ScoreSprites)          # This is because text is as boring as the score
        
    def kill( self ):
        self.rect.center = OFF_SCREEN
        self.remove(ScoreSprites)       # When passed a kill command, it will remove the sprite

        
    def update( self ):
        self.duration -= 1
        if ( self.duration <= 0 ):
            self.reset()
        else:
            self.rect.centery += self.dy
            if ( self.rect.top > self.screen.get_height() ):
                self.reset()
            if ( self.rect.bottom < 0 ):
                self.reset()        
            
    def reset( self ):
        self.text = "Empty"
        self.image = self.font.render( self.text, 1, (255, 255, 0 ) )
        self.rect = self.image.get_rect()
        self.rect.center = OFF_SCREEN
        self.kill()
