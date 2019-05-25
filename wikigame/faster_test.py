#!/usr/bin/env python3

'''
Created on May 22, 2019

Prepared for Stratifyd

Wikipedia game python code

See readme.txt

@author: bill
'''
from datetime import datetime
import unittest

import wikipedia

from wikigame.cachedict import DataDict as DiskDict
from wikigame.faster_game import Folder, op_backlinks, search_path


class Test(unittest.TestCase):

    def setUp(self):
        pass
 
    def test_random_pages(self):
        print("------ random pages test ------------")
        pages = wikipedia.random(2)
        print(pages)
        
        article1 = Folder(pages[0], repo=dict())
        article2 = Folder(pages[1], op=op_backlinks, repo=dict())
        run_test(article1, article2)
        print('=========================================')
    
    def test_tax_holiday(self):
        print("------ tax holiday test ------------")
        web_bot = find_real_title("Web Bot")
        tax_holiday = find_real_title("Tax holiday")
        
        article1 = Folder(web_bot, repo=dict())
        article2 = Folder(tax_holiday, op=op_backlinks, repo=dict())
        run_test(article1, article2)
        print('=========================================')
    
    def test_disk_cached(self):
        print("------ disk cached tax holiday test ------------")
        web_bot = find_real_title("Web Bot")
        tax_holiday = find_real_title("Tax Holiday")
        
        disk1 = DiskDict('web_bot')
        disk2 = DiskDict('tax_holiday')
        disk1.clear()
        disk2.clear()
        
        article1 = Folder(web_bot, repo=disk1)
        article2 = Folder(tax_holiday, op=op_backlinks, repo=disk2)
        run_test(article1, article2)
        print('=========================================')

    def test_impeachment(self):
        print("------ Impeachment test ------------")
        impeachment = find_real_title("Impeachment")
        tower = find_real_title("Trump Tower")
        
        article1 = Folder(impeachment, repo=dict())
        article2 = Folder(tower, op=op_backlinks, repo=dict())
        run_test(article1, article2)
        print('=========================================')

def find_real_title(title):
    try:
        x = wikipedia.page(title, auto_suggest=False).title
    except:
        x = wikipedia.page(title).title
        
    return x

def run_test(article1, article2):
    time1 = datetime.now()
    search_path(article1, article2)
    time2  = datetime.now()
    duration = time2 - time1
    print("Total Time in seconds: " + str(duration.total_seconds()))    
        

 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()