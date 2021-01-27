#!/usr/bin/python
from bs4 import BeautifulSoup
import urllib2
import csv
import codecs

linksList = []

#f = csv.writer(open("worksURI.csv", "w"))
#f.writerow(["Name", "Link"])
f = codecs.open("alllinkstrial.txt", encoding='utf-8', mode='w+')
#'http://www.isfdb.org/cgi-bin/ea.cgi?12578 ',

target_url=['http://www.isfdb.org/cgi-bin/ea.cgi?48861']

    
for thing in target_url:
    code = urllib2.urlopen(thing)

    soup = BeautifulSoup(code.read())


#this finds all html tags with <a> and a href value, so all the links.
    for link in soup.find_all('a', href=True):

        names = link.contents[0]
        fullLink = link.attrs['href']
#this sets the links as rows and writes them to the text file
        row=names+","+fullLink+"\n"
        f.write(row)
        
