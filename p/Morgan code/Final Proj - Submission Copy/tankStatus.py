"""
    This module contains the sound subsystem for my Tank game
Erin Brown - 2010
 """
 
import os,  sys,  pygame,  math,  random

import tankImage, tankBackground
from tankGlobals import *

#notes on tags
# labels        should be moved to iconic graphics if possible
# text          will be live updating
# cur aux       means print the current icon of the current weapon
# xxxxxxx       means print an icon

class tankStatusIcon( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, icon, whichStatus, whichPlayer ):
        """This will be used to keep status icons updated in the status area"""
        pygame.sprite.Sprite.__init__( self )
        workImage       = tankImage.gameImage()
        workImage.image = workImage.Get_Image(icon)
        self.image      = workImage.image
        self.rect       = self.image.get_rect()
        if self.rect.width > width:
            self.rect.width = width
        if self.rect.height > height:
            self.rect.height = height
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < width:
            xOffset     = ( width - workWide ) / 2
        if workHigh < height:
            yOffset     = ( height - workHigh ) / 2
        
        self.rect.left  = STATUS_SCREEN[0] + posLeft + xOffset
        self.rect.top   = STATUS_SCREEN[1] + posTop + yOffset
        self.player     = whichPlayer
        self.type       = "STATUS ICON"
        self.name       = str(whichStatus)
        self.add(StatusSprites)

class tankStatusCDIcon( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, liveIcon, whichStatus, whichPlayer ):
        """This will be used to keep status icons updated in the status area"""
        pygame.sprite.Sprite.__init__( self )
        
        
        self.frames         = liveIcon[0]                           # set the frame number at which to wrap-around to 0
        self.cur_frame      = 0                                     # which frame are we currently on
        self.imglist        = []
        workImage           = tankImage.gameImage()
        for i in range(1, len(liveIcon) ):
            workImage.image = workImage.Get_Image(liveIcon[i])
            self.imglist.append(workImage.image)
            
        self.image          = self.imglist[self.cur_frame]          # set image to current frame
        self.rect           = self.image.get_rect()
        
        if self.rect.width > width:
            self.rect.width = width
        if self.rect.height > height:
            self.rect.height = height
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < width:
            xOffset     = ( width - workWide ) / 2
        if workHigh < height:
            yOffset     = ( height - workHigh ) / 2
        
        self.rect.left  = STATUS_SCREEN[0] + posLeft + xOffset
        self.rect.top   = STATUS_SCREEN[1] + posTop + yOffset
        self.player     = whichPlayer
        workTank        = self.fetchTank( self.player )
        self.tank       = workTank
        
        self.type       = "STATUS ICON"
        self.name       = str(whichStatus)
        self.add(StatusSprites)

    def fetchTank( self, whichPlayer ):
        workTank = "none"
        for tanks in TankSprites:
            if tanks.player == whichPlayer:
                workTank = tanks
        return workTank
        
    def update( self ):
        if self.tank == "none":                         # tank not set
            self.tank = self.fetchTank( self.player)    # try and pull it again
            if self.tank == "none":                     # still no tank? exit out
                return

        workValue       = 0
        maxValue        = 0
        if self.name == "Main Weapon CD":               # linked to primary cannon
            workValue   = self.tank.primary_cd_time
            maxValue    = self.tank.primary_cd * FRAME_RATE
        if self.name == "Aux Weapon CD":                # linked to aux cannon            
            workValue   = self.tank.aux_cd_time
            maxValue    = self.tank.aux_cd * FRAME_RATE

        if maxValue > 0:
            if workValue <= 0:
                self.cur_frame = 0
            elif ( workValue > 0 ) and ( workValue < maxValue / 3 ):
                self.cur_frame = 3
            elif ( workValue > 0 ) and ( workValue < maxValue * 2 / 3 ):
                self.cur_frame = 2
            else:
                self.cur_frame = 1 
        else:
            self.cur_frame  = 0
         
        self.image          = self.imglist[self.cur_frame]

