# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Lexical.py

import Token
import FiniteAtmt

class Lexical( object ):
    
    def __init__( self, lines, atmt ):
        self.lines = lines
        self.line = ""
        self.curChar = 0
        self.curLine = 0
        self.automata = atmt
        
    def findStart( self ):
        keepGoing = True
        
        while keepGoing and self.automata.isEndOfToken( self.line[self.curChar] ):
            self.curChar += 1
            if self.curChar > len( self.line ):
                if not self.nextLine():
                    keepGoing = False
        
        return keepGoing
        
    def nextLine( self ):
        success = False
        
        self.curLine += 1
        while self.curLine < len( self.lines ) and not success:
            self.line = self.lines[self.curLine]
            if not self.line == "":
                success = True
            else:
                self.curLine += 1
        
        self.curChar = 0
        
        return success
        
    def nextToken( self ):
        moreTokens = True
        token = None
        tokenTypes = Token.getTokenTypes()
        
        if self.line == "":
            if len( self.lines ) > 0:
                self.line = self.lines[self.curLine]
                self.curChar = 0
            else:
                moreTokens = False
        elif self.curChar >= len( self.line ):
            ok = True
            while self.curChar >= len( self.line ) and ok:
                ok = self.nextLine()
            if not ok:
                moreTokens = False
            elif not self.findStart():
                moreTokens = False
        elif not self.findStart():
            moreTokens = False
            
        self.automata.curChar = self.curChar
        self.automata.line = self.line
        if moreTokens and not self.line == "":
            symbol = self.automata.getTokenString()
            self.curChar = self.automata.curChar
            token = Token.Token( symbol, self.automata.getType() )
            if tokenTypes.isKeyword( symbol ):
                token.nodeType = tokenTypes.types[symbol]
                
        return token
