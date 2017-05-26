import csv, re

repo_names = open("./random_repos.csv", "rb")
write_to = open("./ios.txt", "w")
repo_iter = csv.reader(repo_names)


repo_iter.next();		#Skips header

try : 
	while True :
		name = repo_iter.next()[0];
		#print name;
		search_object = re.search(r'.*/.*ios.*', name, re.I)
		if search_object :
			write_to.write(name + "\t -- " + "ios\n")

except StopIteration :
	print "Done"
	repo_names.close()
	write_to.close()
