"""
    This module contains the sound subsystem for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from tankGlobals import *

global Sound_Cache

Sound_Cache = {}

class gameSound():
    """
        This class should handle the queuing and playing of game sounds
        .sanity     - Stores sanity of a sound variable, if false it's not going to work.
        
        Functions
    """
    
    def __init__( self ):
        if not pygame.mixer:
            debug("Due to lack of sanity, Sound was not able to be loaded.")            
            self.sanity     = False

        self.sanity         = True

    def Play_Sound( self, whichSound ):
        if not self.sanity:
            #No sanity, we don't attempt to play sounds then
            return False
        
        if ( len( whichSound ) < 1 ):
            #No sound given, abort.
            return False
        
        soundFile = self.Seek_Sound( whichSound )    # Let's go hunt to see if the sound file is already loaded
        
        if ( soundFile == False ):
            # we looked for the sound but got nothing, we'll hafta load it
            tempFile = self.Load_Sound( whichSound )
            if not tempFile:                    # Sound could not be loaded... Give up.
                return False
            else:                
                soundChan = tempFile.play()
                if soundChan is not None:
                    soundChan.set_volume(0.25)
                return True
        else:
            # we looked for the sound and had it, let's play it
            soundChan = soundFile.play()
            if soundChan is not None:
                soundChan.set_volume(0.25)
            return True
            
    def Load_Sound( self, whichSound ):
        """
            This should attempt to construct a soundfile name from the whichSound string given and load it
            First it will smash all spaces and turn them into _
            Uses SOUND_PATH
            -- A more robust version of this would try several extensions besides .ogg before giving up
        """
        work_name = whichSound.replace( " ", "_" )          # spaces converted to underscores
        work_name = work_name + ".ogg"                      # we'll attach an ogg ending as default to sounds,
        work_file = os.path.join( SOUND_PATH, work_name )   # path pre-pended
        if os.path.exists(work_file):                       # If the file actually exists...
            debug("Sound file %s [%s] found." % ( whichSound, work_file ) )
            work_contents = pygame.mixer.Sound( work_file ) # ... we load it
            self.Store_Sound( whichSound, work_contents )   # ... and we store it
            return work_contents                            # ... and we return it to use
        else:
            debug("Sound file %s [%s] could not be found." % ( whichSound, work_file ) )
            return False
        
    def Seek_Sound( self, whichSound ):
        """
            Search through our Sound_Cache to see if the sound file has already been loaded
        """
        if ( len( Sound_Cache ) == 0 ) or ( len( whichSound ) < 1 ):
            return False
        
        if Sound_Cache.__contains__( whichSound ):
            return Sound_Cache[whichSound]
        
        return False
    
    def Store_Sound( self, storeName, storeContents = "none" ):
        """
            Either update a sound in our cache system or add it to the cache
        """
        if ( len( storeName ) < 1 ) or ( storeContents == "none" ) :
            #either no name given or no contents given, skip storage
            return False        
    
        if Sound_Cache.__contains__( storeName ):
            #key exists, are we updating it or ignoring.
            if Sound_Cache[storeName] == storeContents:
                #contents of key match what we're trying to store, return False
                return False
            else:
                #the key exists, but the contents, differ.  Update the contents
                Sound_Cache[storeName] = storeContents
        else:
            #the key didn't exist, store it.
            Sound_Cache[storeName] = storeContents

    def __str__( self ):
        """
            Since there isn't much to display, all this will do is say how big
            the Sound_Cache currently is
        """
            
        output = "Cached Sounds: %d files" % ( len(Sound_Cache) )
        return output
 
               
