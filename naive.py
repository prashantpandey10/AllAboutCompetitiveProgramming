import urllib2
from bs4 import BeautifulSoup
url="http://theshayna.com/data-structures-and-algorithms-tutorials/"
f=open("out.txt",'w')
page=urllib2.urlopen(url).read()
soup=BeautifulSoup(page,"lxml")
topics=soup.find("div","entry-inner")
#print topics
i=1
for link,urls in zip(topics.findAll("strong"),topics.findAll("ul")):
	print str(i)+"."+link.contents[0].encode('ascii','ignore')
	f.write(str(i)+"."+link.contents[0].encode('ascii','ignore')+"\n")
	for url in urls.findAll("li"):
			if url.findAll("a"):
				f.write(url.a["href"])
				print url.a["href"]
			f.write("\n")
	i+=1
	f.write("\n")
	print 

# Uncomment next three lines to print output of the file in which the links have been stored
#f=open("out.txt","r")
#for lines in f:
#	print lines
