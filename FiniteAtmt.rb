# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# FiniteAtmt.rb

class FiniteAtmt
    attr_reader :curState, :line, :curChar
    attr_writer :line, :curChar
    
    public
        def initialize()
            @curState = nil
            @line = ""
            @curChar = 0
        end
        
        def getTokenString()
            return nil
        end
        
        def nextState( input )
            return nil
        end
        
        def getType()
            return nil
        end
        
        def acceptState?()
            return false
        end
        
        def includeNextChar?()
            return false
        end
        
        def endOfToken?( char )
            return ( char == "\n" or char == "\r" or char == " " or char == "\t" )
        end
end
