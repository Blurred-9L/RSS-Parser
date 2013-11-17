# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# NonTerminal.rb

require "./NonTerminalTypes.rb"

class NonTerminal
    @@ntTypes = nil
    
    public
        def NonTerminal.setTypes( types )
            @@ntTypes = types
        end
        
        def NonTerminal.getTypes()
            return @@ntTypes
        end
end
