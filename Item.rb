# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Item.rb

require "./Logger.rb"
require "./RssInfo.rb"

class Item
    attr_reader :hasTitle, :hasLink, :hasDescription
    
    public
        def initialize()
            @hasTitle = false
            @hasLink = false
            @hasDescription = false
        end
        
        def foundTitle()
            if not @hasTitle
                @hasTitle = true
            else
                Logger.instance.writeError( "Error: An item can only have one title." )
                RssInfo.instance.errorsFound += 1
            end
        end
        
        def foundLink()
            if not @hasLink
                @hasLink = true
            else
                Logger.instance.writeError( "Error: An item can only have one link." )
                RssInfo.instance.errorsFound += 1
            end
        end
        
        def foundDescription()
            if not @hasDescription
                @hasDescription = true
            else
                Logger.instance.writeError( "Error: An item can only have one description." )
                RssInfo.instance.errorsFound += 1
            end
        end
end
