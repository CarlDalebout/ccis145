"""
    This module contains what is needed to handle image loading for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from tankGlobals import *

global Image_Cache

Image_Cache = {}

class gameImage():
    """
        This class should handle the storing and retrieving of game art        
        Functions
    """
    
    def __init__( self ):
        pass
        
    def Get_Image( self, whichImage ):        
        if ( len( whichImage ) < 1 ):
            #No image given, abort.
            return False
        
        imageFile = self.Seek_Image( whichImage )    # Let's go hunt to see if the image file is already loaded
        
        if ( imageFile == False ):
            # we looked for the image but got nothing, we'll hafta load it
            tempFile = self.Load_Image( whichImage )
            if not tempFile:                         # Image could not be loaded... Give up.
                tempFile = self.Load_Image("Bad Image")
            return tempFile
        else:
            # we looked for the sound and had it, let's play it
            return imageFile
            
    def Load_Image( self, whichImage ):
        """
            This should attempt to construct an imagefile name from the whichImage string given and load it
            First it will smash all spaces and turn them into _
            Uses IMAGE_PATH
        """
        work_name = whichImage.replace( " ", "_" )          # spaces converted to underscores
        gif_name  = work_name + ".gif"                      # we'll attach a gif ending as default to image,
        png_name  = work_name + ".png"                      # we'll attach a png ending as default to image,
        gif_file  = os.path.join( IMAGE_PATH, gif_name )    # path pre-pended
        png_file  = os.path.join( IMAGE_PATH, png_name )    # path pre-pended
        if os.path.exists( gif_file ):
            work_file = gif_file
        else:
            work_file = png_file
        if os.path.exists(work_file):                       # If the file actually exists...
            debug("Image file %s [%s] found." % ( whichImage, work_file ) )
            work_contents = pygame.image.load( work_file )  # ... we load it
            work_contents.convert_alpha()                   # ... and we convert it keeping alpha layers
            self.Store_Image( whichImage, work_contents )   # ... and we store it
            return work_contents                            # ... and we return it to use
        else:
            debug("Image file %s [%s] could not be found." % ( whichImage, work_file ) )
            return False
        
    def Seek_Image( self, whichImage ):
        """
            Search through our Image_Cache to see if the image file has already been loaded
        """
        if ( len( Image_Cache ) == 0 ) or ( len( whichImage ) < 1 ):
            return False
        
        if Image_Cache.__contains__( whichImage ):
            return Image_Cache[whichImage]
        
        return False
    
    def Store_Image( self, storeName, storeContents = "none" ):
        """
            Either update an image in our cache system or add it to the cache
        """
        if ( len( storeName ) < 1 ) or ( storeContents == "none" ) :
            #either no name given or no contents given, skip storage
            return False        
    
        if Image_Cache.__contains__( storeName ):
            #key exists, are we updating it or ignoring.
            if Image_Cache[storeName] == storeContents:
                #contents of key match what we're trying to store, return False
                return False
            else:
                #the key exists, but the contents, differ.  Update the contents
                Image_Cache[storeName] = storeContents
        else:
            #the key didn't exist, store it.
            Image_Cache[storeName] = storeContents

    def __str__( self ):
        """
            Since there isn't much to display, all this will do is say how big
            the Image_Cache currently is
        """
            
        output = "Cached Images: %d files" % ( len(Image_Cache) )
        return output
 
               
def main():
    global testImage
    global tankScreen
    
    tankScreen = pygame.display.set_mode((640,480))
    testImage = gameImage()
    newImage = testImage.Get_Image("R1Torpedo 1")    
    tankScreen.blit(newImage, (10,10))
    pygame.display.flip()
    
if __name__ == "__main__":
    main()
    
        
