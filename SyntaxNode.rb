# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# SyntaxNode.rb

class SyntaxNode
    attr_reader :type
    attr_writer :type
    
    public
        def initialize( type )
            @type = type
        end
        
        def visitNode()
        end
        
        def to_s()
            str = @type.to_s
            
            return str
        end
end