class tankStatusAuxIcon( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, whichStatus, whichPlayer ):
        """This will be used to keep status icons updated in the status area"""
        pygame.sprite.Sprite.__init__( self )
        icon            = "Empty Space"
        workImage       = tankImage.gameImage()
        workImage.image = workImage.Get_Image(icon)
        self.image      = workImage.image
        self.rect       = self.image.get_rect()
        self.blankImage = self.image
        self.def_top    = STATUS_SCREEN[1] + posTop
        self.def_left   = STATUS_SCREEN[0] + posLeft
        self.def_wide   = width
        self.def_high   = height

        if self.rect.width > self.def_wide:
            self.rect.width = self.def_wide
        if self.rect.height > self.def_high:
            self.rect.height = self.def_high

        self.player     = whichPlayer
        workTank        = self.fetchTank( self.player )
        self.tank       = workTank
        self.type       = "STATUS ICON"
        self.name       = str(whichStatus)
        self.Aux_Slot   = int(whichStatus[len(whichStatus)-1])
        self.set_def_loc( )
        self.keep_loc ( )
        self.add(StatusSprites)    

    def fetchTank( self, whichPlayer ):
        workTank = "none"
        for tanks in TankSprites:
            if tanks.player == whichPlayer:
                workTank = tanks
        return workTank

    def set_def_loc( self ):
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < self.def_wide:
            xOffset     = ( self.def_wide - workWide ) / 2
        if workHigh < self.def_high:
            yOffset     = ( self.def_high - workHigh ) / 2
        self.def_top   += yOffset
        self.def_left  += xOffset        
    
    def keep_loc( self ):    
        self.rect.top       = self.def_top
        self.rect.left      = self.def_left
        self.rect.width     = self.def_wide
        self.rect.height    = self.def_high
            
    def update( self ):
        if self.tank == "none":                         # tank not set
            self.tank = self.fetchTank( self.player)    # try and pull it again
            if self.tank == "none":                     # still no tank? exit out
                return
        icon = "none"
        if self.tank.cur_aux_ammo >= self.Aux_Slot:     # show me if the tank has aux ammo >= which slot I am
            if   self.tank.aux_weapon == AUX_1:         # Missiles
                icon        = R1_MISSILE[1]
            elif self.tank.aux_weapon == AUX_2:         # Shield Pens
                icon        = R1_SHIELD_PEN[1]
            elif self.tank.aux_weapon == AUX_3:         # Leeches
                icon        = R1_LEECH[1]
            elif self.tank.aux_weapon == AUX_4:         # Torpedoes
                icon        = R1_TORPEDO[1]
            elif self.tank.aux_weapon == AUX_5:         # Mines
                icon        = R1_MINE[1]

            workImage       = tankImage.gameImage()
            workImage.image = workImage.Get_Image(icon)
            self.image      = workImage.image
        else:                                           # hide me
            self.image      = self.blankImage
        self.set_def_loc( )
        self.keep_loc ( )
        
