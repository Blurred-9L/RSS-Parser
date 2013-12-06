# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Item.py

import Logger
import RssInfo

class Item( object ):

    def __init__( self ):
        self.hasTitle = False
        self.hasLink = False
        self.hasDescription = False
        
    def foundTitle( self, rssInfo, log ):
        if not self.hasTitle:
            self.hasTitle = True
        else:
            log.writeError( "Error: An item can only have one title." )
            rssInfo.errorsFound += 1
            
    def foundLink( self, rssInfo, log ):
        if not self.hasLink:
            self.hasLink = True
        else:
            log.writeError( "Error: An item can only have one link." )
            rssInfo.errorsFound += 1
            
    def foundDescription( self, rssInfo, log ):
        if not self.hasDescription:
            self.hasDescription = True
        else:
            log.writeError( "Error: An item can only have one link." )
            rssInfo.errorsFound += 1
            
    def isCorrect( self ):
        return self.hasTitle and self.hasLink and self.hasDescription
