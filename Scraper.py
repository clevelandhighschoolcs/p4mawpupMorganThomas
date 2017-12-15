import urllib2
from bs4 import BeautifulSoup
import sys
import time
site = sys.argv[1]
import os
import requests
from twilio.rest import Client

msg = raw_input("Do you want to get a message of the results?(y/n)  ")
if (msg == "y"):
	twilio = raw_input("Do you have a twilio account?(y/n)  ")
	if (twilio == "y"):
		use = raw_input("Do you want to use your twilio account?(y/n)  ")
		if (use == "y"):
			account_sid = raw_input("What is your account sid?  ")
			auth_token = raw_input("What is your authorization token?  ")
			twilio_phone_number = raw_input("What is your Twilio phone number?  ")
			my_phone_number = raw_input("What is your phone number? (must be registered in twilio)  ")

if len(sys.argv) < 3 or len(sys.argv) > 3:
 addArgu = len(sys.argv) - 1
 addArgustr = str(addArgu)
 print 'This program needs exactly 2 additional arguments, an address and a number of seconds.'+' You have '+addArgustr+'.'
 
 exit()
def getname():
 quote_page = site
 page = urllib2.urlopen(quote_page)
 soup = BeautifulSoup(page, 'html.parser')
 name_box = soup.find('title')
 global name
 name = name_box.text.strip()
 print 'checking "'+name+'" for changes...'
def is_number(s):
 try:
  int(s)
  #return false
 except ValueError:
  print 'The second argument is not an integer.'
  exit()
def main():
 TTimeint = int(sys.argv[2])
 TTimeI = sys.argv[2]
 TTimeIint = int(sys.argv[2])
 getname()
 URL = urllib2.urlopen(site)
 data = URL.read()
 datastring = str(data)
 length1 = len(datastring)
 print 'Working...'
 while TTimeint > 0:
  URL = urllib2.urlopen(site)
  data = URL.read()
  datastring = str(data)
  URL = urllib2.urlopen(site)
  data = URL.read()
  datastring = str(data)
  length2 = len(datastring)
  os.system('cls')
  print 'checking "'+name+'" for changes...'
  print 'Working...'
  print length2
  if length2 != length1:
   difTime = str(TTimeIint - TTimeint+1)
   os.system('cls')
   print 'checking "'+name+'" for changes...'
   print 'Working...'
   print length1
   print length2
   print 'The page has changed after '+difTime+' second(s).'
   if (msg == "y"):
     if (twilio == "y"):
      if (use == "y"):
	      message()
   exit()
  else:
    TTimeint -= 1
    time.sleep(1)
 if TTimeint == 0:
  print 'There was no change in '+TTimeI+' seconds.'
def message():
	tclient = Client(account_sid, auth_token)
	tclient.messages.create(
		body=body,
		to=my_phone_number,
		from_=twilio_phone_number
	)
is_number(sys.argv[2])
main()
