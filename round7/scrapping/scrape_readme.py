import urllib
import re, csv
from bs4 import BeautifulSoup

write_to = open("./scraped5.txt", "w")
repo_names = open("./5.csv", "rb")
errors = open("./errors5.txt", "w")

repo_iter = csv.reader(repo_names)
#repo_iter.next();		#Skips header

try :
	while True :
		name = repo_iter.next()[0];

		url = "https://github.com/" + name
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, "html.parser")

		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out

		# get text
		text = soup.get_text()

		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = '\n'.join(chunk for chunk in chunks if chunk)

		text = text.encode('utf-8')
		#print text

		parts = text.split("README.md")
		#print parts[2]
		print "...   "
		write_to.write("-->" + name + "\n")

		try:
			needed_text = parts[2].split("\n")
		
			for i in range(0,10) :
				write_to.write(needed_text[i])
			write_to.write("\n\n")	

		except IndexError:
			errors.write(name + "\n")

except StopIteration :
	print "Done"
	repo_names.close()	
	write_to.close()
	errors.close()
