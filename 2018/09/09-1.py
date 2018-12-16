import time
###############
useTestData = False
###############

# TestData
players = 30
highestMarble = 5807

if not useTestData:
    players = 464
    highestMarble = 70918

circle = [0]
playerScores = [0] * players
marbleToPlace = 1
currentMarble = 0
currentPlayer = 1

def GetVisibleCircle():
    visibleCircle = ""
    for marble in circle:
        if circle.index(marble) != currentMarble:
            visibleCircle += str(marble) + "\t"
        else:
            visibleCircle += "(" + str(marble) + ")" + "\t"
    return visibleCircle

def nextRound():
    global marbleToPlace, currentPlayer
    #print "P" + str(currentPlayer) + " " + GetVisibleCircle()
    marbleToPlace +=1
    if currentPlayer < players:
        currentPlayer += 1
    else:
        currentPlayer = 1

def getClockwiseFromPosition(clockwiseAmount, relatedPosition):
    calculatedPosition = relatedPosition + clockwiseAmount
    highestCircleIndex = len(circle) -1
    circleRange = range(len(circle))

    if relatedPosition not in circleRange:
        print "ERROR: relatedPosition " + str(relatedPosition) + " not in CircleRange " + str(circleRange)
        return None

    if calculatedPosition in circleRange:
        return calculatedPosition
    elif calculatedPosition > highestCircleIndex:
        return calculatedPosition % len(circle)
    elif calculatedPosition < 0:
        while calculatedPosition < 0:
            calculatedPosition += len(circle)
        return calculatedPosition

def getClockwiseFromCurrentMarble(clockwiseAmount):
    return getClockwiseFromPosition(clockwiseAmount, currentMarble)

def placeMarbleAtPosition(positionToPlace, marble):
    highestCircleIndex = len(circle) -1
    circleRange = range(len(circle))

    global currentMarble
    if positionToPlace in circleRange:
        if positionToPlace <= currentMarble:
            currentMarble += 1
        circle.insert(positionToPlace, marble)
    else:
        print "ERROR: Marble could not be placed outside the Circle."
        # TODO Make possible to place at every given position

#####

if highestMarble > 75000:
    print "Warning: This will take long!"

startTime = time.clock()
while marbleToPlace <= highestMarble:
    #print "marbleToPlace: " + str(marbleToPlace)
    if marbleToPlace % 23 != 0:
        newMarblePosition = getClockwiseFromCurrentMarble(2)
        placeMarbleAtPosition(newMarblePosition, marbleToPlace)
        currentMarble = circle.index(marbleToPlace)
    else:
        marble7CounterClockwise = getClockwiseFromCurrentMarble(-7)
        playerScores[currentPlayer -1] += marbleToPlace + circle[marble7CounterClockwise]
        circle.pop(marble7CounterClockwise)
        currentMarble = marble7CounterClockwise
    nextRound()
endTime = time.clock()

timeSpend = endTime - startTime
print "calculation took " + str(int(timeSpend / 60)) + " Minutes and " + str(timeSpend % 60) + " seconds"

highestScore = 0
for score in playerScores:
    if score > highestScore:
        highestScore = score

print "The winners Score is " + str(highestScore)