class tankStatusLiveText( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, size, whichField, whichPlayer ):
        """This will do live text of stats"""
        pygame.sprite.Sprite.__init__( self )
        # first let's snag the player we refer to
        #just because we don't find a tank, doesn't mean we can't still exist, it just means we don't update until it does exist
        self.screen         = screen
        self.text           = "0"
        self.textSize       = size
        self.font           = pygame.font.SysFont("None", self.textSize )        
        self.image          = self.font.render( self.text, 1, clr_GREEN )       
        self.rect           = self.image.get_rect()
        self.def_top        = STATUS_SCREEN[1] + posTop
        self.def_left       = STATUS_SCREEN[0] + posLeft
        self.def_wide       = width
        self.def_high       = height
        self.field          = whichField
        self.player         = whichPlayer
        workTank            = self.fetchTank( self.player )
        self.tank           = workTank
        self.set_def_loc( )
        self.keep_loc ( )
        self.add( StatusSprites )

    def set_def_loc( self ):
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < self.def_wide:
            xOffset     = ( self.def_wide - workWide ) / 2
            if self.textSize == 32:
                xOffset /= 3
        if workHigh < self.def_high:
            yOffset     = ( self.def_high - workHigh ) / 2
        self.def_top   += yOffset
        self.def_left  += xOffset
    
    def keep_loc( self ):    
        self.rect.top       = self.def_top
        self.rect.left      = self.def_left
        self.rect.width     = self.def_wide
        self.rect.height    = self.def_high
        
    def fetchTank( self, whichPlayer ):
        workTank = "none"
        for tanks in TankSprites:
            if tanks.player == whichPlayer:
                workTank = tanks
        return workTank
    
    def update( self ):
        if self.tank == "none":                         # tank not set
            self.tank = self.fetchTank( self.player)    # try and pull it again
            if self.tank == "none":                     # still no tank? exit out
                return
        # now select data by field and return it
        outField        = "0"                 # well actually it's a spot in baseball, right?
        useColor        = clr_GREEN
        if   self.field == "Cur Energy":
            outField = "%2d" % self.tank.cur_energy
        elif self.field == "Max Energy":
            outField = str( self.tank.max_energy )
        elif self.field == "Cur Armor":
            outField = str( self.tank.cur_health )
        elif self.field == "Max Armor":
            outField = str( self.tank.max_health )
        elif self.field == "Cur Shield":
            outField = str( self.tank.cur_shield )
        elif self.field == "Max Shield":
            outField = str( self.tank.max_shield )
        elif self.field == "Cur Bullet":
            outField = str( self.tank.cur_primary_ammo )
        elif self.field == "Max Bullet":
            outField = str( self.tank.max_primary_ammo )
        elif self.field == "Hull Rank":
            outField = str( self.tank.upgrades.hull_rank )
        elif self.field == "Shield Cap Rnk":
            outField = str( self.tank.upgrades.shield_rank )
        elif self.field == "Energy Tnk Rnk":
            outField = str( self.tank.upgrades.energy_rank )
        elif self.field == "Regen Rank":
            outField = str( self.tank.upgrades.regen_rank )
        elif self.field == "Shield Gen Rnk":
            outField = str( self.tank.upgrades.shield_gen_rank )
        elif self.field == "Energy Gen Rnk":
            outField = str( self.tank.upgrades.energy_gen_rank )
        elif self.field == "Cannon Rank":
            outField = str( self.tank.upgrades.cannon_rank )
        elif self.field == "Aux Wpn Rank":
            outField = str( self.tank.upgrades.aux_rank )
        elif self.field == "Ammo Rank":
            outField = str( self.tank.upgrades.ammo_rank )
        elif self.field == "P1 Score" or self.field == "P2 Score":
            outField = str( self.tank.score.score )
            useColor = clr_RED
        if self.text == outField:                           # no change, skip
            return
        # otherwise, something changed, update
        self.text           = outField
        self.image          = self.font.render( self.text, 1, useColor )       
        self.keep_loc()
           
