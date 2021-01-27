#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2
import codecs
import csv
import re

#this defines some tags we will use later to only scrape from the part of the page with the publication info
def pub_tag(tag):
    return ('p', {"dir": "ltr"})
def pub_info(tag):
    return ('li')


f = codecs.open("biblio_all_real.txt", encoding='utf-8', mode='w+')
# Lists all the urls, actual list much longer
target_url=[
'http://www.isfdb.org/cgi-bin/title.cgi?605617'
]
for thing in target_url:
    code = urllib2.urlopen(thing)
    
    soup = BeautifulSoup(code.read())
    for link in soup.find_all('div', {"id": "main"}): 
#   The author's name is stored in the first 'a' link after the beginning of
#the div 
        author=link.a.contents[0]
        authorlink=link.a.attrs['href']

#find all the li tags, which have the info on each publication
        
        for bib in link.find_all(pub_tag):
            for info in bib.find_all(pub_info):
                try:
                    print(info)
  
                    title=info.a.contents[0]
#the first 'a' tag has the title info
                    titlelink=info.a.attrs['href']
#this gets the link for the title
            #these parse other bits of info about the books
                    tu=info.a
                    pubdate=tu.next_element.next_element
#this finds the publisher and link
                    pub=info.find(href=re.compile("publisher"))
                    print(pub)
                    pubname=pub.string
                    publink=pub.attrs['href']
                    numbers=info.find('span', {"dir": "ltr"})
#   this finds the ISBN number and then converts it into a string
                    number=str(numbers)
                    row=author+","+authorlink+","+title+","+titlelink+","+pubdate+","+pubname+","+publink+","+number+"\n"
                    f.write(row)
  # this writes everything as a row (that can be read as a csv unless there is an error, then it passes                  
                except:
                    pass
