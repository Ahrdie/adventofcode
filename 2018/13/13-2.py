import copy

sourceFile = open("source.txt","r")
#sourceFile = open("test.txt", "r")
railSource = sourceFile.readlines()
railPlan = []
cartSymbols = ["^",">","v","<"]
specialTiles = ["/","\\","+"]
crashed = False

for line in railSource:
    line = line.replace("\n","")
    railPlan.append(list(line))

emptyRailPlan = copy.deepcopy(railPlan)
carts = []

class Cart:
    def __init__(self, position):
        self.position = position
        self.turnDirection = 0

    def __str__(self):
        return "Pos: " + str(self.position) + " next turn to " + str(self.turnDirection)

    def bumpTurnDirection(self):
        if self.turnDirection < 2:
            self.turnDirection += 1
        else:
            self.turnDirection = 0

    def getNextTile(self):
        cartTile = railPlan[self.position[1]][self.position[0]]
        if cartTile == cartSymbols[0]:
            return [self.position[0],self.position[1] -1]
        elif cartTile == cartSymbols[1]:
            return [self.position[0] +1,self.position[1]]
        elif cartTile == cartSymbols[2]:
            return [self.position[0],self.position[1] +1]
        elif cartTile == cartSymbols[3]:
            return [self.position[0] -1,self.position[1]]

    def turnSymbol(self, direction):
        currentSymbol = cartSymbols.index(railPlan[self.position[1]][self.position[0]])
        if direction == 0:      # Left
            if currentSymbol != 0:
                return cartSymbols[currentSymbol -1]
            else:
                return "<"
        elif direction == 1:    # Right
            if currentSymbol != 3:
                return cartSymbols[currentSymbol +1]
            else:
                return "^"

    def bumpTurnDirection(self):
        if self.turnDirection == 2:
            self.turnDirection = 0
        else:
            self.turnDirection += 1

    def turnSymbolAtCrossing(self):
        if self.turnDirection == 0:
            self.bumpTurnDirection()
            return self.turnSymbol(0)
        elif self.turnDirection == 1:
            self.bumpTurnDirection()
            return railPlan[self.position[1]][self.position[0]]
        elif self.turnDirection == 2:
            self.bumpTurnDirection()
            return self.turnSymbol(1)

def visualizeMap(map):
    for line in map:
        lineToPrint = ""
        for symbol in line:
            lineToPrint += symbol
        print lineToPrint

def createCarts():
    for line in railPlan:
        for symbolPosition in range(len(line)):
            symbol = line[symbolPosition]
            if symbol in cartSymbols:
                linePosition = railPlan.index(line)
                newCart = Cart([symbolPosition, linePosition])
                carts.append(newCart)
                emptyRailPlan[linePosition][symbolPosition] = " "

def findCartIndex(position):
    for cart in carts:
        if cart.position == position:
            return carts.index(cart)

def driveCart(cartID):
    cartToDrive = carts[cartID]
    global crashed
    nextPosition = cartToDrive.getNextTile()
    currentSymbol = railPlan[cartToDrive.position[1]][cartToDrive.position[0]]
    nextTile = railPlan[nextPosition[1]][nextPosition[0]]
    if nextTile not in cartSymbols:
        if nextTile == specialTiles[0]:     # /
            if currentSymbol in [">","<"]:
                railPlan[nextPosition[1]][nextPosition[0]] = cartToDrive.turnSymbol(0)
            else:
                railPlan[nextPosition[1]][nextPosition[0]] = cartToDrive.turnSymbol(1)
        elif nextTile == specialTiles[1]:   # \
            if currentSymbol in [">","<"]:
                railPlan[nextPosition[1]][nextPosition[0]] = cartToDrive.turnSymbol(1)
            else:
                railPlan[nextPosition[1]][nextPosition[0]] = cartToDrive.turnSymbol(0)
        elif nextTile == specialTiles[2]:   # +
            railPlan[nextPosition[1]][nextPosition[0]] = cartToDrive.turnSymbolAtCrossing()
        else:
            railPlan[nextPosition[1]][nextPosition[0]] = railPlan[cartToDrive.position[1]][cartToDrive.position[0]]

        railPlan[cartToDrive.position[1]][cartToDrive.position[0]] = emptyRailPlan[cartToDrive.position[1]][cartToDrive.position[0]]
        cartToDrive.position = nextPosition
    else:
        print "CRASH at " + str(nextPosition)
        global numberOfCrashes
        numberOfCrashes += 1
        otherCartID = findCartIndex([nextPosition[0],nextPosition[1]])
        railPlan[cartToDrive.position[1]][cartToDrive.position[0]] = emptyRailPlan[cartToDrive.position[1]][cartToDrive.position[0]]
        railPlan[nextPosition[1]][nextPosition[0]] = emptyRailPlan[nextPosition[1]][nextPosition[0]]
        if otherCartID < cartID:
            carts.pop(cartID)
            carts.pop(otherCartID)
        else:
            carts.pop(otherCartID)
            carts.pop(cartID)

def iterate():
    global numberOfCrashes
    numberOfCrashes = 0
    for cartID in range(len(carts)):
        driveCart(cartID -numberOfCrashes *2)


createCarts()

while len(carts) > 1:
    iterate()
    #visualizeMap(railPlan)

print "Location of last cart: " + str(carts[0].position)
