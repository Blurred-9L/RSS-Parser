# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# SyntaxNode.py

class SyntaxNode( object ):
    
    def __init__( self, nodeType ):
        self.nodeType = nodeType
    
    def visitNode( self, log, rssInfo ):
        pass
    
    def __str__( self ):
        retStr = str( self.nodeType )
        
        return retStr
