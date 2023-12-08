"""
    This module contains what will be needed to handle scoring for my Tank game
Erin Brown - 2010
 """
 
import os, sys, pygame
from tankGlobals import *

class tankScore( ):
    def __init__( self, whichTank, victory = 10 ):
        self.goal = victory
        self.score = 0
        self.player = whichTank.player
        
    def modify_score( self, howmuch ):
        self.score += howmuch
        
    def check_victory( self ):
        if self.score >= self.goal:
            return True
        else:
            return False
