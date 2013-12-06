# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Token.py

import SyntaxNode
import Logger

class Token( SyntaxNode.SyntaxNode ):
    tokenTypes = None
    
    def __init__( self, symbol, nodeType ):
        super( Token, self ).__init__( nodeType )
        self.symbol = symbol
        
    def visitNode( self, log, rssInfo ):
        self.symbol.strip()
        if self.nodeType == getTokenTypes().types["Token"]:
            log.writeLog( " " + self.symbol )
        elif self.nodeType == getTokenTypes().types["Url"]:
            log.writeLog( " " + self.symbol)
        
    def __str__( self ):
        retStr = self.symbol + " " + super( Token, self ).__str__()
        
        return retStr
        
def setTokenTypes( types ):
    Token.tokenTypes = types
    
def getTokenTypes():
    return Token.tokenTypes
