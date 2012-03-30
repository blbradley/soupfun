'''
Created on Mar 29, 2012

@author: Brandon Bradley
@email:  crixdev@gmail.com
'''

from bs4 import BeautifulSoup
import urllib2
import re
from datetime import datetime
from urlparse import urlparse

pollsite = "http://news.ycombinator.com/item?id=3771286"
options = []
polldata = dict()

#open URL and create soup obj using content
pollsiteobj = urllib2.urlopen(pollsite)
soup = BeautifulSoup(pollsiteobj.read())

#collect simple parameters
poll_id = urlparse(pollsite).query[3:]
title = soup.title.string
timestamp = datetime.now()

#collect required data, lots of work in these statements
choices_tags = soup.table.find_all('td', 'comment')
points_tags = soup.table.find_all('span', 'comhead')

#choices HTML structure was unique
#score text HTML was not, it was very similar to comment header and article score HTML
#but score text tags all at top
#so grab length of choices_tags records from the points tags
for i in range(len(choices_tags)):
  options.append({'choice_text' : choices_tags[i].string,
                'num_points'  : points_tags[i].string})
  
polldata = {'id': poll_id,
            'ts': timestamp,
            'title' : title,
            'options' : options }

print polldata   