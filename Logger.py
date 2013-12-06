# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Logger.py

import sys

class Logger( object ):

    def __init__( self ):
         self.log = sys.stdout
         self.debugLog = sys.stdout
         self.errorLog = sys.stdout
         self.writeEnabled = True
         
    def writeLog( self, logString ):
        if self.writeEnabled:
            self.log.write( logString )
            self.log.flush()
    
    def writeError( self, errString ):
        self.errorLog.write( errString )
        self.errorLog.write( "\n" )
        self.errorLog.flush()
        
    def writeDebug( self, dbgString ):
        self.debugLog.write( dbgString )
        self.debugLog.write( "\n" )
        self.errorLog.flush()
