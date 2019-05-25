'''
Created on May 24, 2019

@author: bill
'''
import wikipediaapi
wiki = wikipediaapi.Wikipedia('en')
import copy

op_backlinks = lambda page: page.backlinks
op_links = lambda page: page.links

class Folder(object):
    def __init__(self, title, op=op_links, repo=dict()):
        self._title_ = title
        self.data = repo
        self.data[self._title_] = [self._title_]
        self.op = op

    def match(self, keys):
        return set(self.data.keys()) & keys
        
    def size(self):
        return len(self.data)
        
    def loads(self):
        keys = set(self.data.keys())
        for k in keys:
            links = [t for t in self.op(wiki.page(k))]
            for t in links:
                if self.data.get(t) == None:
                    path = copy.copy(self.data[k])
                    path.append(t)
                    self.data[t] = path
                
            yield links
            
    def path(self, key):
        return self.data[key]
        
def search_path(forward, backward):
    done = False;    
    
    while not done:
        # load child links from smaller side
        (s, l) = (forward, backward) if forward.size() < backward.size() else (backward, forward)    
        for links in s.loads():
            # compare one by one instead.
            m = l.match(set(links))
                
            # found the match, so print out the result and stop.    
            if len(m)>0:
                k = m.pop()
                b = copy.copy(backward.path(k))
                b.reverse()
                print(" ->".join(forward.path(k)[:-1] + b))
                done = True
                break
            

if __name__ == '__main__':
    import wikipedia
    import sys

    if len(sys.argv) != 3:
        print('Usage: python3 faster_game.py "start_article" "end_article"!')
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
        

    # print out the original inputs and what we got to run with corrected titles.
    print("Original From [" + start + "] to [" + end + "]")
    print("Found and Run From [" + title1 + "] to [" + title2 + "]")

    forward = Folder(title1, repo=dict())
    backward = Folder(title2, op=op_backlinks, repo=dict())
    
    from datetime import datetime
    
    time1 = datetime.now()
    
    search_path(forward, backward)
    
    time2  = datetime.now()
    duration = time2 - time1
    
    print("Total Time Used in seconds: " + str(duration.total_seconds()))    
    
    
    