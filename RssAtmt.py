# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssAtmt.py

import Token
import FiniteAtmt
import re

class RssAtmt( FiniteAtmt.FiniteAtmt ):
    
    def __init__( self ):
        super( RssAtmt, self ).__init__()
        self.transitions = [ [ 4,  1,  4,  4,  5,  6,  7,  8,  4],
                             [-1, -1, -1,  2, -1, -1, -1, -1, -1],
                             [-1,  3, -1, -1, -1, -1, -1, -1, -1],
                             [-1,  3, -1, -1, -1, -1, -1, -1, -1],
                             [ 4,  4,  4,  4,  4,  4, -1, -1,  4],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1,  9],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1] ]
        self.inputTypes = { "letter" : 0,
                            "digit" : 1,
                            "ascii" : 2,
                            "." : 3,
                            "=" : 4,
                            "\"" : 5,
                            "<" : 6,
                            ">" : 7,
                            "/" : 8 }
                            
    def getTokenString( self ):
        done = False
        error = False
        symbol = ""
        
        self.curState = 0
        while not done and not error:
            symbol += self.line[self.curChar]
            self.curState = self.nextState( self.line[self.curChar] )
            if self.curState >= 0:
                if self.isAcceptState():
                    if not self.includeNextChar():
                        done = True
            else:
                error = True
            
            self.curChar += 1
            
        if error:
            self.handleError( symbol )
            
        return symbol
        
    def nextState( self, charInput ):
        if re.match( "[a-zA-Z]", charInput ) is not None:
            key = "letter"
        elif re.match( "\d", charInput ) is not None:
            key = "digit"
        elif self.inputTypes.has_key( charInput ):
            key = charInput
        else:
            key = "ascii"
            
        return self.transitions[self.curState][self.inputTypes[key]]
        
    def getType( self ):
        tokenTypes = Token.getTokenTypes()
        
        if self.curState == 3:
            key = "VersionNum"
        elif self.curState == 4:
            key = "Token"
        elif self.curState == 5:
            key = "="
        elif self.curState == 6:
            key = "\""
        elif self.curState == 7:
            key = "<"
        elif self.curState == 8:
            key = ">"
        elif self.curState == 9:
            key = "</"
        else:
            key = "Error"
            
        return tokenTypes.types[key]
        
    def isAcceptState( self ):
        acceptedStates = [3, 4, 5, 6, 7, 8, 9]
        
        return self.curState in acceptedStates
        
    def includeNextChar( self ):
        ok = False
        
        if self.curChar + 1 < len( self.line ):
            newState = self.nextState( self.line[self.curChar + 1] )
            if newState >= 0 and not self.isEndOfToken( self.line[self.curChar + 1] ):
                ok = True
                
        return ok
        
    def handleError( self, symbol ):
        while self.curChar < len( self.line ) and not isEndOfToken( self.line[self.curChar] ):
            symbol += self.line[self.curChar]
            self.curChar += 1
