"""
    This module contains the music player definition for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from tankGlobals import *

class MusicPlayer( ):
    """
        This class should handle the queuing and playing of music
        .playlist   - Stores a given file list as a playlist, nextTrack() & prevTrack() will reference this
        .track      - Stores the currently playing track # starts at 0
        .current    - Stores the currently playing piece
        .currentName- Stores the name of the currently playing track
        .currentFile- Stores the filename of the currently playing track
        .next       - Stores the next piece to play
        .nextName   - Stores the name of the next queued track
        .nextFile   - Stores the fileename of the next queued track
        .sanity     - Stores sanity of a music variable, if false it's not going to work.
        
        Functions
        loadTrack( whichTrack ) - Loads a specified track in the playlist with bounds of 0 to len(playlist) into a variable list
        nextTrack( forced )     - Either queue up the next track or, if forced, immediately start playing the next track
        prevTrack( forced )     - Either queue up the previous track or, if forced, immediately start playing the previous track
        playTrack( forced )     - Either wait for the player to finish current track or, if forced, immediately start playing
    """
    
    def __init__( self, fileList ):
        if not pygame.mixer:
            debug("Due to lack of sanity, Music was not able to be loaded.")            
            self.sanity             = False
        
        if ( len(fileList) == 0 ):
            debug("fileList given was empty, returning early.")
            self.sanity             = False
            return
        # shouldn't need to init mixer, the sanity_checks should have done that
        
        self.sanity             = True
        self.playlist           = fileList
        self.list_length        = len(fileList)
        self.track              = -1
        self.currentName        = "no name"
        self.currentFile        = "no file"
        self.nextName           = "no name"
        self.nextFile           = "no file"
        if ( self.list_length > 1 ):
            self.next, self.nextName, self.nextFile         = self.loadTrack( ( self.track + 2 ) )
        self.nextTrack( True )  # don't ask me why this works...but what would be correct methods do not...
        
    def loadTrack( self, whichTrack = 0 ):
        global MUSIC_PATH

        work_current    = "no track"
        work_name       = "no name"
        work_file       = "no file"
        
        # Check for system sanity, if system sanity has failed it returns junk
        if not self.sanity:
            return ( work_current, work_name, work_file )
        
        the_Track           = whichTrack
        debug("Requested track %d" % ( the_Track ) )
        # Go ahead and bounds check to make sure the parameter given is in the boundaries of the playlist
        if ( whichTrack >= self.list_length ):
            the_Track       = 0
        if ( whichTrack < 0 ):
            the_Track       = self.list_length - 1

        debug("loading track %d" % ( the_Track ) )
        
        # We had a valid track, go ahead and fetch the name, file and load it into temp vars.
        work_name           = self.playlist[ the_Track ]
        debug("track work_name - %s" % ( work_name ) )
        work_file           = os.path.join( MUSIC_PATH, work_name )
        debug("track work_file - %s" % ( work_file ) )
        work_current        = pygame.mixer.music.load( work_file )
        
        # ok everything should be loaded... return it
        return ( work_current, work_name, work_file )

    def nextTrack( self, forceStart = False ):
        if not self.sanity:
            return
            
        the_Track           = self.track + 1
        if ( the_Track >= self.list_length ):
            the_Track       = 0

        self.track          = the_Track
        self.next, self.nextName, self.nextFile = self.loadTrack( the_Track )
        
        if forceStart:
            self.playTrack( True )
        
    def prevTrack( self, forceStart = False ):
        if not self.sanity:
            return
            
        the_Track           = self.track - 1
        if ( the_Track < 0 ):
            the_Track       = self.list_length - 1

        self.track          = the_Track            
        self.next, self.nextName, self.nextFile = self.loadTrack( the_Track )

        if forceStart:
            self.playTrack( True )

    def playTrack( self, forceStart = False ):
        """
            forceStart tells this module to immediately start playing the next track
        """
        if not self.sanity:
            return
        pygame.mixer.music.set_volume(0.10)
        if ( forceStart ):
            if ( self.nextName == "no name" ):
                #there is no next...
                pass
            else:
                self.currentName    = self.nextName
                self.currentFile    = self.nextFile
                self.current        = self.next     # pygame.mixer.music.load(self.currentFile)
                self.nextName       = "no name"     # we are not preloading the next track yet
                self.nextFile       = "no file"     # see above
        #fi forceStart        

        # now we actually do something
        debug( "Playing %s [%s]." % ( self.currentName, self.currentFile ) )
        pygame.mixer.music.stop()   # stop current music and start afresh
        self.current                = pygame.mixer.music.play( 0 )
        pygame.mixer.music.set_endevent( TRACK_END )
        if ( self.nextName == "no name" ):
            #there is no next...
            pass
        else:
            #debug( pygame.mixer.music.get_busy())
            pygame.mixer.music.queue( self.next )
        
    def __str__( self ):
        """ returns the current playing filename and the next filename """
        if not self.sanity:
            return
            
        output = " Current: %s [%s] \n    Next: %s [%s]\nPlaylist: %s\n Playing: %d" % ( self.currentName, self.currentFile, self.nextName, self.nextFile, self.playlist, self.track )

        return output
 