class tankStatusLabelText( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, size, whichField ):
        """This will just print a label of text"""
        pygame.sprite.Sprite.__init__( self )
        # first let's snag the player we refer to
       #just because we don't find a tank, doesn't mean we can't still exist, it just means we don't update until it does exist
        self.screen         = screen
        self.text           = "0"
        self.textSize       = size
        self.font           = pygame.font.SysFont("None", self.textSize )        
        self.image          = self.font.render( self.text, 1, clr_GREEN )       
        self.rect           = self.image.get_rect()
        self.def_top        = STATUS_SCREEN[1] + posTop
        self.def_left       = STATUS_SCREEN[0] + posLeft
        self.def_wide       = width
        self.def_high       = height
        self.field          = whichField
        self.extraOffsetX = 0
        self.extraOffsetY = 0
        self.spawn_text()
        self.set_def_loc( )
        self.keep_loc ( )
        self.add( StatusSprites )

    def set_def_loc( self ):
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < self.def_wide:
            xOffset     = ( self.def_wide - workWide ) / 2
            if self.textSize == 32:
                xOffset /= 3
            if self.textSize == 16:
                xOffset /= 2
        if workHigh < self.def_high:
            yOffset     = ( self.def_high - workHigh ) / 2
        self.def_top   += yOffset + self.extraOffsetY + 6 
        self.def_left  += xOffset + self.extraOffsetX
    
    def keep_loc( self ):    
        self.rect.top       = self.def_top
        self.rect.left      = self.def_left
        self.rect.width     = self.def_wide
        self.rect.height    = self.def_high
    
    def spawn_text( self ):
        # now select data by field and return it
        outField        = "0"                 # well actually it's a spot in baseball, right?
        if   self.field == "Shield Label":
            outField = "Shields"
            self.extraOffsetX = 16
        elif self.field == "Vitals Lbl":
            outField = "Vitals"
            self.extraOffsetX = 6
        elif self.field == "Hull Label":
            outField = "Hu"
            self.extraOffsetX = 2
        elif self.field == "Shield Cap Lbl":
            outField = "SC"
            self.extraOffsetX = 2
        elif self.field == "Energy Tnk Lbl":
            outField = "ET"
            self.extraOffsetX = 2
        elif self.field == "Generators Lbl":
            outField = "Regens"
            self.extraOffsetX = 4
        elif self.field == "Regen Label":
            outField = "Re"
            self.extraOffsetX = 2
        elif self.field == "Shield Gen Lbl":
            outField = "SG"
            self.extraOffsetX = 2
        elif self.field == "Energy Gen Lbl":
            outField = "EG"
            self.extraOffsetX = 2
        elif self.field == "Weapons Lbl":
            outField = "Weapon"
            self.extraOffsetX = 2
        elif self.field == "Cannon Label":
            outField = "MW"
            self.extraOffsetX = 1
        elif self.field == "Aux Wpn Label":
            outField = "AW"
            self.extraOffsetX = 1
        elif self.field == "Ammo Label":
            outField = "Am"
            self.extraOffsetX = 1
        elif self.field == "SCORES":
            outField = "SCORES"
            self.extraOffsetX = 5
        if self.text == outField:                           # no change, skip
            return
        # otherwise, something changed, update
        self.text           = outField
        self.image          = self.font.render( self.text, 1, clr_GREEN )       
        self.keep_loc()

