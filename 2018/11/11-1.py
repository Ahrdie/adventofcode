serialNumber = 5535
gridSize = 300
grid = [[None for y in range(gridSize)] for x in range(gridSize)]

def calculatePowerLevel(x,y):
    rackID = x + 10
    powerLevel =  ( rackID * y ) + serialNumber
    powerLevel *= rackID
    powerLevel = powerLevel // 10**2  %10
    powerLevel -= 5
    return powerLevel

for y in range(gridSize):
    for x in range(gridSize):
        grid[x][y] = calculatePowerLevel(x,y)

biggestTotalPower = 0
biggestPowerPosition = []

for y in range(gridSize -2):
    for x in range(gridSize -2):
        totalPower = 0
        for xAdd in range(3):
            for yAdd in range(3):
                newX = x + xAdd
                newY = y + yAdd

                power = None
                if newX < len(grid) or newY < len(grid[0]):
                    #print str(newX) + " " + str(newY)
                    power = grid[newX][newY]
                else:
                    power = 0
                totalPower += power
        if totalPower > biggestTotalPower:
            biggestTotalPower = totalPower
            biggestPowerPosition = [x, y]

print biggestPowerPosition
