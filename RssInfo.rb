# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssInfo.rb

require "singleton"

class RssInfo
    attr_reader :channels, :inItem, :errorsFound
    attr_writer :channels, :inItem, :errorsFound
    
    include Singleton
    
    public
        def initialize()
            @channels = Array.new()
            @inItem = false
            @errorsFound = 0
        end
end