class tankStatusArmorIcon( pygame.sprite.Sprite ):
    def __init__( self, screen, posLeft, posTop, width, height, liveIcon, whichStatus, whichPlayer ):
        """This will be used to keep status icons updated in the status area"""
        pygame.sprite.Sprite.__init__( self )
        
        
        self.frames         = liveIcon[0]                           # set the frame number at which to wrap-around to 0
        self.cur_frame      = 0                                     # which frame are we currently on
        self.imglist        = []
        workImage           = tankImage.gameImage()
        for i in range(1, len(liveIcon) ):
            workImage.image = workImage.Get_Image(liveIcon[i])
            self.imglist.append(workImage.image)
            
        self.image          = self.imglist[self.cur_frame]          # set image to current frame
        self.rect           = self.image.get_rect()
        
        if self.rect.width > width:
            self.rect.width = width
        if self.rect.height > height:
            self.rect.height = height
        xOffset         = 0
        yOffset         = 0
        workWide        = self.rect.width
        workHigh        = self.rect.height
        if workWide < width:
            xOffset     = ( width - workWide ) / 2
        if workHigh < height:
            yOffset     = ( height - workHigh ) / 2
        
        self.rect.left  = STATUS_SCREEN[0] + posLeft + xOffset
        self.rect.top   = STATUS_SCREEN[1] + posTop + yOffset
        self.player     = whichPlayer
        workTank        = self.fetchTank( self.player )
        self.tank       = workTank
        
        self.type       = "STATUS ICON"
        self.name       = str(whichStatus)
        self.add(StatusSprites)

    def fetchTank( self, whichPlayer ):
        workTank = "none"
        for tanks in TankSprites:
            if tanks.player == whichPlayer:
                workTank = tanks
        return workTank
        
    def update( self ):
        if self.tank == "none":                         # tank not set
            self.tank = self.fetchTank( self.player)    # try and pull it again
            if self.tank == "none":                     # still no tank? exit out
                return

        workValue       = max(0, self.tank.cur_health)
        maxValue        = max(1, self.tank.max_health)
        perValue        = ( workValue * 100 ) / maxValue

        if   workValue == maxValue:       #100% HP
            self.cur_frame = 0
        elif perValue >= 95:
            self.cur_frame = 1
        elif perValue >= 90:
            self.cur_frame = 2
        elif perValue >= 85:
            self.cur_frame = 3
        elif perValue >= 80:
            self.cur_frame = 4
        elif perValue >= 75:
            self.cur_frame = 5
        elif perValue >= 70:
            self.cur_frame = 6
        elif perValue >= 65:
            self.cur_frame = 7
        elif perValue >= 60:
            self.cur_frame = 8
        elif perValue >= 55:
            self.cur_frame = 9
        elif perValue >= 50:
            self.cur_frame = 10
        elif perValue >= 45:
            self.cur_frame = 11
        elif perValue >= 40:
            self.cur_frame = 12
        elif perValue >= 35:
            self.cur_frame = 13
        elif perValue >= 30:
            self.cur_frame = 14
        elif perValue >= 25:
            self.cur_frame = 15
        elif perValue >= 20:
            self.cur_frame = 16
        elif perValue >= 15:
            self.cur_frame = 17
        elif perValue >= 10:
            self.cur_frame = 18
        elif perValue >=  5:
            self.cur_frame = 19
        elif perValue >=  0:
            self.cur_frame = 20
        else:
            self.cur_frame  = 0
         
        self.image          = self.imglist[self.cur_frame]        
        
