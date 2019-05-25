Purpose:
  The project is prepared by Bill Tsay for demonstrating the implementation of The Wikipedia game

Environment:
  ubuntu 18.04
  python 3.6.7 which comes with ubuntu
  eclipse with pydev plugin for python development
  
Setup:
  $ sudo apt-get install python3-pip
  $ pip3 install wikipedia     (https://pypi.org/project/wikipedia/)
  $ pip3 install wikipedia-api (https://github.com/martin-majlis/Wikipedia-API)
  $ pip3 install diskcache     (https://pypi.org/project/diskcache/)
  
Approaches:
  1. Considering degree of heavy connected graph should be small - https://en.wikipedia.org/wiki/Wikipedia:Six_degrees_of_Wikipedia
  2. Bidirectional search with Breadth-first -- https://pdfs.semanticscholar.org/6516/c3f2d5c7a33440bccfc45d988c3088e2d2ba.pdf
  3. The package wikipedia has nice figure to locate wikipages and present the proper titles. (better than wikipedia-api)
  4. Disk caches the data in case when the search goes wild and need big amount of space. The package diskcache seems very good.
  5. Wiki articles match should consider English language such as 'This is a book' matches '   this    is   a  BOOK' 
     since we are comparing wiki page titles. wikipath.title_match does that.
  6. Find the shortest path and print it out. Any shortest path, so every time may get a different result if the path length is the same.
  
Updated Approaches:
  7. The wikigame.faster_game.py does the links comparison before loading more. Unlike the wikigame.wikipath.py that loads all children links before doing comparison.  

Run from console:
  ~/python_projects$ export PYTHONPATH=.:$PYTHONPATH
  ~/python_projects$ python3 wikigame/wikipedia_game.py
  Usage: python3 wikipedia_game.py "start_article" "end_article"!

  ~/python_projects$ python3 wikigame/wikipedia_game.py "Web Bot" "Tax Holiday"

  Original From [Web Bot] to [Tax Holiday]
  Found and Run From [Web Bot] to [Tax holiday]
  loading forward .... 
  forward : 32
  loading backward .... 
  backward : 296
  loading forward .... 
  forward : 13139
  Web Bot -> Pacific Northwest -> Taxation in Canada -> Tax holiday
  Total Time Used in seconds: 16.400381
  
Tests:
  $ python3 wikigame/faster_test.py

	------ disk cached tax holiday test ------------
	Web Bot ->Iran ->Taxation in Iran ->Tax holiday
	Total Time in seconds: 41.411679
	=========================================
	------ Impeachment test ------------
	.Impeachment ->President of Pakistan ->Nawaz Sharif ->Trump Tower
	Total Time in seconds: 4.306113
	=========================================
	.------ random pages test ------------
	['Leonów, Lublin Voivodeship', 'Voluntary taxation']
	Leonów, Lublin Voivodeship ->Poland ->Economy of India ->Tax ->Voluntary taxation
	Total Time in seconds: 11.128884
	=========================================
	.------ tax holiday test ------------
	Web Bot ->Iran ->Taxation in Iran ->Tax holiday
	Total Time in seconds: 6.393393
	=========================================
	.
	----------------------------------------------------------------------
	Ran 4 tests in 68.829s
	
	OK

  $ python3 wikigame/test.py

	Finding files... done.
	Importing test modules ... done.
	
	------ disk cached tax holiday test ------------
	loading forward .... 
	forward : 32
	loading backward .... 
	backward : 296
	loading forward .... 
	forward : 13139
	Web Bot -> Pacific Northwest -> Taxation in Canada -> Tax holiday
	Total Time in seconds: 62.488488
	=========================================
	------ Impeachment test ------------
	loading forward .... 
	forward : 293
	loading backward .... 
	backward : 623
	loading forward .... 
	forward : 70360
	Impeachment -> Bill Clinton -> 2016 United States presidential debates -> Trump Tower
	Total Time in seconds: 189.442386
	=========================================
	------ random pages test ------------
	['Giləparqo', 'Neglected Aspects of Sufi Study']
	loading forward .... 
	forward : 111
	loading backward .... 
	backward : 13
	loading backward .... 
	backward : 399
	loading forward .... 
	forward : 2135
	Giləparqo -> Azerbaijan -> Mysticism -> Idries Shah -> Neglected Aspects of Sufi Study
	Total Time in seconds: 41.948322
	=========================================
	------ tax holiday test ------------
	loading forward .... 
	forward : 32
	loading backward .... 
	backward : 296
	loading forward .... 
	forward : 13139
	Web Bot -> Iran -> Taxation in Iran -> Tax holiday
	Total Time in seconds: 22.031348
	=========================================
	----------------------------------------------------------------------
	Ran 4 tests in 322.150s
	OK


To Do:
	1. consider to do multithreading on big amount of keys matching.
	2. map/reduce in clustered environment.  

       
  
