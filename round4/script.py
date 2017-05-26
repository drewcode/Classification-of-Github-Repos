from __future__ import division
import csv

file1  = open("./results.csv", "rb")
file11  = open("./results.csv", "rb")
file2  = open("./pairs.csv", "rb")
f = open('./values.csv','w')

allrepos1 = csv.reader(file1)
allrepos2 = csv.reader(file11)
pairs = csv.reader(file2)

#for row in reader:
#	print row[0].replace(" ", "") + " " +row[1]

pairs.next()
row = pairs.next()
repo1 = row[0] 
repo2 = row[1] 
num = int(row[2])

#print repo1 + " " + repo2 + " " + count
try:
	while True:
		print repo1
		repo1 = row[0]
		temp1 = allrepos1.next()
		while repo1 != temp1[0].replace(" ", "") :
			temp1 = allrepos1.next()
		denom1 = int(temp1[1])
		##print "yolla"
		while row[0] == repo1 :
			#print repo2
			temp2 = allrepos2.next()
			
			while(repo2 != temp2[0].replace(" ", "")) :
				temp2 = allrepos2.next()
			denom2 = int(temp2[1])

			value = num / (denom1 + denom2)
			f.write(repo1 + ", " + repo2 + ", " + str(value) + "\n")

			row = pairs.next() 
			repo2 = row[1] 
			num = int(row[2])
			##print row[0]
			##print "***"
			##print row[1]

		file11.seek(0)
		#allrepos2 = csv.reader(file11)	
		##print "these happened"
		
except StopIteration:
	print "its in the exception block !"
	pass


file1.close()
file11.close()
file2.close()
f.close()
