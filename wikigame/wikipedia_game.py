#!/usr/bin/env python3
'''
Created on May 23, 2019

main program to run wikigame from CLI

@author: bill
'''

import sys
import wikipedia
from wikigame.wikipath import search_path_between_articles, Article, DataDict, op_backlinks


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 wikipedia_game.py "start_article" "end_article"!')
        sys.exit(-1)
        
    start = sys.argv[1]
    end = sys.argv[2]
    
    # we need to find out the real titles of the articles expected to search    
    try:
        title1 = wikipedia.page(start, auto_suggest=False).title
    except:
        title1 = wikipedia.page(start).title
        
    try:
        title2 = wikipedia.page(end, auto_suggest=False).title
    except:
        title2 = wikipedia.page(end).title
        

    print("Original From [" + start + "] to [" + end + "]")
    print("Found and Run From [" + title1 + "] to [" + title2 + "]")
    
    article1 = Article(title1, repo=DataDict())
    article2 = Article(title2, op=op_backlinks, repo=DataDict())
    
    from datetime import datetime
    
    time1 = datetime.now()
    search_path_between_articles(article1, article2)
    time2  = datetime.now()
    duration = time2 - time1
    print("Total Time Used in seconds: " + str(duration.total_seconds()))    
    