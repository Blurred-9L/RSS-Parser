# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# Syntactic.py

import Token
import NonTerminal
import Lexical
import LRTable
import Logger
import re

class Syntactic( object ):
    
    def __init__( self, lex, table, log ):
        self.lexAnalyzer = lex
        self.token = None
        self.correctSyntax = True
        self.stateStack = list()
        self.syntaxTree = list()
        self.lrTable = table
        self.log = log
        
    def analyze( self ):
        done = False
        
        self.stateStack = list()
        self.syntaxTree = list()
        self.stateStack.append( 0 )
        
        self.getToken()
        while self.correctSyntax and not done:
            if self.token is not None:
                self.log.writeDebug( "Token: " + str( self.token.symbol ) )
                self.log.writeDebug( "Type: " + str( self.token.nodeType ) )
                done = self.doAction( self.stateStack[-1], self.token.nodeType )
            else:
                self.log.writeDebug( "Token: $" )
                self.log.writeDebug( "Type: End of Input" )
                done = self.doAction( self.stateStack[-1], Token.getTokenTypes().types["InputEnd"] )
        
        if self.correctSyntax:
            self.log.writeDebug( "Ok" )
            
    def doAction( self, state, tokenType ):
        key = (state, tokenType)
        done = False
        
        if self.lrTable.table.has_key( key ):
            value = self.lrTable.table[key]
            action = value[0]
            index = value[1]
            done = self.applyAction( action, index, tokenType )
        else:
            self.log.writeError( "Error: Could not find pair." )
            self.log.writeError( str( state ) + ", " + str( tokenType ) )
            self.correctSyntax = False
            
        return done
        
    def applyAction( self, action, index, tokenType ):
        done = False
        
        if action == LRTable.LRTable.SHIFT:
            self.log.writeDebug( "Shift " + str( index ) )
            self.stateStack.append( index )
            self.syntaxTree.append( self.token )
            
            self.getToken()
        elif action == LRTable.LRTable.REDUCE:
            self.log.writeDebug( "Reduce: " + str( index ) )
            self.applyReduction( index )
        elif action == LRTable.LRTable.CHANGE:
            self.log.writeError( "Error: Unreacheable code reacher." )
            self.correctSyntax = False
        elif action == LRTable.LRTable.ACCEPT:
            done = True
            
        return done
        
    def applyReduction( self, index ):
        times = [3, 4, 5, 3, 2, 2, 0, 3, 3, 3, 2, 2, 2, 2, 0,
                 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2,
                 0, 2, 0]
                 
        children = []
        for i in range( 0, times[index - 1] ):
            self.stateStack.pop()
            children.append( self.syntaxTree.pop() )
        children.reverse()

        if index == 1:
            nonTermKey = "rss_tag" 
        elif index == 2:
            nonTermKey = "rss_start"
        elif index == 3:
            nonTermKey = "version"
        elif index == 4:
            nonTermKey = "rss_end"
        elif index == 5:
            nonTermKey = "rss_children"
        elif index == 6 or index == 7:
            nonTermKey = "channels"
        elif index == 8:
            nonTermKey = "channel_tag"
        elif index == 9:
            nonTermKey = "channel_start"
        elif index == 10:
            nonTermKey = "channel_end"
        elif index >= 11 and index <= 15:
            nonTermKey = "channel_children"
        elif index == 16:
            nonTermKey = "title_tag"
        elif index == 17:
            nonTermKey = "title_start"
        elif index == 18:
            nonTermKey = "title_end"
        elif index == 19:
            nonTermKey = "link_tag"
        elif index == 20:
            nonTermKey = "link_start"
        elif index == 21:
            nonTermKey = "link_end"
        elif index == 22:
            nonTermKey = "description_tag"
        elif index == 23:
            nonTermKey = "description_start"
        elif index == 24:
            nonTermKey = "description_end"
        elif index == 25:
            nonTermKey = "item_tag"
        elif index == 26:
            nonTermKey = "item_start"
        elif index == 27:
            nonTermKey = "item_end"
        elif index >= 28 and index <= 31:
            nonTermKey = "item_children"
        elif index == 32 or index == 33:
            nonTermKey = "content"

        nonTerm = NonTerminal.getTypes().types[nonTermKey]

        key = (self.stateStack[-1], nonTerm)
        if self.lrTable.table.has_key( key ):
            self.stateStack.append( self.lrTable.table[key][1] )
            self.syntaxTree.append( NonTerminal.NonTerminal( nonTerm, children ) )
        
    def getToken( self ):
        self.token = self.lexAnalyzer.nextToken()
        if self.token is not None:
            if re.match( "^(https?:\/\/)?([\w\.-]+)\.([\w\.]{2,6})([\/\w\.-]*)\/?$", self.token.symbol ) is not None:
                self.token.nodeType = Token.getTokenTypes().types["Url"]
