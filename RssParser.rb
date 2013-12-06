# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssParser.rb

require "./Token.rb"
require "./RssTokens.rb"
require "./Lexical.rb"
require "./RssAtmt.rb"
require "./RssNTerminals.rb"
require "./RssTable.rb"
require "./Syntactic.rb"
require "./Logger.rb"
require "./RssInfo.rb"
require "stringio"

class RssParser
    private
        def readFile()
            @file.each_line do |line|
                line.chomp!()
                @lines.push( line )
            end
            @file.close()
        end
        
        def tokensSetUp()
            tokenTypes = RssTokens.new()
            tokenTypes.set()
            Token.setTokenTypes( tokenTypes )
        end
        
        def ntSetUp()
            ntTypes = RssNTerminals.new()
            ntTypes.set()
            NonTerminal.setTypes( ntTypes )
        end
        
        def checkSyntaxTree()
            if @syntaxAnalyzer.correctSyntax
                Logger.instance.writeEnabled = true
                Logger.instance.writeDebug( "Checking..." )
                @syntaxAnalyzer.syntaxTree.last().visitNode()
                dumpResults()
            else
                puts "There were syntax errors. No output file will be generated."
            end
        end
        
        def dumpResults()
            errors = RssInfo.instance.errorsFound
            
            if errors > 0
                puts "Found #{ errors }. No output file will be generated."
            else
                file = File.open( OUTPUT_FILE, "w" )
                file.write( Logger.instance.log.string )
            end
        end
    
    public
        INPUT_FILE = "entrada.txt"
        OUTPUT_FILE = "salida.txt"
        DEBUG_FILE = "debug.txt"
        
        def initialize( filename )
            @file = File.open( filename, "r" )
            @lines = Array.new()
            readFile()
            tokensSetUp()
            ntSetUp()
            @rssAutomata = RssAtmt.new()
            @lexAnalyzer = Lexical.new( @lines, @rssAutomata )
            @rssTable = RssTable.new()
            @rssTable.setUp()
            @syntaxAnalyzer = Syntactic.new( @lexAnalyzer, @rssTable )
            Logger.instance.writeEnabled = false
        end
        
        def run()
            @syntaxAnalyzer.analyze()
            checkSyntaxTree()
        end
        
        
end

Logger.instance.log = StringIO.new( "w" )
Logger.instance.debugLog = File.open( RssParser::DEBUG_FILE, "w" )
rssParser = RssParser.new( RssParser::INPUT_FILE )
rssParser.run()
