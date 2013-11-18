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
    
    public
        INPUT_FILE = "entrada.txt"
        OUTPUT_FILE = "salida.txt"
        
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
        end
        
        def run()
            @syntaxAnalyzer.analyze()
            puts "Checking..."
            @syntaxAnalyzer.syntaxTree.last().visitNode()
        end
end

Logger.instance.writeEnabled = false
rssParser = RssParser.new( RssParser::INPUT_FILE )
rssParser.run()
