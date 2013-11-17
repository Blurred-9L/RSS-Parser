# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssTable.rb

require "./LRTable.rb"
require "./Token.rb"
require "./NonTerminal.rb"

class RssTable < LRTable
    public
        def initialize()
            super()
            @tokens = Token.getTokenTypes().types
            @nonTerms = NonTerminal.getTypes().types
        end
        
        def setUp()
            @table[ [0, @tokens["<"]] ] = [SHIFT, 3]
            @table[ [0, @nonTerms["rss_tag"]] ] = [CHANGE, 1]
            @table[ [0, @nonTerms["rss_start"]] ] = [CHANGE, 2]
            
            @table[ [1, @tokens["InputEnd"]] ] = [ACCEPT, 0]
            
            @table[ [2, @tokens["<"]] ] = [SHIFT, 7]
            @table[ [2, @nonTerms["rss_children"]] ] = [CHANGE, 4]
            @table[ [2, @nonTerms["channel_tag"]] ] = [CHANGE, 5]
            @table[ [2, @nonTerms["channel_start"]] ] = [CHANGE, 6]
            
            @table[ [3, @tokens["rss"]] ] = [SHIFT, 8]
            
            @table[ [4, @tokens["</"]] ] = [SHIFT, 10]
            @table[ [4, @nonTerms["rss_end"]] ] = [CHANGE, 9]
            
            @table[ [5, @tokens["<"]] ] = [SHIFT, 7]
            @table[ [5, @tokens["</"]] ] = [REDUCE, 7]
            @table[ [5, @nonTerms["channels"]] ] = [CHANGE, 11]
            @table[ [5, @nonTerms["channel_tag"]] ] = [CHANGE, 12]
            @table[ [5, @nonTerms["channel_start"]] ] = [CHANGE, 6]
            
            @table[ [6, @tokens["<"]] ] = [SHIFT, 25]
            @table[ [6, @tokens["</"]] ] = [REDUCE, 15]
            @table[ [6, @nonTerms["channel_children"]] ] = [CHANGE, 16]
            @table[ [6, @nonTerms["title_tag"]] ] = [CHANGE, 17]
            @table[ [6, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [6, @nonTerms["link_tag"]] ] = [CHANGE, 18]
            @table[ [6, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [6, @nonTerms["description_tag"]] ] = [CHANGE, 19]
            @table[ [6, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [6, @nonTerms["item_tag"]] ] = [CHANGE, 20]
            @table[ [6, @nonTerms["item_start"]] ] = [CHANGE, 24]
            
            @table[ [7, @tokens["channel"]] ] = [SHIFT, 13]
            
            @table[ [8, @tokens["version"]] ] = [SHIFT, 15]
            @table[ [8, @nonTerms["version"]] ] = [CHANGE, 14]
            
            @table[ [9, @tokens["InputEnd"]] ] = [REDUCE, 1]
            
            @table[ [10, @tokens["rss"]] ] = [SHIFT, 26]
            
            @table[ [11, @tokens["</"]] ] = [REDUCE, 5]
            
            @table[ [12, @tokens["<"]] ] = [SHIFT, 7]
            @table[ [12, @tokens["</"]] ] = [REDUCE, 7]
            @table[ [12, @nonTerms["channels"]] ] = [CHANGE, 27]
            @table[ [12, @nonTerms["channel_tag"]] ] = [CHANGE, 12]
            @table[ [12, @nonTerms["channel_start"]] ] = [CHANGE, 6]
            
            @table[ [13, @tokens[">"]] ] = [SHIFT, 28]
            
            @table[ [14, @tokens[">"]] ] = [SHIFT, 29]
            
            @table[ [15, @tokens["="]] ] = [SHIFT, 30]
            
            @table[ [16, @tokens["</"]] ] = [SHIFT, 32]
            @table[ [16, @nonTerms["channel_end"]] ] = [CHANGE, 31]
            
            @table[ [17, @tokens["<"]] ] = [SHIFT, 25]
            @table[ [17, @tokens["</"]] ] = [REDUCE, 15]
            @table[ [17, @nonTerms["channel_children"]] ] = [CHANGE, 33]
            @table[ [17, @nonTerms["title_tag"]] ] = [CHANGE, 17]
            @table[ [17, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [17, @nonTerms["link_tag"]] ] = [CHANGE, 18]
            @table[ [17, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [17, @nonTerms["description_tag"]] ] = [CHANGE, 19]
            @table[ [17, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [17, @nonTerms["item_tag"]] ] = [CHANGE, 20]
            @table[ [17, @nonTerms["item_start"]] ] = [CHANGE, 24]
            
            @table[ [18, @tokens["<"]] ] = [SHIFT, 25]
            @table[ [18, @tokens["</"]] ] = [REDUCE, 15]
            @table[ [18, @nonTerms["channel_children"]] ] = [CHANGE, 34]
            @table[ [18, @nonTerms["title_tag"]] ] = [CHANGE, 17]
            @table[ [18, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [18, @nonTerms["link_tag"]] ] = [CHANGE, 18]
            @table[ [18, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [18, @nonTerms["description_tag"]] ] = [CHANGE, 19]
            @table[ [18, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [18, @nonTerms["item_tag"]] ] = [CHANGE, 20]
            @table[ [18, @nonTerms["item_start"]] ] = [CHANGE, 24]
            
            @table[ [19, @tokens["<"]] ] = [SHIFT, 25]
            @table[ [19, @tokens["</"]] ] = [REDUCE, 15]
            @table[ [19, @nonTerms["channel_children"]] ] = [CHANGE, 35]
            @table[ [19, @nonTerms["title_tag"]] ] = [CHANGE, 17]
            @table[ [19, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [19, @nonTerms["link_tag"]] ] = [CHANGE, 18]
            @table[ [19, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [19, @nonTerms["description_tag"]] ] = [CHANGE, 19]
            @table[ [19, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [19, @nonTerms["item_tag"]] ] = [CHANGE, 20]
            @table[ [19, @nonTerms["item_start"]] ] = [CHANGE, 24]
            
            @table[ [20, @tokens["<"]] ] = [SHIFT, 25]
            @table[ [20, @tokens["</"]] ] = [REDUCE, 15]
            @table[ [20, @nonTerms["channel_children"]] ] = [CHANGE, 36]
            @table[ [20, @nonTerms["title_tag"]] ] = [CHANGE, 17]
            @table[ [20, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [20, @nonTerms["link_tag"]] ] = [CHANGE, 18]
            @table[ [20, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [20, @nonTerms["description_tag"]] ] = [CHANGE, 19]
            @table[ [20, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [20, @nonTerms["item_tag"]] ] = [CHANGE, 20]
            @table[ [20, @nonTerms["item_start"]] ] = [CHANGE, 24]
            
            @table[ [21, @tokens["</"]] ] = [SHIFT, 33]
            @table[ [21, @tokens["Token"]] ] = [SHIFT, 38]
            @table[ [21, @nonTerms["content"]] ] = [CHANGE, 37]
            
            @table[ [22, @tokens["Url"]] ] = [SHIFT, 39]
            
            @table[ [23, @tokens["</"]] ] = [REDUCE, 33]
            @table[ [23, @tokens["Token"]] ] = [SHIFT, 38]
            @table[ [23, @nonTerms["content"]] ] = [CHANGE, 40]
            
            @table[ [24, @tokens["<"]] ] = [SHIFT, 45]
            @table[ [24, @tokens["</"]] ] = [REDUCE, 31]
            @table[ [24, @nonTerms["title_tag"]] ] = [CHANGE, 42]
            @table[ [24, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [24, @nonTerms["link_tag"]] ] = [CHANGE, 43]
            @table[ [24, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [24, @nonTerms["description_tag"]] ] = [CHANGE, 44]
            @table[ [24, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [24, @nonTerms["item_children"]] ] = [CHANGE, 41]
            
            @table[ [25, @tokens["title"]] ] = [SHIFT, 46]
            @table[ [25, @tokens["link"]] ] = [SHIFT, 47]
            @table[ [25, @tokens["description"]] ] = [SHIFT, 48]
            @table[ [25, @tokens["item"]] ] = [SHIFT, 49]
            
            @table[ [26, @tokens[">"]] ] = [SHIFT, 50]
            
            @table[ [27, @tokens["</"]] ] = [REDUCE, 6]
            
            @table[ [28, @tokens["<"]] ] = [REDUCE, 9]
            @table[ [28, @tokens["</"]] ] = [REDUCE, 9]
            
            @table[ [29, @tokens["<"]] ] = [REDUCE, 2]
            
            @table[ [30, @tokens["\""]] ] = [SHIFT, 51]
            
            @table[ [31, @tokens["<"]] ] = [REDUCE, 8]
            @table[ [31, @tokens["</"]] ] = [REDUCE, 8]
            
            @table[ [32, @tokens["channel"]] ] = [SHIFT, 52]
            
            @table[ [33, @tokens["</"]] ] = [REDUCE, 11]
            
            @table[ [34, @tokens["</"]] ] = [REDUCE, 12]
            
            @table[ [35, @tokens["</"]] ] = [REDUCE, 13]
            
            @table[ [36, @tokens["</"]] ] = [REDUCE, 14]
            
            @table[ [37, @tokens["</"]] ] = [SHIFT, 54]
            @table[ [37, @nonTerms["title_end"]] ] = [CHANGE, 53]
            
            @table[ [38, @tokens["</"]] ] = [REDUCE, 33]
            @table[ [38, @tokens["Token"]] ] = [SHIFT, 38]
            @table[ [38, @nonTerms["content"]] ] = [CHANGE, 55]
            
            @table[ [39, @tokens["</"]] ] = [SHIFT, 57]
            @table[ [39, @nonTerms["link_end"]] ] = [CHANGE, 56]
            
            @table[ [40, @tokens["</"]] ] = [SHIFT, 59]
            @table[ [40, @nonTerms["description_end"]] ] = [CHANGE, 58]
            
            @table[ [41, @tokens["</"]] ] = [SHIFT, 61]
            @table[ [41, @nonTerms["item_end"]] ] = [CHANGE, 60]
            
            @table[ [42, @tokens["<"]] ] = [SHIFT, 45]
            @table[ [42, @tokens["</"]] ] = [REDUCE, 31]
            @table[ [42, @nonTerms["title_tag"]] ] = [CHANGE, 42]
            @table[ [42, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [42, @nonTerms["link_tag"]] ] = [CHANGE, 43]
            @table[ [42, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [42, @nonTerms["description_tag"]] ] = [CHANGE, 44]
            @table[ [42, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [42, @nonTerms["item_children"]] ] = [CHANGE, 62]
            
            @table[ [43, @tokens["<"]] ] = [SHIFT, 45]
            @table[ [43, @tokens["</"]] ] = [REDUCE, 31]
            @table[ [43, @nonTerms["title_tag"]] ] = [CHANGE, 42]
            @table[ [43, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [43, @nonTerms["link_tag"]] ] = [CHANGE, 43]
            @table[ [43, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [43, @nonTerms["description_tag"]] ] = [CHANGE, 44]
            @table[ [43, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [43, @nonTerms["item_children"]] ] = [CHANGE, 63]
            
            @table[ [44, @tokens["<"]] ] = [SHIFT, 45]
            @table[ [44, @tokens["</"]] ] = [REDUCE, 31]
            @table[ [44, @nonTerms["title_tag"]] ] = [CHANGE, 42]
            @table[ [44, @nonTerms["title_start"]] ] = [CHANGE, 21]
            @table[ [44, @nonTerms["link_tag"]] ] = [CHANGE, 43]
            @table[ [44, @nonTerms["link_start"]] ] = [CHANGE, 22]
            @table[ [44, @nonTerms["description_tag"]] ] = [CHANGE, 44]
            @table[ [44, @nonTerms["description_start"]] ] = [CHANGE, 23]
            @table[ [44, @nonTerms["item_children"]] ] = [CHANGE, 64]
            
            @table[ [45, @tokens["title"]] ] = [SHIFT, 46]
            @table[ [45, @tokens["link"]] ] = [SHIFT, 47]
            @table[ [45, @tokens["description"]] ] = [SHIFT, 48]
            
            @table[ [46, @tokens[">"]] ] = [SHIFT, 65]
            
            @table[ [47, @tokens[">"]] ] = [SHIFT, 66]
            
            @table[ [48, @tokens[">"]] ] = [SHIFT, 67]
            
            @table[ [49, @tokens[">"]] ] = [SHIFT, 68]
            
            @table[ [50, @tokens["InputEnd"]] ] = [REDUCE, 4]
            
            @table[ [51, @tokens["VersionNum"]] ] = [SHIFT, 69]
            
            @table[ [52, @tokens[">"]] ] = [SHIFT, 70]
            
            @table[ [53, @tokens["<"]] ] = [REDUCE, 16]
            @table[ [53, @tokens["</"]] ] = [REDUCE, 16]
            
            @table[ [54, @tokens["title"]] ] = [SHIFT, 71]
            
            @table[ [55, @tokens["</"]] ] = [REDUCE, 32]
            
            @table[ [56, @tokens["<"]] ] = [REDUCE, 19]
            @table[ [56, @tokens["</"]] ] = [REDUCE, 19]
            
            @table[ [57, @tokens["link"]] ] = [SHIFT, 72]
            
            @table[ [58, @tokens["<"]] ] = [REDUCE, 22]
            @table[ [58, @tokens["</"]] ] = [REDUCE, 22]
            
            @table[ [59, @tokens["description"]] ] = [SHIFT, 73]
            
            @table[ [60, @tokens["<"]] ] = [REDUCE, 25]
            @table[ [60, @tokens["</"]] ] = [REDUCE, 25]
            
            @table[ [61, @tokens["item"]] ] = [SHIFT, 74]
            
            @table[ [62, @tokens["</"]] ] = [REDUCE, 28]
            
            @table[ [63, @tokens["</"]] ] = [REDUCE, 29]
            
            @table[ [64, @tokens["</"]] ] = [REDUCE, 30]
            
            @table[ [65, @tokens["</"]] ] = [REDUCE, 17]
            @table[ [65, @tokens["Token"]] ] = [REDUCE, 17]
            
            @table[ [66, @tokens["Url"]] ] = [REDUCE, 20]
            
            @table[ [67, @tokens["</"]] ] = [REDUCE, 23]
            @table[ [67, @tokens["Token"]] ] = [REDUCE, 23]
            
            @table[ [68, @tokens["<"]] ] = [REDUCE, 26]
            @table[ [68, @tokens["</"]] ] = [REDUCE, 26]
            
            @table[ [69, @tokens["\""]] ] = [SHIFT, 75]
            
            @table[ [70, @tokens["<"]] ] = [REDUCE, 10]
            @table[ [70, @tokens["</"]] ] = [REDUCE, 10]
            
            @table[ [71, @tokens[">"]] ] = [SHIFT, 76]
            
            @table[ [72, @tokens[">"]] ] = [SHIFT, 77]
            
            @table[ [73, @tokens[">"]] ] = [SHIFT, 78]
            
            @table[ [74, @tokens[">"]] ] = [SHIFT, 79]
            
            @table[ [75, @tokens[">"]] ] = [REDUCE, 3]
            
            @table[ [76, @tokens["<"]] ] = [REDUCE, 18]
            @table[ [76, @tokens["</"]] ] = [REDUCE, 18]
            
            @table[ [77, @tokens["<"]] ] = [REDUCE, 21]
            @table[ [77, @tokens["</"]] ] = [REDUCE, 21]
            
            @table[ [78, @tokens["<"]] ] = [REDUCE, 24]
            @table[ [78, @tokens["</"]] ] = [REDUCE, 24]
            
            @table[ [79, @tokens["<"]] ] = [REDUCE, 27]
            @table[ [79, @tokens["</"]] ] = [REDUCE, 27]
        end
end
