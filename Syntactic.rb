# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Syntactic.rb

require "./Token.rb"
require "./NonTerminal.rb"
require "./Lexical.rb"
require "./LRTable.rb"
require "./Logger.rb"

class Syntactic
    attr_reader :correctSyntax, :stateStack, :syntaxTree
    attr_writer :stateStack, :syntaxTree
    
    private 
        def getToken()
            @token = @lexAnalyzer.nextToken()
            if @token != nil
                if /^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w\.-]*)*\/?$/.match( @token.symbol )
                    @token.type = Token.getTokenTypes().types["Url"]
                end
            end
        end
    
    public
        def initialize( lex, table )
            @lexAnalyzer = lex
            @token = nil
            @correctSyntax = true
            @stateStack = Array.new()
            @syntaxTree = Array.new()
            @lrTable = table
        end
        
        def analyze()
            done = false
            
            @stateStack.clear()
            @syntaxTree.clear()
            @stateStack.push( 0 )
            
            getToken()
            while @correctSyntax and not done
                if @token != nil
                    Logger.instance.writeLog( "Token: #{ @token.symbol }" )
                    Logger.instance.writeLog( "Type: #{ @token.type }" )
                    done = doAction( @stateStack.last(), @token.type )
                else
                    Logger.instance.writeLog( "Token: $" ) 
                    Logger.instance.writeLog( "Type: End of Input" )
                    done = doAction( @stateStack.last(), Token.getTokenTypes().types["InputEnd"] )
                end
            end
            
            if @correctSyntax
                Logger.instance.writeLog( "Ok" )
            end
        end
        
        def doAction( state, input )
            key = [state, input]
            done = false
            
            if @lrTable.table.has_key?( key )
                value = @lrTable.table[key]
                action = value[0]
                index = value[1]
                done = applyAction( action, index, input )
            else
                Logger.instance.writeLog( "Error: Could not find pair." )
                @correctSyntax = false
            end
            
            return done
        end
        
        def applyAction( action, index, input )
            done = false
            
            if action == LRTable::SHIFT
                Logger.instance.writeLog( "Shift: #{ index }" )
                @stateStack.push( index )
                @syntaxTree.push( @token )
                
                getToken()
            elsif action == LRTable::REDUCE
                Logger.instance.writeLog( "Reduce: #{ index }" )
                applyReduction( index )
            elsif action == LRTable::CHANGE
                Logger.instance.writeLog( "Error: Unreacheable code reached." )
                correctSyntax = false
            elsif action == LRTable::ACCEPT
                done = true
            end
            
            return done
        end
        
        def applyReduction( index )
            times = [3, 4, 5, 3, 2, 2, 0, 3, 3, 3, 2, 2, 2, 2, 0,
                     3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2,
                     0, 2, 0]
            
            @stateStack.pop( times[index - 1] )
            children = @syntaxTree.pop( times[index - 1] )
            
            nonTermKey = case index
                when 1 then "rss_tag"
                when 2 then "rss_start"
                when 3 then "version"
                when 4 then "rss_end"
                when 5 then "rss_children"
                when 6..7 then "channels"
                when 8 then "channel_tag"
                when 9 then "channel_start"
                when 10 then "channel_end"
                when 11..15 then "channel_children"
                when 16 then "title_tag"
                when 17 then "title_start"
                when 18 then "title_end"
                when 19 then "link_tag"
                when 20 then "link_start"
                when 21 then "link_end"
                when 22 then "description_tag"
                when 23 then "description_start"
                when 24 then "description_end"
                when 25 then "item_tag"
                when 26 then "item_start"
                when 27 then "item_end"
                when 28..31 then "item_children"
                when 32..33 then "content"
            end
            nonTerm = NonTerminal.getTypes().types[nonTermKey]
            
            key = [@stateStack.last(), nonTerm]
            if @lrTable.table.has_key?( key )
                @stateStack.push( @lrTable.table[key][1] )
                @syntaxTree.push( NonTerminal.new( nonTerm, children ) )
            else
                Logger.instance.writeLog( "Error: Could not apply reduction." )
                @correctSyntax = false
            end
        end
end
