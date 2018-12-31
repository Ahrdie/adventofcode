recepies = [3,7]
recepiesToSearch = [8,4,6,6,0,1]
#recepiesToSearch = [1,2,4]
first = 0
second = 1
searchedFound = False
positionInSearch = 0

def increaseElfPointer(previousValue):
    elfValue = previousValue + recepies[previousValue] +1

    while elfValue > len(recepies) -1:
        elfValue = elfValue - len(recepies)
    return elfValue

def iterate():
    global first
    global second
    global recepies

    result = recepies[first] + recepies[second]
    resultRecepies = []
    if result >= 10:
        resultString = str(result)
        resultRecepies.append(int(resultString[:1]))
        resultRecepies.append(int(resultString[1:]))
    else:
        resultRecepies.append(result)
    recepies = recepies + resultRecepies

    first = increaseElfPointer(first)
    second = increaseElfPointer(second)
    return resultRecepies

def getTenAfterPosition(position):
    tenToReturn = []
    if position != None:
        if position + 10 <= len(recepies):
            while len(tenToReturn) < 10:
                tenToReturn.append(recepies[position])
                position += 1
    else:
        return None
    return tenToReturn

def searchForRecepies(newRecepies):
    global positionInSearch
    global searchedFound
    if positionInSearch +1 < len(recepiesToSearch):
        for result in resultRecepies:
            if result == recepiesToSearch[positionInSearch]:
                positionInSearch += 1
            else:
                positionInSearch = 0
        return None
    else:
        searchedFound = True
        print "Found at" + str(len(recepies) -len(recepiesToSearch))
        return len(recepies) -len(recepiesToSearch)

#recepiesToSearch = list(reversed(recepiesToSearch))

# i = 0
# while not recepiesFound:
#     print str(i) + "\tf: " + str(first) + "\ts: " + str(second) + "\t" + str(recepies)
#     iterate()
#     i = i+1



searchedPosition = None
for i in range(10000000):
    resultRecepies = iterate()
    if not searchedFound:
        searchedPosition = searchForRecepies(resultRecepies)
        print str(i)
    else:
        break

if searchedFound:
    for i in range(10):
        iterate()
    print getTenAfterPosition(searchedPosition + len(recepiesToSearch))
else:
    print "Searched could not be found."


print "#######################\n"