def Test_Image( whichImage ):
        """
            Attempt to verify if an image exists
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
            debug("Validate: file %s [%s] found." % ( whichImage, work_file ) )
            return True
        else:
            debug("Validate: file %s [%s] not found." % ( whichImage, work_file ) )
            return False

def iconify_status( theScreen ):
    highlight_status()
    #fillage next
    ss_text = 16
    s_text  = 20
    m_text  = 24
    l_text  = 32
    worktable = [[]]
    for whichPlayer in range(1,4):
        if whichPlayer == 1:
            worktable = p1_status_table
        elif whichPlayer == 2:
            worktable = p2_status_table
        elif whichPlayer == 3:
            worktable = aux_info_lines
        else:
            continue
        for line in range(0,len(worktable)):
            # break into parameters
            param1 = worktable[line][0]
            param2 = worktable[line][1]
            param3 = worktable[line][2]
            
            theLeft, theTop, theWide, theHigh = param2
            debug("Filling in P%1d's %s with %s" % ( 1, param1, param3 ) )
            workCommand = param3
            if   workCommand == "label":
                tankStatusLabelText( theScreen, theLeft, theTop, theWide, theHigh, ss_text, param1 )        
                debug("Label done")
            elif workCommand == "label_big":
                tankStatusLabelText( theScreen, theLeft, theTop, theWide, theHigh, l_text, param1 )        
                debug("Label_big done")
            elif workCommand == "MAIN READY":
                tankStatusCDIcon( theScreen, theLeft, theTop, theWide, theHigh, MAIN_READY, param1, whichPlayer )
                debug("Main Ready")
            elif workCommand == "AUX READY":
                tankStatusCDIcon( theScreen, theLeft, theTop, theWide, theHigh, AUX_READY, param1, whichPlayer )
                debug("Aux Ready")
            elif workCommand == "ARMOR PLATE":
                tankStatusArmorIcon( theScreen, theLeft, theTop, theWide, theHigh, ARMOR_PLATE, param1, whichPlayer )
                debug("Aux Ready")
            elif workCommand == "cur aux":
                tankStatusAuxIcon( theScreen, theLeft, theTop, theWide, theHigh, param1, whichPlayer )
                debug("cur aux")
            elif ( workCommand == "text s" ):
                tankStatusLiveText( theScreen, theLeft, theTop, theWide, theHigh, s_text, param1, whichPlayer )
                debug("text s done")
            elif ( workCommand == "text m" ):
                tankStatusLiveText( theScreen, theLeft, theTop, theWide, theHigh, m_text, param1, whichPlayer )
                debug("text m done")
            elif ( workCommand == "text l" ):
                tankStatusLiveText( theScreen, theLeft, theTop, theWide, theHigh, l_text, param1, whichPlayer )
                debug("text l done")
            elif ( workCommand == "scorefield" ):
                tankStatusLiveText( theScreen, theLeft, theTop, theWide, theHigh, l_text, param1, int(param1[1]) )
                debug("scorefield for Player %d done" % int(param1[1]) )
            else:
                if Test_Image(workCommand):
                    #go ahead and paint the icon
                    tankStatusIcon( theScreen, theLeft, theTop, theWide, theHigh, workCommand,  param1, whichPlayer )
                    debug("workCommand 'putting %s at %s' done" % ( workCommand, str( param2 ) ) )
                    pass   
        
def highlight_status( ):
    workSprite  = "none"
    workSurface = "none"    
    for theSprite in BackgroundSprites:
        if theSprite.name == "Status Screen":
            workSprite = theSprite
    if workSprite == "none":        # no status screen sprite found
        return
    workSurface = workSprite.image

    #line first
    for line in range(0,len(p1_divider_lines)):
        #debug("Drawing P%1d's %s" % ( 1, p1_divider_lines[line][0] ) )        
        pygame.draw.line( workSurface, clr_WHITE, p1_divider_lines[line][1], p1_divider_lines[line][2], 1 )
    for line in range(0,len(p2_divider_lines)):
        #debug("Drawing P%1d's %s" % ( 2, p2_divider_lines[line][0] ) )
        pygame.draw.line( workSurface, clr_WHITE, p2_divider_lines[line][1], p2_divider_lines[line][2], 1 )
    #boxes next
    for line in range(0,len(p1_status_table)):
        #debug("Drawing P%1d's %s" % ( 1, p1_status_table[line][0] ) )
        pygame.draw.rect( workSurface, clr_BLACK, p1_status_table[line][1], 0 )
    for line in range(0,len(p2_status_table)):
        #debug("Drawing P%1d's %s" % ( 2, p2_status_table[line][0] ) )
        pygame.draw.rect( workSurface, clr_BLACK, p2_status_table[line][1], 0 )
    for line in range(0,len(aux_info_lines)):
        #debug("Drawing P%1d's %s" % ( 2, p2_status_table[line][0] ) )
        pygame.draw.rect( workSurface, clr_BLACK, aux_info_lines[line][1], 0 )

aux_info_lines = [
[ "SCORES",          (  600,   10,  104,   32 ), "label_big"    ],
[ "P1 Score",        (  605,   50,   40,   32 ), "scorefield"   ],
[ "P2 Score",        (  660,   50,   40,   32 ), "scorefield"   ],
]
        
#reminder lines are ( x1, y1 ), ( x2, y2 )
p1_divider_lines = [
[ "Div Line E",      (   38,  108 ), (   43,   82 )  ],   # line is botleft to topright
[ "Div Line A",      (  118,  108 ), (  123,   82 )  ],   # line is botleft to topright
[ "Div Line S",      (  198,  108 ), (  203,   82 )  ]    # line is botleft to topright
]

p2_divider_lines = [
[ "Div Line E",      ( 1238,  108 ), ( 1243,   82 )  ],   # line is botleft to topright
[ "Div Line A",      ( 1158,  108 ), ( 1163,   82 )  ],   # line is botleft to topright
[ "Div Line S",      ( 1078,  108 ), ( 1083,   82 )  ]    # line is botleft to topright
]

#reminder rectangles are either ( L, T, W, H ) or ( L, T ), ( W, H)
p1_status_table = [
[ "Energy Tank",     (    5,    5,   64,   64 ), "Energy Tank"  ], 
[ "Cur Energy",      (    5,   80,   32,   32 ), "text l"       ], 
[ "Max Energy",      (   45,   80,   32,   32 ), "text l"       ], 

[ "Armor Plate",     (   85,    5,   64,   64 ), "ARMOR PLATE"  ], 
[ "Cur Armor",       (   85,   80,   32,   32 ), "text l"       ], 
[ "Max Armor",       (  125,   80,   32,   32 ), "text l"       ], 
  
[ "Shield Label",    (  165,   50,   72,   24 ), "label"        ], 
[ "Cur Shield",      (  165,   80,   32,   32 ), "text l"       ], 
[ "Max Shield",      (  205,   80,   32,   32 ), "text l"       ], 

[ "Main Weapon CD",  (  165,    5,   32,   32 ), "MAIN READY"   ],
[ "Aux Weapon CD",   (  205,    5,   32,   32 ), "AUX READY"    ],

[ "Bullet Icon@2x",  (  245,    5,   32,   32 ), "R1Bullet 1"   ], 
[ "Cur Bullet",      (  245,   45,   32,   32 ), "text l"       ], 
[ "Max Bullet",      (  245,   80,   32,   32 ), "text l"       ], 

[ "Aux Ammo Icon1",  (  290,    5,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon3",  (  290,   45,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon5",  (  290,   85,   32,   32 ), "cur aux"      ], 

[ "Aux Ammo Icon2",  (  335,    5,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon4",  (  335,   45,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon6",  (  335,   85,   32,   32 ), "cur aux"      ], 

[ "Vitals Lbl",      (  380,    5,   50,   24 ), "label"        ], 
[ "Hull Label",      (  380,   40,   24,   24 ), "label"        ], 
[ "Hull Rank",       (  410,   40,   24,   24 ), "text m"       ], 
[ "Shield Cap Lbl",  (  380,   70,   24,   24 ), "label"        ], 
[ "Shield Cap Rnk",  (  410,   70,   24,   24 ), "text m"       ], 
[ "Energy Tnk Lbl",  (  380,  100,   24,   24 ), "label"        ], 
[ "Energy Tnk Rnk",  (  410,  100,   24,   24 ), "text m"       ], 

[ "Generators Lbl",  (  440,    5,   50,   24 ), "label"        ], 
[ "Regen Label",     (  440,   40,   24,   24 ), "label"        ], 
[ "Regen Rank",      (  470,   40,   24,   24 ), "text m"       ], 
[ "Shield Gen Lbl",  (  440,   70,   24,   24 ), "label"        ], 
[ "Shield Gen Rnk",  (  470,   70,   24,   24 ), "text m"       ], 
[ "Energy Gen Lbl",  (  440,  100,   24,   24 ), "label"        ], 
[ "Energy Gen Rnk",  (  470,  100,   24,   24 ), "text m"       ], 

[ "Weapons Lbl",     (  500,    5,   50,   24 ), "label"        ], 
[ "Cannon Label",    (  500,   40,   24,   24 ), "label"        ], 
[ "Cannon Rank",     (  530,   40,   24,   24 ), "text m"       ], 
[ "Aux Wpn Label",   (  500,   70,   24,   24 ), "label"        ], 
[ "Aux Wpn Rank",    (  530,   70,   24,   24 ), "text m"       ], 
[ "Ammo Label",      (  500,  100,   24,   24 ), "label"        ], 
[ "Ammo Rank",       (  530,  100,   24,   24 ), "text m"       ]  
]

p2_status_table = [
[ "Energy Tank",     ( 1205,    5,   64,   64 ), "Energy Tank"  ], 
[ "Cur Energy",      ( 1205,   80,   32,   32 ), "text l"       ], 
[ "Max Energy",      ( 1245,   80,   32,   32 ), "text l"       ], 

[ "Armor Plate",     ( 1125,    5,   64,   64 ), "ARMOR PLATE"  ], 
[ "Cur Armor",       ( 1125,   80,   32,   32 ), "text l"       ], 
[ "Max Armor",       ( 1165,   80,   32,   32 ), "text l"       ], 
  
[ "Shield Label",    ( 1045,   50,   72,   24 ), "label"        ], 
[ "Cur Shield",      ( 1045,   80,   32,   32 ), "text l"       ], 
[ "Max Shield",      ( 1085,   80,   32,   32 ), "text l"       ], 

[ "Main Weapon CD",  ( 1045,    5,   32,   32 ), "MAIN READY"   ],
[ "Aux Weapon CD",   ( 1085,    5,   32,   32 ), "AUX READY"    ],

[ "Bullet Icon@2x",  ( 1000,    5,   32,   32 ), "R1Bullet 2"   ], 
[ "Cur Bullet",      ( 1005,   45,   32,   32 ), "text l"       ], 
[ "Max Bullet",      ( 1005,   80,   32,   32 ), "text l"       ], 

[ "Aux Ammo Icon1",  (  955,    5,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon3",  (  955,   45,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon5",  (  955,   85,   32,   32 ), "cur aux"      ], 

[ "Aux Ammo Icon2",  (  910,    5,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon4",  (  910,   45,   32,   32 ), "cur aux"      ], 
[ "Aux Ammo Icon6",  (  910,   85,   32,   32 ), "cur aux"      ], 

[ "Vitals Lbl",      (  850,    5,   50,   24 ), "label"        ], 
[ "Hull Label",      (  850,   40,   24,   24 ), "label"        ], 
[ "Hull Rank",       (  880,   40,   24,   24 ), "text m"       ], 
[ "Shield Cap Lbl",  (  850,   70,   24,   24 ), "label"        ], 
[ "Shield Cap Rnk",  (  880,   70,   24,   24 ), "text m"       ], 
[ "Energy Tnk Lbl",  (  850,  100,   24,   24 ), "label"        ], 
[ "Energy Tnk Rnk",  (  880,  100,   24,   24 ), "text m"       ], 

[ "Generators Lbl",  (  790,    5,   50,   24 ), "label"        ], 
[ "Regen Label",     (  790,   40,   24,   24 ), "label"        ], 
[ "Regen Rank",      (  820,   40,   24,   24 ), "text m"       ], 
[ "Shield Gen Lbl",  (  790,   70,   24,   24 ), "label"        ], 
[ "Shield Gen Rnk",  (  820,   70,   24,   24 ), "text m"       ], 
[ "Energy Gen Lbl",  (  790,  100,   24,   24 ), "label"        ], 
[ "Energy Gen Rnk",  (  820,  100,   24,   24 ), "text m"       ], 

[ "Weapons Lbl",     (  730,    5,   50,   24 ), "label"        ], 
[ "Cannon Label",    (  730,   40,   24,   24 ), "label"        ], 
[ "Cannon Rank",     (  760,   40,   24,   24 ), "text m"       ], 
[ "Aux Wpn Label",   (  730,   70,   24,   24 ), "label"        ], 
[ "Aux Wpn Rank",    (  760,   70,   24,   24 ), "text m"       ],
[ "Ammo Label",      (  730,  100,   24,   24 ), "label"        ], 
[ "Ammo Rank",       (  760,  100,   24,   24 ), "text m"       ]  
]
