# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# NonTerminalTypes.py

import NonTerminalTypes

class RssNTerminals( NonTerminalTypes.NonTerminalTypes ):
    
    def __init__( self ):
        super( RssNTerminals, self ).__init__()
        
    def setTypes( self ):
        self.types["rss_tag"] = 1000
        self.types["rss_start"] = 1001
        self.types["version"] = 1002
        self.types["rss_end"] = 1003
        self.types["rss_children"] = 1004
        self.types["channels"] = 1005
        self.types["channel_tag"] = 1006
        self.types["channel_start"] = 1007
        self.types["channel_end"] = 1008
        self.types["channel_children"] = 1009
        self.types["title_tag"] = 1010
        self.types["title_start"] = 1011
        self.types["title_end"] = 1012
        self.types["link_tag"] = 1013
        self.types["link_start"] = 1014
        self.types["link_end"] = 1015
        self.types["description_tag"] = 1016
        self.types["description_start"] = 1017
        self.types["description_end"] = 1018
        self.types["item_tag"] = 1019
        self.types["item_start"] = 1020
        self.types["item_end"] = 1021
        self.types["item_children"] = 1022
        self.types["content"] = 1023
        
