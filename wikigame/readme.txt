Purpose:
  The project is prepared by Bill Tsay for demonstrating the implementation of The Wikipedia game

Environment:
  ubuntu 18.04
  python 3.6.7 which comes with ubuntu
  
Setup:
  $ sudo apt-get install python3-pip
  $ pip3 install wikipedia     (https://pypi.org/project/wikipedia/)
  $ pip3 install wikipedia-api (https://github.com/martin-majlis/Wikipedia-API)
  $ pip3 install diskcache     (https://pypi.org/project/diskcache/)
  
Approaches:
  1. Considering degree of heavy connected graph should be small - https://en.wikipedia.org/wiki/Wikipedia:Six_degrees_of_Wikipedia
  2. Bidirectional search with Breadth-first -- https://pdfs.semanticscholar.org/6516/c3f2d5c7a33440bccfc45d988c3088e2d2ba.pdf
  3. The package wikipedia has nice figure to locate wikipages and present the correct titles. (better than wikipedia-api)
  4. Disk caches the data in case when the search goes wild and need big amount of space. The package diskcache seems very good.
  5. Wiki articles match should consider English language such as 'This is a book' matches '   this    is   a  BOOK' 
     since we are comparing wiki page titles. wikipath.title_match does that.
  6. Find the shortest path and print it out. Any shortest path, so every time may get a different result if the path length is the same.
     
Tests:
  $ python solrup.test.py

	------ disk cached tax holiday test ------------
	loading forward .... 
	forward : 32
	loading backward .... 
	backward : 296
	loading forward .... 
	forward : 13139
	['Web Bot', 'Barack Obama', 'Tax credit', 'Tax holiday']
	Total Time in seconds: 60.792068
	=========================================
	------ Impeachment test ------------
	.loading forward .... 
	forward : 293
	loading backward .... 
	backward : 623
	loading forward .... 
	forward : 70352
	['Impeachment', 'Andrew Johnson', 'Donald Trump', 'Trump Tower']
	Total Time in seconds: 197.832535
	=========================================
	.------ random pages test ------------
	['Meads Cup', 'Worsowut']
	loading forward .... 
	forward : 67
	loading backward .... 
	backward : 4
	loading backward .... 
	backward : 53
	loading backward .... 
	backward : 30946
	loading forward .... 
	forward : 5524
	['Meads Cup', 'New Zealand at the Rugby World Cup', 'Republic of Ireland', 'Economy of Tajikistan', 'List of towns and villages in Tajikistan', 'Worsowut']
	Total Time in seconds: 287.891355
	=========================================
	.------ tax holiday test ------------
	loading forward .... 
	forward : 32
	loading backward .... 
	backward : 296
	loading forward .... 
	forward : 13139
	['Web Bot', 'Barack Obama', 'Tax credit', 'Tax holiday']
	Total Time in seconds: 19.146129
	=========================================
	.
	----------------------------------------------------------------------
	Ran 4 tests in 573.313s
	
	OK

To Do:
	1. consider to do multithreading on big amount of keys matching.
	2. map/reduce in clustered environment.  

       
  
