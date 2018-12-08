sourceFile = open("source.txt","r")
vectorLines = sourceFile.readlines()
testVectors = [[1,1],[1,6],[8,3],[3,4],[5,5],[8,9]]

vectors = []
for line in vectorLines:
    x, y = line.replace("\n","").split(",")
    vectors.append([int(x),int(y)])

#vectors = list(testVectors)

print("\n\n")

maximumCombinedDistance = 10000

def GetAmountOfBestPoints():
    width = 0
    height = 0

    amountOfBestPoints = 0
    for vector in vectors:

        if vector[0] > width:
            width = vector[0]

        if vector[1] > height:
            height = vector[1]

    for x in range(0, width):
        for y in range(0, height):
            sumOfDistances = 0
            for vector in vectors:
                horizontalDistance = abs(x - vector[0])
                verticalDistance = abs(y - vector[1])
                distance = horizontalDistance + verticalDistance
                sumOfDistances = sumOfDistances + distance
                if sumOfDistances > maximumCombinedDistance:
                    break;
            if sumOfDistances < maximumCombinedDistance:
                amountOfBestPoints = amountOfBestPoints +1
    return amountOfBestPoints

print("Central Points: " + str(GetAmountOfBestPoints()) + "\n")
