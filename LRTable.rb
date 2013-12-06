# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# LRTable.rb

class LRTable
    attr_reader :table

    public
        SHIFT = 0
        REDUCE = 1
        CHANGE = 2
        ACCEPT = 3
        
        def initialize()
            @table = Hash.new()
        end
        
        def setUp()
        end
end
