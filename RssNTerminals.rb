# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssNTerminals.rb

require "./NonTerminalTypes.rb"

class RssNTerminals < NonTerminalTypes
    public
        def initialize()
            super()
        end
        
        def set()
            @types["rss_tag"] = 1000
            @types["rss_start"] = 1001
            @types["version"] = 1002
            @types["rss_end"] = 1003
            @types["rss_children"] = 1004
            @types["channels"] = 1005
            @types["channel_tag"] = 1006
            @types["channel_start"] = 1007
            @types["channel_end"] = 1008
            @types["channel_children"] = 1009
            @types["title_tag"] = 1010
            @types["title_start"] = 1011
            @types["title_end"] = 1012
            @types["link_tag"] = 1013
            @types["link_start"] = 1014
            @types["link_end"] = 1015
            @types["description_tag"] = 1016
            @types["description_start"] = 1017
            @types["description_end"] = 1018
            @types["item_tag"] = 1019
            @types["item_start"] = 1020
            @types["item_end"] = 1021
            @types["item_children"] = 1022
            @types["content"] = 1023
        end
end
