# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# NonTerminal.py

import SyntaxNode
import Logger
import RssInfo
import Channel
import Item

class NonTerminal( SyntaxNode.SyntaxNode ):
    ntTypes = None
    
    def __init__( self, nodeType, children ):
        super( NonTerminal, self ).__init__( nodeType )
        self.children = children
        
    def visitNode( self, log, rssInfo ):
        if self.nodeType == getTypes().types["channel_tag"]:
            log.writeLog( "InicioCanal\n" )
            rssInfo.channels.append( Channel.Channel() )
        elif self.nodeType == getTypes().types["item_tag"]:
            log.writeLog( "InicioElemento\n" )
            rssInfo.channels[-1].foundItem()
            rssInfo.inItem = True
        elif self.nodeType == getTypes().types["title_start"]:
            log.writeLog( "Titulo:" )
            if rssInfo.inItem:
               rssInfo.channels[-1].items[-1].foundTitle( rssInfo, log )
            else:
               rssInfo.channels[-1].foundTitle( rssInfo, log )
        elif self.nodeType == getTypes().types["link_start"]:
            log.writeLog( "Enlace:" )
            if rssInfo.inItem:
               rssInfo.channels[-1].items[-1].foundLink( rssInfo, log )
            else:
               rssInfo.channels[-1].foundLink( rssInfo, log )
        elif self.nodeType == getTypes().types["description_start"]:
            log.writeLog( "Descripcion:" )
            if rssInfo.inItem:
               rssInfo.channels[-1].items[-1].foundDescription( rssInfo, log )
            else:
               rssInfo.channels[-1].foundDescription( rssInfo, log )
            
        self.visitChildren( log, rssInfo )
        
        if self.nodeType == getTypes().types["channel_tag"]:
            log.writeLog( "FinCanal\n" )
            if not rssInfo.channels[-1].isCorrect():
                log.writeError( "Error: Missing obligatory tag in channel." )
                rssInfo.errorsFound += 1
        elif self.nodeType == getTypes().types["item_tag"]:
            log.writeLog( "FinElemento\n" )
            if not rssInfo.channels[-1].items[-1].isCorrect():
                log.writeError( "Error: Missing obligatory tag in item." )
                rssInfo.errorsFound += 1
            rssInfo.inItem = False
        elif self.nodeType == getTypes().types["title_end"] or self.nodeType == getTypes().types["link_end"] or self.nodeType == getTypes().types["description_end"]:
                log.writeLog( "\n" )
                
    def visitChildren( self, log, rssInfo ):
        for child in self.children:
            child.visitNode( log, rssInfo )
        
def setTypes( types ):
    NonTerminal.ntTypes = types
    
def getTypes():
    return NonTerminal.ntTypes
