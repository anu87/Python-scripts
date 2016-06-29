# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 14:20:59 2016

@author: Bhuti
"""
# Reddit Scrapper - DailyProgrammer subreddit

import re
import sys
try:
    from urllib.request import urlopen, Request
except ImportError: # this is included for python2 - it gives import error on the first cmd - and when that happens this lines tells the program to perform operation below
    from urllib2 import urlopen

target_url = 'https://www.reddit.com/r/dailyprogrammer/'
# we need to pretend we are a website otherwise reddit blocks the request
# assuming that we are a bot trying to take its server down
# user agent is required to do this
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
hdrs = {'User-Agent': user_agent} # headers
req = Request(target_url, headers=hdrs)

result = urlopen(req)
code = result.getcode()
if code != 200:
    print("Error! Code:", code)
    sys.exit(1) # 1 used for unix based OS - mac  exit with error; 0 - means exit without error

# import pdb; pdb.set_trace() # Debugger    
data = result.read().decode('utf-8')
matches = re.findall(r'<a[^>]*?>[^<]*?\[Easy][^<]*<\/a>',data) # 
# html for < - start, a - start of any html code, [easy or any other word] - the phrase you are interested in -> followed by * to indicate to include evrything that follows that phrase
for m in matches: # using this instead of just print(matches) gives you cleaner easier to read output - goes through matches and prints them one by one
    print(m)

