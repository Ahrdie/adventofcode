sourceFile = open("source.txt","r")
sourceChanges = sourceFile.readlines()

sum = 0 
for number in sourceChanges:
	number = number.replace("\n","")
	number = int(number)
	sum = sum + number
	print number
print "sum: " + str(sum)
