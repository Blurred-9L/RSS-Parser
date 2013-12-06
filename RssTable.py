# encoding: utf-8
# Rodrigo Fuentes Hernandez
# aka Blurred_9L
# Compiladores CUCEI 2013B
# RssTable.py

import LRTable
import Token
import NonTerminal

class RssTable( LRTable.LRTable ):
    
    def __init__( self ):
        super( RssTable, self ).__init__()
        self.tokens = Token.getTokenTypes().types
        self.nonTerms = NonTerminal.getTypes().types
        
    def setUp( self ):
        self.table[ (0, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 3]
        self.table[ (0, self.nonTerms["rss_tag"]) ] = [LRTable.LRTable.CHANGE, 1]
        self.table[ (0, self.nonTerms["rss_start"]) ] = [LRTable.LRTable.CHANGE, 2]
        
        self.table[ (1, self.tokens["InputEnd"]) ] = [LRTable.LRTable.ACCEPT, 0]
        
        self.table[ (2, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 7]
        self.table[ (2, self.nonTerms["rss_children"]) ] = [LRTable.LRTable.CHANGE, 4]
        self.table[ (2, self.nonTerms["channel_tag"]) ] = [LRTable.LRTable.CHANGE, 5]
        self.table[ (2, self.nonTerms["channel_start"]) ] = [LRTable.LRTable.CHANGE, 6]
        
        self.table[ (3, self.tokens["rss"]) ] = [LRTable.LRTable.SHIFT, 8]
        
        self.table[ (4, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 10]
        self.table[ (4, self.nonTerms["rss_end"]) ] = [LRTable.LRTable.CHANGE, 9]
        
        self.table[ (5, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 7]
        self.table[ (5, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 7]
        self.table[ (5, self.nonTerms["channels"]) ] = [LRTable.LRTable.CHANGE, 11]
        self.table[ (5, self.nonTerms["channel_tag"]) ] = [LRTable.LRTable.CHANGE, 12]
        self.table[ (5, self.nonTerms["channel_start"]) ] = [LRTable.LRTable.CHANGE, 6]
        
        self.table[ (6, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 25]
        self.table[ (6, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 15]
        self.table[ (6, self.nonTerms["channel_children"]) ] = [LRTable.LRTable.CHANGE, 16]
        self.table[ (6, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 17]
        self.table[ (6, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (6, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 18]
        self.table[ (6, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (6, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 19]
        self.table[ (6, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (6, self.nonTerms["item_tag"]) ] = [LRTable.LRTable.CHANGE, 20]
        self.table[ (6, self.nonTerms["item_start"]) ] = [LRTable.LRTable.CHANGE, 24]
        
        self.table[ (7, self.tokens["channel"]) ] = [LRTable.LRTable.SHIFT, 13]
        
        self.table[ (8, self.tokens["version"]) ] = [LRTable.LRTable.SHIFT, 15]
        self.table[ (8, self.nonTerms["version"]) ] = [LRTable.LRTable.CHANGE, 14]
        
        self.table[ (9, self.tokens["InputEnd"]) ] = [LRTable.LRTable.REDUCE, 1]
        
        self.table[ (10, self.tokens["rss"]) ] = [LRTable.LRTable.SHIFT, 26]
        
        self.table[ (11, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 5]
        
        self.table[ (12, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 7]
        self.table[ (12, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 7]
        self.table[ (12, self.nonTerms["channels"]) ] = [LRTable.LRTable.CHANGE, 27]
        self.table[ (12, self.nonTerms["channel_tag"]) ] = [LRTable.LRTable.CHANGE, 12]
        self.table[ (12, self.nonTerms["channel_start"]) ] = [LRTable.LRTable.CHANGE, 6]
        
        self.table[ (13, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 28]
        
        self.table[ (14, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 29]
        
        self.table[ (15, self.tokens["="]) ] = [LRTable.LRTable.SHIFT, 30]
        
        self.table[ (16, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 32]
        self.table[ (16, self.nonTerms["channel_end"]) ] = [LRTable.LRTable.CHANGE, 31]
        
        self.table[ (17, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 25]
        self.table[ (17, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 15]
        self.table[ (17, self.nonTerms["channel_children"]) ] = [LRTable.LRTable.CHANGE, 33]
        self.table[ (17, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 17]
        self.table[ (17, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (17, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 18]
        self.table[ (17, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (17, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 19]
        self.table[ (17, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (17, self.nonTerms["item_tag"]) ] = [LRTable.LRTable.CHANGE, 20]
        self.table[ (17, self.nonTerms["item_start"]) ] = [LRTable.LRTable.CHANGE, 24]
        
        self.table[ (18, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 25]
        self.table[ (18, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 15]
        self.table[ (18, self.nonTerms["channel_children"]) ] = [LRTable.LRTable.CHANGE, 34]
        self.table[ (18, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 17]
        self.table[ (18, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (18, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 18]
        self.table[ (18, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (18, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 19]
        self.table[ (18, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (18, self.nonTerms["item_tag"]) ] = [LRTable.LRTable.CHANGE, 20]
        self.table[ (18, self.nonTerms["item_start"]) ] = [LRTable.LRTable.CHANGE, 24]
        
        self.table[ (19, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 25]
        self.table[ (19, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 15]
        self.table[ (19, self.nonTerms["channel_children"]) ] = [LRTable.LRTable.CHANGE, 35]
        self.table[ (19, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 17]
        self.table[ (19, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (19, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 18]
        self.table[ (19, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (19, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 19]
        self.table[ (19, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (19, self.nonTerms["item_tag"]) ] = [LRTable.LRTable.CHANGE, 20]
        self.table[ (19, self.nonTerms["item_start"]) ] = [LRTable.LRTable.CHANGE, 24]
        
        self.table[ (20, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 25]
        self.table[ (20, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 15]
        self.table[ (20, self.nonTerms["channel_children"]) ] = [LRTable.LRTable.CHANGE, 36]
        self.table[ (20, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 17]
        self.table[ (20, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (20, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 18]
        self.table[ (20, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (20, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 19]
        self.table[ (20, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (20, self.nonTerms["item_tag"]) ] = [LRTable.LRTable.CHANGE, 20]
        self.table[ (20, self.nonTerms["item_start"]) ] = [LRTable.LRTable.CHANGE, 24]
        
        self.table[ (21, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 33]
        self.table[ (21, self.tokens["Token"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (21, self.tokens["Url"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (21, self.nonTerms["content"]) ] = [LRTable.LRTable.CHANGE, 37]
        
        self.table[ (22, self.tokens["Url"]) ] = [LRTable.LRTable.SHIFT, 39]
        
        self.table[ (23, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 33]
        self.table[ (23, self.tokens["Token"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (23, self.tokens["Url"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (23, self.nonTerms["content"]) ] = [LRTable.LRTable.CHANGE, 40]
        
        self.table[ (24, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 45]
        self.table[ (24, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 31]
        self.table[ (24, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 42]
        self.table[ (24, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (24, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 43]
        self.table[ (24, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (24, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 44]
        self.table[ (24, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (24, self.nonTerms["item_children"]) ] = [LRTable.LRTable.CHANGE, 41]
        
        self.table[ (25, self.tokens["title"]) ] = [LRTable.LRTable.SHIFT, 46]
        self.table[ (25, self.tokens["link"]) ] = [LRTable.LRTable.SHIFT, 47]
        self.table[ (25, self.tokens["description"]) ] = [LRTable.LRTable.SHIFT, 48]
        self.table[ (25, self.tokens["item"]) ] = [LRTable.LRTable.SHIFT, 49]
        
        self.table[ (26, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 50]
        
        self.table[ (27, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 6]
        
        self.table[ (28, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 9]
        self.table[ (28, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 9]
        
        self.table[ (29, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 2]
        
        self.table[ (30, self.tokens["\""]) ] = [LRTable.LRTable.SHIFT, 51]
        
        self.table[ (31, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 8]
        self.table[ (31, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 8]
        
        self.table[ (32, self.tokens["channel"]) ] = [LRTable.LRTable.SHIFT, 52]
        
        self.table[ (33, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 11]
        
        self.table[ (34, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 12]
        
        self.table[ (35, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 13]
        
        self.table[ (36, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 14]
        
        self.table[ (37, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 54]
        self.table[ (37, self.nonTerms["title_end"]) ] = [LRTable.LRTable.CHANGE, 53]
        
        self.table[ (38, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 33]
        self.table[ (38, self.tokens["Token"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (38, self.tokens["Url"]) ] = [LRTable.LRTable.SHIFT, 38]
        self.table[ (38, self.nonTerms["content"]) ] = [LRTable.LRTable.CHANGE, 55]
        
        self.table[ (39, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 57]
        self.table[ (39, self.nonTerms["link_end"]) ] = [LRTable.LRTable.CHANGE, 56]
        
        self.table[ (40, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 59]
        self.table[ (40, self.nonTerms["description_end"]) ] = [LRTable.LRTable.CHANGE, 58]
        
        self.table[ (41, self.tokens["</"]) ] = [LRTable.LRTable.SHIFT, 61]
        self.table[ (41, self.nonTerms["item_end"]) ] = [LRTable.LRTable.CHANGE, 60]
        
        self.table[ (42, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 45]
        self.table[ (42, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 31]
        self.table[ (42, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 42]
        self.table[ (42, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (42, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 43]
        self.table[ (42, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (42, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 44]
        self.table[ (42, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (42, self.nonTerms["item_children"]) ] = [LRTable.LRTable.CHANGE, 62]
        
        self.table[ (43, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 45]
        self.table[ (43, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 31]
        self.table[ (43, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 42]
        self.table[ (43, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (43, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 43]
        self.table[ (43, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (43, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 44]
        self.table[ (43, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (43, self.nonTerms["item_children"]) ] = [LRTable.LRTable.CHANGE, 63]
        
        self.table[ (44, self.tokens["<"]) ] = [LRTable.LRTable.SHIFT, 45]
        self.table[ (44, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 31]
        self.table[ (44, self.nonTerms["title_tag"]) ] = [LRTable.LRTable.CHANGE, 42]
        self.table[ (44, self.nonTerms["title_start"]) ] = [LRTable.LRTable.CHANGE, 21]
        self.table[ (44, self.nonTerms["link_tag"]) ] = [LRTable.LRTable.CHANGE, 43]
        self.table[ (44, self.nonTerms["link_start"]) ] = [LRTable.LRTable.CHANGE, 22]
        self.table[ (44, self.nonTerms["description_tag"]) ] = [LRTable.LRTable.CHANGE, 44]
        self.table[ (44, self.nonTerms["description_start"]) ] = [LRTable.LRTable.CHANGE, 23]
        self.table[ (44, self.nonTerms["item_children"]) ] = [LRTable.LRTable.CHANGE, 64]
        
        self.table[ (45, self.tokens["title"]) ] = [LRTable.LRTable.SHIFT, 46]
        self.table[ (45, self.tokens["link"]) ] = [LRTable.LRTable.SHIFT, 47]
        self.table[ (45, self.tokens["description"]) ] = [LRTable.LRTable.SHIFT, 48]
        
        self.table[ (46, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 65]
        
        self.table[ (47, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 66]
        
        self.table[ (48, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 67]
        
        self.table[ (49, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 68]
        
        self.table[ (50, self.tokens["InputEnd"]) ] = [LRTable.LRTable.REDUCE, 4]
        
        self.table[ (51, self.tokens["VersionNum"]) ] = [LRTable.LRTable.SHIFT, 69]
        
        self.table[ (52, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 70]
        
        self.table[ (53, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 16]
        self.table[ (53, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 16]
        
        self.table[ (54, self.tokens["title"]) ] = [LRTable.LRTable.SHIFT, 71]
        
        self.table[ (55, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 32]
        
        self.table[ (56, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 19]
        self.table[ (56, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 19]
        
        self.table[ (57, self.tokens["link"]) ] = [LRTable.LRTable.SHIFT, 72]
        
        self.table[ (58, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 22]
        self.table[ (58, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 22]
        
        self.table[ (59, self.tokens["description"]) ] = [LRTable.LRTable.SHIFT, 73]
        
        self.table[ (60, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 25]
        self.table[ (60, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 25]
        
        self.table[ (61, self.tokens["item"]) ] = [LRTable.LRTable.SHIFT, 74]
        
        self.table[ (62, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 28]
        
        self.table[ (63, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 29]
        
        self.table[ (64, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 30]
        
        self.table[ (65, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 17]
        self.table[ (65, self.tokens["Token"]) ] = [LRTable.LRTable.REDUCE, 17]
        self.table[ (65, self.tokens["Url"]) ] = [LRTable.LRTable.REDUCE, 17]
        
        self.table[ (66, self.tokens["Url"]) ] = [LRTable.LRTable.REDUCE, 20]
        
        self.table[ (67, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 23]
        self.table[ (67, self.tokens["Token"]) ] = [LRTable.LRTable.REDUCE, 23]
        self.table[ (67, self.tokens["Url"]) ] = [LRTable.LRTable.REDUCE, 23]
        
        self.table[ (68, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 26]
        self.table[ (68, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 26]
        
        self.table[ (69, self.tokens["\""]) ] = [LRTable.LRTable.SHIFT, 75]
        
        self.table[ (70, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 10]
        self.table[ (70, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 10]
        
        self.table[ (71, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 76]
        
        self.table[ (72, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 77]
        
        self.table[ (73, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 78]
        
        self.table[ (74, self.tokens[">"]) ] = [LRTable.LRTable.SHIFT, 79]
        
        self.table[ (75, self.tokens[">"]) ] = [LRTable.LRTable.REDUCE, 3]
        
        self.table[ (76, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 18]
        self.table[ (76, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 18]
        
        self.table[ (77, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 21]
        self.table[ (77, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 21]
        
        self.table[ (78, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 24]
        self.table[ (78, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 24]
        
        self.table[ (79, self.tokens["<"]) ] = [LRTable.LRTable.REDUCE, 27]
        self.table[ (79, self.tokens["</"]) ] = [LRTable.LRTable.REDUCE, 27]


