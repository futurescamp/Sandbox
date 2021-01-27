#Find all in the nav div and replace all the ul tags with paragraph tags
#Get the contents of the ul tags
#then loop within that and pull out the data
#then loop within that and parse the info

#seperate functions
#make each one and test them

from bs4 import BeautifulSoup
import urllib2
import codecs
import csv
import re

f = codecs.open("biblio_all.txt", encoding='utf-8', mode='w+')

target_url=['http://www.isfdb.org/cgi-bin/title.cgi?14252']

for thing in target_url:
    code = urllib2.urlopen(thing)
    
    soup = BeautifulSoup(code.read())
    for link in soup.find_all('div', {"id": "main"}): 
        plink=link.find('p', {"dir": "ltr"})
#   The author's name is stored in the first 'a' link after the beginning of
#the div 
        author=link.a.contents[0]
        authorlink=link.a.attrs['href']
#        print(plink.nextSibling)
#This is wrong, but it still works? next sibling is the unordered list after publications
      #  pubs=plink.next_element.next_element.next_element.next_element.next_element
        pubs=plink.next_sibling
        print(pubs)
#find all the li tags, which have the info on each publication
        
        for info in pubs.find_all('li'):
   #         print(info.a.contents)
  #          print(info.contents)
            title=info.a.contents[0]
#the first 'a' tag has the title info
            titlelink=info.a.attrs['href']
#this gets the link for the title
            #these parse other bits of info about the books
            tu=info.a
            pubdate=tu.next_element.next_element
#this finds the publisher and link
            pub=info.find(href=re.compile("publisher"))
            pubname=pub.string
            publink=pub.attrs['href']
            numbers=info.find('span', {"dir": "ltr"})
#            isbn=number.contents[0]
#            print(number)
            number=str(numbers)
            row=author+","+authorlink+","+title+","+titlelink+","+pubdate+","+pubname+","+publink+","+number+"\n"
            f.write(row)
