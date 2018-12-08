import copy

sourceFile = open("source.txt","r")
vectorLines = sourceFile.readlines()
testVectors = [[1,1],[1,6],[8,3],[3,4],[5,5],[8,9]]

vectors = []
for line in vectorLines:
    x, y = line.replace("\n","").split(",")
    vectors.append([int(x),int(y)])

#vectors = list(testVectors)

print("\n\n")

def GetAmountOfNearestPoints(extend):
    width = 0
    height = 0

    extendedVectors = copy.deepcopy(vectors)
    doubleExtend = 2 * extend

    for vector in extendedVectors:

        if vector[0] > width:
            width = vector[0] + doubleExtend

        if vector[1] > height:
            height = vector[1] + doubleExtend

        vector[0] = vector[0] + extend
        vector[1] = vector[1] + extend

    amountOfNearestPoints = {}

    for x in range(0, width):
        for y in range(0, height):
            closestDistance = width + height
            nearestVector = 0
            for vector in extendedVectors:
                horizontalDistance = abs(x - vector[0])
                verticalDistance = abs(y - vector[1])
                distance = horizontalDistance + verticalDistance
                if distance < closestDistance:
                    nearestVector = extendedVectors.index(vector)
                    closestDistance = distance
                elif distance == closestDistance:
                    nearestVector = None
            if nearestVector != None:
                if nearestVector in amountOfNearestPoints:
                    amountOfNearestPoints.update({nearestVector: amountOfNearestPoints[nearestVector] +1})
                else:
                    amountOfNearestPoints[nearestVector] = 1
    return amountOfNearestPoints


extendedDistances = GetAmountOfNearestPoints(1)
normalDistances = GetAmountOfNearestPoints(0)

biggestArea = 0
for vector in extendedDistances:
    if extendedDistances[vector] == normalDistances[vector]:
        if extendedDistances[vector] > biggestArea:
            biggestArea = extendedDistances[vector]

print("Biggest Area: " + str(biggestArea) + "\n")
