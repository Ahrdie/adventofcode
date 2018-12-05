sourceFile = open("source.txt","r")
sourceChanges = sourceFile.readlines()
changes = []
testArray = [[+3,+3,+4,-2,-4],[-6,+3,+8,+5,-6],[+7,+7,-2,-7,-4]]
usedFrequencies = [0]

def loadFromSourceFile():
    source = []
    for i in sourceChanges:
        number = i.replace("\n","")
        number = int(number)
        source.append(number)
    return source

#changes = testArray[2]
changes = loadFromSourceFile()

found = False
while found == False:
    for i in changes:
        newFrequency = usedFrequencies[len(usedFrequencies) -1] + i
        if newFrequency in usedFrequencies:
            print "Double Frequency: " + str(newFrequency)
            found = True
            break
        usedFrequencies.append(newFrequency)
