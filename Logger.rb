# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Logger.rb

require 'singleton'

class Logger
    attr_reader :log, :writeEnabled
    attr_writer :log, :writeEnabled
    
    include Singleton
    
    public
        def initialize()
            @log = STDOUT
            @writeEnabled = true
        end
        
        def writeLog( logString )
            if @writeEnabled
                @log.puts( logString )
            end
        end
end
