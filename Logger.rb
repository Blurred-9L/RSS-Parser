# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Logger.rb

require "singleton"

class Logger
    attr_reader :log, :debugLog, :errorLog, :writeEnabled
    attr_writer :log, :debugLog, :errorLog, :writeEnabled
    
    include Singleton
    
    public
        def initialize()
            @log = STDOUT
            @debugLog = STDOUT
            @errorLog = STDOUT
            @writeEnabled = true
        end
        
        def writeLog( logString )
            if @writeEnabled
                @log.print( logString )
            end
        end
        
        def writeError( errString )
            @errorLog.puts( errString )
        end
        
        def writeDebug( dbgString )
            @debugLog.puts( dbgString )
        end
end
