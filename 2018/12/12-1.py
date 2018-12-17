sourceFile = open("source.txt","r")
#sourceFile = open("testData.txt", "r")
dataLines = sourceFile.readlines()

potState = []
boolRange = [None,None]
paddingLeft = 0
rules = [[[[[0,0] for r in boolRange] for r in boolRange] for r in boolRange] for r in boolRange]

line0 = dataLines.pop(0)
rubbish, stateLine = line0.split(": ")
dataLines.pop(0)

for symbol in range(len(stateLine)):
    if stateLine[symbol] == ".":
        potState.append(0)
    elif stateLine[symbol] == "#":
        potState.append(1)

for line in dataLines:
    condition, result = line.split(" => ")
    accessRules = []
    for symbol in condition:
        if symbol == "#":
            accessRules.append(1)
        elif symbol == ".":
            accessRules.append(0)

    if result[0] == "#":
        accessRules.append(1)
    else:
        accessRules.append(0)
    rules[accessRules[0]][accessRules[1]][accessRules[2]][accessRules[3]][accessRules[4]] = accessRules[5]

def insertEmptyPots(amountOfPots):
    for pot in range(0,amountOfPots):
        potState.insert(0,0)

def clipZeros(arrayToClip):
    global paddingLeft
    while True:
        if arrayToClip[0] == 1:
            break
        else:
            arrayToClip.pop(0)
            paddingLeft -= 1

    while True:
        highestIndex = len(arrayToClip) -1
        if arrayToClip[highestIndex] == 1:
            break
        else:
            arrayToClip.pop(highestIndex)
    return arrayToClip

def getNewGeneration():
    global potState
    global paddingLeft

    newGeneration = [0 for pot in range(len(potState)+10)]

    previousLength = len(potState)
    potState = [0 for pot in range(4)] + potState
    paddingLeft += len(potState) - previousLength
    potState += [0 for pot in range(4)]

    for potIndex in range(2,len(potState) -3):
        newGeneration[potIndex] = rules[potState[potIndex -2]][potState[potIndex -1]][potState[potIndex]][potState[potIndex +1]][potState[potIndex +2]]

    newGeneration = clipZeros(newGeneration)
    return newGeneration

for generation in range(20):
    potState = getNewGeneration()

count = 0
for pot in range(len(potState)):
    if potState[pot] == 1:
        count += pot -paddingLeft

print str(count)
