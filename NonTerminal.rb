# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# NonTerminal.rb

require "./SyntaxNode.rb"
require "./NonTerminalTypes.rb"
require "./Logger.rb"
require "./RssInfo.rb"
require "./Channel.rb"

class NonTerminal < SyntaxNode
    attr_reader :children
    attr_writer :children
    
    @@ntTypes = nil
    
    private
        def visitChildren()
            for child in children
                child.visitNode()
            end
        end
    
    public
        def initialize( type, children )
            super( type )
            @children = children
        end
        
        def visitNode()
            if @type == NonTerminal.getTypes().types["channel_tag"]
                Logger.instance.writeLog( "InicioCanal\n" )
                RssInfo.instance.channels.push( Channel.new() )
            elsif @type == NonTerminal.getTypes().types["item_tag"]
                Logger.instance.writeLog( "InicioElemento\n" )
                RssInfo.instance.channels.last().foundItem()
                RssInfo.instance.inItem = true
            elsif @type == NonTerminal.getTypes().types["title_start"]
                Logger.instance.writeLog( "Titulo: " )
                if RssInfo.instance.inItem
                    RssInfo.instance.channels.last().items.last().foundTitle()
                else
                    RssInfo.instance.channels.last().foundTitle()
                end
            elsif @type == NonTerminal.getTypes().types["link_start"]
                Logger.instance.writeLog( "Enlace: " )
                if RssInfo.instance.inItem
                    RssInfo.instance.channels.last().items.last().foundLink()
                else
                    RssInfo.instance.channels.last().foundLink()
                end
            elsif @type == NonTerminal.getTypes().types["description_start"]
                Logger.instance.writeLog( "Descripcion: " )
                if RssInfo.instance.inItem
                    RssInfo.instance.channels.last().items.last().foundDescription()
                else
                    RssInfo.instance.channels.last().foundDescription()
                end
            end
            
            visitChildren()
            
            if @type == NonTerminal.getTypes().types["channel_tag"]
                Logger.instance.writeLog( "FinCanal\n" )
            elsif @type == NonTerminal.getTypes().types["item_tag"]
                Logger.instance.writeLog( "FinElemento\n" )
                RssInfo.instance.inItem = false
            elsif @type == NonTerminal.getTypes().types["title_end"] or
                  @type == NonTerminal.getTypes().types["link_end"] or    
                  @type == NonTerminal.getTypes().types["description_end"]  
                  Logger.instance.writeLog( "\n" )     
            end
        end
        
        def NonTerminal.setTypes( types )
            @@ntTypes = types
        end
        
        def NonTerminal.getTypes()
            return @@ntTypes
        end
end
