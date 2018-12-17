
sourceFile = open("source.txt","r")
#sourceFile = open("testSource.txt", "r")
dataLines = sourceFile.readlines()

positions = []
velocities = []

for pointData in dataLines :
    rawPosition, rawVelocity, zero = pointData.replace("\n","").split(">")

    x, y = map(int,rawPosition[10:].split(","))
    positions.append([x,y])

    vx,vy = map(int, rawVelocity[11:].split(","))
    velocities.append([vx,vy])

def getExtremePositions():
    extremePositions = [[0, 0],[0, 0]]
    for point in positions :
        # X
        if point[0] < extremePositions[0][0]:
            extremePositions[0][0] = point[0]
        elif point[0] > extremePositions[1][0]:
            extremePositions[1][0] = point[0]
        # Y
        if point[1] < extremePositions[0][1]:
            extremePositions[0][1] = point[1]
        elif point[1] > extremePositions[1][1]:
            extremePositions[1][1] = point[1]
    return extremePositions

def drawSky(border) :
    extremePositions = getExtremePositions()

    xRange = range(extremePositions[0][0] -1 -border,extremePositions[1][0] +border)
    yRange = range(extremePositions[0][1] -1 -border,extremePositions[1][1] +border)
    skyGrid = [["." for y in yRange] for x in xRange]

    for point in positions :
        x = point[0] -1 + border
        y = point[1] -1 + border
        skyGrid[x][y] = "#"

    newLines = []
    for y in yRange :
        newLine = ""
        for x in xRange:
            newLine += skyGrid[x][y]
        newLine += " " + str(len(newLine))
        print newLine

def applyTime(time) :
    for point in range(len(positions)):
        positions[point][0] += velocities[point][0] * time
        positions[point][1] += velocities[point][1] * time

def getExtremeDistance():
    extremePositions = getExtremePositions()
    manhattanDistance = extremePositions[1][0] - extremePositions[0][0] + extremePositions[1][1] - extremePositions[0][1]
    return manhattanDistance

previousDistance = 10000000

# To find the message and correct place in time, start with a big `stepSize` and manualy optimize
# to the minimum distance of extremes.
counter = -1
stepsize = 100
while counter > 0:
    distance = getExtremeDistance()
    print "Distance: " + str(distance) + " Counter: " + str(counter)
    if distance < previousDistance:
        applyTime(stepSize)
        previousDistance = distance
    else:
        break
    counter -= 1

applyTime(10641)
drawSky(0)
