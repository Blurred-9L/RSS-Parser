# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# FiniteAtmt.py

class FiniteAtmt( object ):
    
    def __init__( self ):
        self.curState = None
        self.line = ""
        self.curChar = 0
        
    def getTokenString( self ):
        return None
        
    def nextState( self, charInput ):
        return None
        
    def getType( self ):
        return None
        
    def isAcceptState( self ):
        return False
        
    def includeNextChar( self ):
        return False
        
    def isEndOfToken( self, char ):
        return ( char == "\n" or char == "\r" or char == " " or char == "\t" )
