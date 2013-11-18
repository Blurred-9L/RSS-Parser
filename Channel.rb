# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Channel.rb

require "./Logger.rb"
require "./RssInfo.rb"
require "./Item.rb"

class Channel
    attr_reader :hasTitle, :hasLink, :hasDescription, :items
    
    public
        def initialize()
            @hasTitle = false
            @hasLink = false
            @hasDescription = false
            @items = Array.new()
        end
        
        def foundTitle()
            if not @hasTitle
                @hasTitle = true
            else
                Logger.instance.writeError( "Error: A channel can only have one title." )
                RssInfo.instance.errorsFound += 1
            end
        end
        
        def foundLink()
            if not @hasLink
                @hasLink = true
            else
                Logger.instance.writeError( "Error: A channel can only have one link." )
                RssInfo.instance.errorsFound += 1
            end
        end
        
        def foundDescription()
            if not @hasDescription
                @hasDescription = true
            else
                Logger.instance.writeError( "Error: A channel can only have one description." )
                RssInfo.instance.errorsFound += 1
            end
        end
        
        def foundItem()
            @items.push( Item.new() )
        end
end
