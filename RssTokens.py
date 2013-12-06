# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssTokens.py

import TokenTypes

class RssTokens( TokenTypes.TokenTypes ):

    def __init__( self ):
        super( RssTokens, self ).__init__()
        
    def setTypes( self ):
        self.types["Token"] = 0
        self.types["Url"] = 1
        self.types["VersionNum"] = 2
        self.types["="] = 3
        self.types["\""] = 4
        self.types["<"] = 5
        self.types[">"] = 6
        self.types["</"] = 7
        self.types["version"] = 8
        self.types["rss"] = 9
        self.types["channel"] = 10
        self.types["title"] = 11
        self.types["link"] = 12
        self.types["description"] = 13
        self.types["item"] = 14
        self.types["Error"] = 15
        self.types["InputEnd"] = 16
        
    def isKeyword( self, symbol ):
        keywords = ["version", "rss", "channel", "title", "link", "description", "item"]
        
        return symbol in keywords
        
