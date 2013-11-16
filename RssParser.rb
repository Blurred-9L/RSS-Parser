# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssParser.rb

require "./Token.rb"
require "./RssTokens.rb"
require "./Lexical.rb"
require "./RssAtmt.rb"

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
    
    public
        INPUT_FILE = "entrada.txt"
        OUTPUT_FILE = "salida.txt"
        
        def initialize( filename )
            @file = File.open( filename, "r" )
            @lines = Array.new()
            readFile()
            tokensSetUp()
            @rssAutomata = RssAtmt.new()
            @lexAnalyzer = Lexical.new( @lines, @rssAutomata )
        end
        
        def run()
            token = @lexAnalyzer.nextToken()
            while token != nil
                if /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?$/.match( token.symbol )
                    token.type = Token.getTokenTypes().types["Url"]
                end
                puts token
                token = @lexAnalyzer.nextToken()
            end
        end
end

rssParser = RssParser.new( RssParser::INPUT_FILE )
rssParser.run()
