# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# TokenTypes.rb

class TokenTypes
    attr_reader :types

    public
        def initialize()
            @types = Hash.new()
        end
        
        def set()
        end
        
        def isKeyword?( symbol )
            return false
        end
end
