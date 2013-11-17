# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssTokens.rb

require "./TokenTypes.rb"

class RssTokens < TokenTypes
    public
        def initialize
            super()
        end
        
        def set()
            @types["Token"] = 0
            @types["Url"] = 1
            @types["VersionNum"] = 2
            @types["="] = 3
            @types["\""] = 4
            @types["<"] = 5
            @types[">"] = 6
            @types["</"] = 7
            @types["version"] = 8
            @types["rss"] = 9
            @types["channel"] = 10
            @types["title"] = 11
            @types["link"] = 12
            @types["description"] = 13
            @types["item"] = 14
            @types["Error"] = 15
            @types["InputEnd"] = 16
        end
        
        def isKeyword?( symbol )
            keywords = ["version", "rss", "channel", "title", "link", "description", "item"]
            
            return ( keywords.index( symbol ) != nil )
        end
end
