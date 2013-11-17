# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssAtmt.rb

require "./Token.rb"
require "./FiniteAtmt.rb"

class RssAtmt < FiniteAtmt
    private
        def handleError( symbol )
            while @curChar < line.length() and not endOfToken?( @line[@curChar] )
                symbol.concat( @line[@curChar] )
                @curChar += 1
            end
        end
        
    public
        def initialize()
            super()
            @transitions = [ [ 4,  1,  4,  4,  5,  6,  7,  8,  4],
                             [-1, -1, -1,  2, -1, -1, -1, -1, -1],
                             [-1,  3, -1, -1, -1, -1, -1, -1, -1],
                             [-1,  3, -1, -1, -1, -1, -1, -1, -1],
                             [ 4,  4,  4,  4, -1, -1, -1, -1,  4],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1,  9],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1],
                             [-1, -1, -1, -1, -1, -1, -1, -1, -1] ]
            @inputTypes = {
                "letter" => 0,
                "digit" => 1,
                "ascii" => 2,
                "." => 3,
                "=" => 4,
                "\"" => 5,
                "<" => 6,
                ">" => 7,
                "/" => 8
            }
        end
        
        def getTokenString()
            done = false
            error = false
            symbol = ""
            
            @curState = 0
            while not done and not error
                symbol.concat( @line[@curChar] )
                @curState = nextState( @line[@curChar] )
                if @curState >= 0
                    if acceptState?
                        if not includeNextChar?()
                            done = true
                        end
                    end
                else
                    error = true
                end
                
                @curChar += 1;
            end
            
            if error
                handleError( symbol )
            end
            
            return symbol
        end
        
        def nextState( input )
            if /[a-zA-Z]/.match( input )
                key = "letter"
            elsif /\d/.match( input )
                key = "digit"
            elsif @inputTypes.has_key?( input )
                key = input
            else
                key = "ascii"
            end
            
            return @transitions[@curState][@inputTypes[key]]
        end
        
        def getType()
            tokenTypes = Token.getTokenTypes()
            
            if @curState == 3
                key = "VersionNum"
            elsif @curState == 4
                key = "Token"
            elsif @curState == 5
                key = "="
            elsif @curState == 6
                key = "\""
            elsif @curState == 7
                key = "<"
            elsif @curState == 8
                key = ">"
            elsif @curState == 9
                key = "</"
            else
                key = "Error"
            end
            
            return tokenTypes.types[key]
        end
        
        def acceptState?()
            acceptedStates = [3, 4, 5, 6, 7, 8, 9]
            
            return acceptedStates.index( @curState )
        end
        
        def includeNextChar?()
            ok = false
            
            if @curChar + 1 < @line.length
                newState = nextState( @line[@curChar + 1] )
                if newState >= 0 and not endOfToken?( @line[@curChar + 1] )
                    ok = true
                end
            end
            
            return ok
        end
end
