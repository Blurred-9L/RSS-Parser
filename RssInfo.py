# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssInfo.py

class RssInfo( object ):
    
    def __init__( self ):
        self.channels = list()
        self.inItem = False
        self.errorsFound = 0
