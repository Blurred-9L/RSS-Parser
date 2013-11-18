# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Token.rb

require "./SyntaxNode.rb"
require "./TokenTypes.rb"
require "./Logger.rb"

class Token < SyntaxNode
    attr_reader :symbol
    attr_writer :symbol
    
    @@tokenTypes = nil
    
    public
        def initialize( symbol, type )
            super( type )
            @symbol = symbol
        end
        
        def visitNode()
            if @type == Token.getTokenTypes().types["Token"]
                Logger.instance.writeLog( "#{ @symbol } " )
            elsif @type == Token.getTokenTypes().types["Url"]
                Logger.instance.writeLog( "#{ @symbol } " )
            end
        end
        
        def Token.setTokenTypes( types )
            @@tokenTypes = types
        end
        
        def Token.getTokenTypes()
            return @@tokenTypes
        end
        
        def to_s()
            str = symbol + " " + super()
            
            return str
        end
end
