# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# NonTerminal.rb

require "./SyntaxNode.rb"
require "./NonTerminalTypes.rb"

class NonTerminal < SyntaxNode
    attr_reader :children
    attr_writer :children
    
    @@ntTypes = nil
    
    public
        def initialize( type, children )
            super( type )
            @children = children
        end
        
        def NonTerminal.setTypes( types )
            @@ntTypes = types
        end
        
        def visitNode()
            for child in children
                child.visitNode()
            end
        end
        
        def NonTerminal.getTypes()
            return @@ntTypes
        end
end
