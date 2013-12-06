# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssParser.py

import StringIO
import Logger
import Token
import RssTokens
import RssNTerminals
import NonTerminalTypes
import NonTerminal
import RssAtmt
import Lexical
import RssTable
import Syntactic
import RssInfo

class RssParser( object ):
    INPUT_FILE = "entrada.txt"
    OUTPUT_FILE = "salida.txt"
    DEBUG_FILE = "debug.txt"
    
    def __init__( self, filename ):
        try:
            self.file = open( filename, "r" )
            self.lines = self.file.readlines()
            fileOpen = True
        except IOError:
            fileOpen = False

        if fileOpen:
            self.cleanLines()
            self.file.close()
            self.rewriteLines()
            self.log = Logger.Logger()
            self.log.log = StringIO.StringIO()
            
            self.tokensSetUp()
            self.ntSetUp()
            self.rssAutomata = RssAtmt.RssAtmt()
            self.lexAnalyzer = Lexical.Lexical( self.lines, self.rssAutomata )
            self.rssTable = RssTable.RssTable()
            self.rssTable.setUp()
            self.syntaxAnalyzer = Syntactic.Syntactic( self.lexAnalyzer, self.rssTable, self.log )
            self.log.writeEnabled = False
            self.rssInfo = RssInfo.RssInfo()
        else:
            self.log.writeLog( "Could not open file." )
            exit()
    
    def cleanLines( self ):
        for i in range( 0, len( self.lines ) ):
            self.lines[i] = self.lines[i].strip()
     
    def tokensSetUp( self ):
        self.tokenTypes = RssTokens.RssTokens()
        self.tokenTypes.setTypes()
        Token.setTokenTypes( self.tokenTypes )
        pass
    
    def ntSetUp( self ):
        ntTypes = RssNTerminals.RssNTerminals()
        ntTypes.setTypes()
        NonTerminal.setTypes( ntTypes )
        pass
        
    def checkSyntaxTree( self ):
        if self.syntaxAnalyzer.correctSyntax:
            self.log.writeEnabled = True
            self.log.writeDebug( "Checking..." )
            self.syntaxAnalyzer.syntaxTree[-1].visitNode( self.log, self.rssInfo )
            self.dumpResults()
        else:
            self.log.writeError( "There were syntax errors. No output file will be generated." )
            try:
                out = open( RssParser.OUTPUT_FILE, "w" )
                fileOpen = True
            except IOError:
                fileOpen = False
            if fileOpen:
                out.close()
                
    def dumpResults( self ):
        errors = self.rssInfo.errorsFound
        
        if errors > 0:
            self.log.writeError( "Found " + str( errors ) + " errors. No output file will be generated." )
            try:
                out = open( RssParser.OUTPUT_FILE, "w" )
                fileOpen = True
            except IOError:
                fileOpen = False
            if fileOpen:
                out.close()
        else:
            output = open( RssParser.OUTPUT_FILE, "w" )
            output.write( self.log.log.getvalue() )
            output.close()
        
    def run( self ):
        self.syntaxAnalyzer.analyze()
        self.checkSyntaxTree()
                
    def rewriteLines( self ):
        splitLines = []
        foundRss = False
        for i in range( 0, len( self.lines ) ):
            splitString = self.lines[i].split()
            for j in range( 0, len( splitString ) ):
                if splitString[j].find( "rss" ) >= 0 and not foundRss:
                    splitString[j] = splitString[j].replace( "rss", "rss version = \"2.0\"" )
                    foundRss = True
                print splitString[j]
            self.lines[i] = "".join( splitString )
        self.lines = ["".join( self.lines )]
        print "".join( self.lines )
        #exit()
