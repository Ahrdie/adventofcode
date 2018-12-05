sourceFile = open("source.txt","r")
sourceLines = sourceFile.readlines()
#sourceLines = ["#1 @ 1,3: 4x4","#2 @ 3,1: 4x4","#3 @ 5,5: 2x2"]

def loadFromSourceFile():
    source = []
    for line in sourceLines:
        correctedLine = line.replace("\n","")
        source.append(correctedLine)
    return source

claims = loadFromSourceFile()

width = 1000
height = 1000
fabric = [[0 for y in range(height)] for x in range(width)]

def visualizeFrabric():
    for x in fabric:
        row = ""
        for y in x:
            row = row + str(y) + " "
        print row

for claim in claims:
    id, at, position, size = claim.split(" ")
    xPos, yPos = position.replace(":","").split(",")
    xSize, ySize = size.split("x")
    x = int(xPos)
    while x < int(xPos) + int(xSize):
        y = int(yPos)
        while y < int(yPos) + int(ySize):
            fabric[x][y] = fabric[x][y] +1
            y = y +1
        x = x +1

twoOrMoreClaims = 0
for x in fabric:
    for y in x:
        if y >= 2:
            twoOrMoreClaims = twoOrMoreClaims +1
#visualizeFrabric()
print "Tiles with more than two claims: " + str(twoOrMoreClaims)
