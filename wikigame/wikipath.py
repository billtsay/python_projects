#!/usr/bin/env python3

'''
Created on May 21, 2019

Prepared for Stratifyd

Wikipedia game python code

See readme.txt

@author: bill
'''

import copy
import wikipedia
import wikipediaapi
wiki = wikipediaapi.Wikipedia('en')

def backlinks(page):
    return page.backlinks

op_backlinks = lambda page: page.backlinks
op_links = lambda page: page.links

# extends dict to trace if key is marked/used.
class DataDict(dict):    
    def __init__(self, *args, **kw):
        super(DataDict,self).__init__(*args, **kw)
        self._marked_ = dict()
        
    def mark(self, key):
        if self.get(key) != None:
            self._marked_[key] = True
            
    def marked(self, key):
        if self.get(key) == None: return False
        if self._marked_.get(key) == None:
            self._marked_[key] = False
            
        return self._marked_[key]
        

class Article(object):
    def __init__(self, title, op=op_links, repo=DataDict()):
        self._title_ = title
        self.data = repo
        self.data[self._title_] = [self._title_]
        self.op = op
        
    def next(self):
        keys = list(self.data.keys())
        
        for key in keys:
            if not self.data.marked(key):
                links = self.op(wiki.page(key))
                self.data.mark(key)
                for l in links:
                    if self.data.get(l) == None:
                        p = copy.copy(self.data[key])
                        p.append(l)
                        self.data[l] = p            
                    
    def size(self):
        return len(self.data)
        
def title_match(a, b):
    x = [x.lower() for x in a.split()] 
    y = [x.lower() for x in b.split()]
    
    return x == y

def list_match(l1, l2):
    s = set()
    for a in l1:
        for b in l2:
            if title_match(a,b):
                s.add((a,b))
    return s

def matched(forward, backward):
    m = list_match(forward.data.keys(), backward.data.keys())
    
    if (len(m) > 0):
        l = 10000
        z = None
        
        # find min len of path
        for k1, k2 in m:
            x1 = forward.data[k1]
            x2 = backward.data[k2]
            x2.reverse()
            y = x1[:-1] + x2
            
            if l > len(y):
                l = len(y)
                z = y
                
        print(z)
        return True
    else:
        return False
        
# depreciated, internal test    
def search_path(start, end):
    forward = Article(start, repo=DataDict())
    backward = Article(end, op=op_backlinks, repo=DataDict())
    
    while not matched(forward, backward):    
        if forward.size() > backward.size():
            print("loading backward .... ")
            backward.next()
            print("backward : " + str(backward.size()))
        else:
            print("loading forward .... ")
            forward.next()
            print("forward : " + str(forward.size()))
    
from wikigame.cachedict import DataDict as CachedDict

# depreciated, internal test    
def cached_search_path(start, end):
    repo1 = CachedDict('forward')
    repo1.clear()
    repo2 = CachedDict('backward')
    repo2.clear()
    forward = Article(start, repo=repo1)
    backward = Article(end, op=op_backlinks, repo=repo2)
    
    while not matched(forward, backward):    
        if forward.size() > backward.size():
            print("loading backward .... ")
            backward.next()
            print("backward : " + str(backward.size()))
        else:
            print("loading forward .... ")
            forward.next()
            print("forward : " + str(forward.size()))

# used in test cases.
def search_path_between_articles(article1, article2):
    while not matched(article1, article2):    
        if article1.size() > article2.size():
            print("loading backward .... ")
            article2.next()
            print("backward : " + str(article2.size()))
        else:
            print("loading forward .... ")
            article1.next()
            print("forward : " + str(article1.size()))
        
if __name__ == "__main__":
    #search_path("Web Bot", "Barack Obama")
    #print(wiki.page("Tax History").title)
    #print(wikipedia.page("Tax    history").title)
    #taxpage = wiki.page("Tax holiday")
    #print(taxpage.title)
    #links = taxpage.links 
    #print(links)
    #print(taxpage.backlinks)
    web_bot = wikipedia.page("Web Bot").title
    barack_obama = wikipedia.page("Barack Obama").title
    tax_holiday = wikipedia.page("Tax holiday").title
    tax_credit = wikipedia.page("Tax Credit").title
    
    from datetime import datetime
    time1 = datetime.now()
    
    search_path(web_bot, tax_holiday)
    #cached_search_path(web_bot, tax_holiday)
    
    #search_path("Web Bot", "Tax History")
    #search_path("Web Bot", "Tax History")
    
    time2  = datetime.now()
    duration = time2 - time1
    print("Total Time in seconds: " + str(duration.total_seconds()))    
