#!/usr/bin/env python3

'''
Created on May 22, 2019

Prepared for Stratifyd

Wikipedia game python code

See readme.txt

@author: bill
'''
from diskcache import Cache


# just simple extension of Disk Cache.
class DataDict(Cache):
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
    
    def keys(self):
        return [k for k in self.iterkeys()]
        
        
