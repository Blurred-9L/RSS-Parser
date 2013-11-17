# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Token.rb

require "./TokenTypes.rb"

class Token
    attr_reader :symbol, :type
    attr_writer :symbol, :type
    
    @@tokenTypes = nil
    
    public
        def initialize( symbol, type )
            @symbol = symbol
            @type = type
        end
        
        def Token.setTokenTypes( types )
            @@tokenTypes = types
        end
        
        def Token.getTokenTypes()
            return @@tokenTypes
        end
        
        def to_s()
            str = symbol + " " + type.to_s
            
            return str
        end
end
