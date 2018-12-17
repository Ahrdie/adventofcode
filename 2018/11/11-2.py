import time
serialNumber = 5535
gridSize = 300
grid = []
summedAreaTable = []

def createPowerGrid(size):
    gridSize = size
    testGrid = [[None for y in range(gridSize)] for x in range(gridSize)]
    for y in range(gridSize):
        for x in range(gridSize):
            testGrid[x][y] = calculatePowerLevel(x+1,y+1)
    return testGrid

def visualizeGrid(gridToVisualize) :
    print "\n"
    for y in range(len(gridToVisualize)):
        newLine = str(y) + " |\t"
        for x in range(len(gridToVisualize[0])):
            newLine += str(gridToVisualize[x][y]) + "\t"
        print newLine + "\n"

def calculatePowerLevel(x,y):
    rackID = x + 10
    powerLevel =  ( rackID * y ) + serialNumber
    powerLevel *= rackID
    powerLevel = powerLevel // 10**2  %10
    powerLevel -= 5
    return powerLevel

def createSummedAreaTable() :
    summedAreaTable = [[None for y in range(gridSize)] for x in range(gridSize)]
    for y in range(gridSize):
        #print "Calculating Row: " + str(y)
        for x in range(gridSize):
            summedAreaTable[x][y] = calculateSquarePower(x,y,1,summedAreaTable)

    print "Finished creating summedAreaTable.\n"
    return summedAreaTable

def calculateSquarePower(x,y,size, lookUpTable):
    lowerRightCorner = [x + size -1, y + size -1]

    if x > 0:
        leftRect = lookUpTable[x-1][lowerRightCorner[1]]
    else:
        leftRect = 0
        smallRect = 0

    if y > 0:
        topRect = lookUpTable[lowerRightCorner[0]][y -1]
    else:
        topRect = 0
        smallRect = 0

    if x > 0 and y > 0:
        smallRect = lookUpTable[x-1][y-1]

    squarePower = None
    bigRect = lookUpTable[lowerRightCorner[0]][lowerRightCorner[1]]

    if bigRect == None:
        bigRect = grid[x][y]
        squarePower = bigRect + leftRect + topRect - smallRect
    else:
        squarePower = smallRect + bigRect - leftRect - topRect

    #if (abs(squarePower) < 1000):
        #print str(x) + "|" + str(y) + " BigR: " + str(bigRect) + "\tsmallR: " + str(smallRect) + "\tleftR: " + str(leftRect) + "\ttopR: " + str(topRect) + "\t\tCell: " + str(grid[x][y]) + "\t\t\t= " + str(squarePower)
    return squarePower

biggestTotalPower = 0
biggestPowerPosition = []
biggestSquareSize = None

def searchForBiggestPowerSquare():
    global biggestTotalPower
    global biggestPowerPosition
    global biggestSquareSize

    for squareSize in range(1,gridSize):
        print "Checking SquareSize " + str(squareSize)
        for y in range(gridSize -squareSize):
            for x in range(gridSize -squareSize):

                squareSum = calculateSquarePower(x,y,squareSize, summedAreaTable)
                if squareSum > biggestTotalPower:
                    biggestTotalPower = squareSum
                    biggestPowerPosition = [x+1,y+1]
                    biggestSquareSize = squareSize

#gridSize = 5
grid = createPowerGrid(gridSize)
#visualizeGrid(grid)
summedAreaTable = createSummedAreaTable()
#visualizeGrid(summedAreaTable)
#createPowerGrid()
#createSummedAreaTable()
searchForBiggestPowerSquare()
print str(biggestPowerPosition) + " " + str(biggestSquareSize)
