# Web-Scraper
*For Windows 10*

## Instructions:

  1. Download and extract the files
  
  2. Make sure Python version 2.7.X is installed
  
It should be a system variable. If you don't know how to do that follow this link: https://www.youtube.com/watch?v=Y2q_b4ugPWk
  
  3. Make sure the Python library Beautiful Soup 4 (bs4) is installed
  
(If you have pip you can use 'pip install bs4')
  
  4. Open your command prompt and navigate to the folder containing scraper.py
  
  5. Type scraper.py followed by the url you want to moniter and an amount of seconds to moniter for.
  
An example comand is <C:/path>scraper.py https://fidosodd.github.io 20

  6. Press eneter

## Info:

Tests whether a website has changed

This program needs 2 arguments to run, an adress and a number of seconds to check for (this isn't going to be perfectly exact)

Known issues: if you have no arguments it will crash. It will, however succesfully in form you that you did not put in the right amount of arguments if you have one argument or three or more. If you put in an unopenable address, it will crash. However, if you put in a non intager value for the second argument it will inform you thus.

If you put in a negative value for seconds, it will stop imediatley. 

It will tell you the title of the website you searched.

It will clear your command line before running and only fills a couple lines. No mess!

## Flowchart:

Note: flowchart may not represent the most recent version of the file.

![flowchart](https://raw.githubusercontent.com/clevelandhighschoolcs/p4mawpup-MorganThomas/master/Flowchart.png)
