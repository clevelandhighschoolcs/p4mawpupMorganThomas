# Web-Scraper

Tests whether a website has changed

In order for this to run, you need the Python library Beautiful Soup 4 (bs4)

This program needs 2 arguments to run, an adress and a number of seconds to check for (this isn't going to be perfectly exact)

An example comand is <C:/path>scraper.py https://fidosodd.github.io 20

Known issues: if you have no arguments it will crash. It will, however succesfully in form you that you did not put in the right amount of arguments if you have one argument or three or more. If you put in an unopenable address, it will crash. However, if you put in a non intager value for the second argument it will inform you thus.

If you put in a negative value for seconds, it will stop imediatley. 

It will tell you the title of the website you searched.

It will clear your command line before running and only fills a couple lines. No mess!

