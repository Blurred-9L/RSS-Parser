# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# LRTable.py

class LRTable( object ):
    SHIFT = 0
    REDUCE = 1
    CHANGE = 2
    ACCEPT = 3
    
    def __init__( self ):
        self.table = dict()
        
    def setUp( self ):
        pass
