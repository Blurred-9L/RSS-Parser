# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Lexical.rb

require "./Token.rb"
require "./FiniteAtmt.rb"

class Lexical
    attr_reader :line, :curChar, :curLine
    
    private
        def findStart()
            keepGoing = true
            
            while keepGoing and @automata.endOfToken?( @line[@curChar] )
                @curChar += 1
                if curChar > @line.length()
                    if not nextLine()
                        keepGoing = false
                    end
                end
            end
            
            return keepGoing
        end
        
        def nextLine()
            success = false
            
            @curLine += 1
            while @curLine < @lines.length() and not success
                @line = @lines[@curLine]
                if not @line.empty?
                    success = true
                else
                    @curLine += 1
                end
            end
            @curChar = 0
            
            return success
        end
    
    public
        def initialize( lines, atmt )
            @lines = lines
            @line = ""
            @curChar = 0
            @curLine = 0
            @automata = atmt
        end
        
        def nextToken()
            moreTokens = true
            token = nil
            tokenTypes = Token.getTokenTypes()
            
            if @line.empty?
                if @lines.length() > 0
                    @line = @lines[@curLine]
                    @curChar = 0
                else
                    moreTokens = false
                end
            elsif curChar >= @line.length()
                ok = true
                while curChar >= line.length() and ok
                    ok = nextLine()
                end
                if not ok
                    moreTokens = false
                elsif not findStart()
                    moreTokens = false
                end
            elsif not findStart()
                moreTokens = false
            end
            
            @automata.curChar = @curChar
            @automata.line = @line
            if moreTokens and not @line.empty?
                symbol = @automata.getTokenString()
                @curChar = @automata.curChar
                token = Token.new( symbol, @automata.getType() )
                if tokenTypes.isKeyword?( symbol )
                    token.type = tokenTypes.types[symbol]
                end
            end
            
            return token
        end
end
