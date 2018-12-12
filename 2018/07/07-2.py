##################
useTestData = False
##################

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

if not useTestData:
    numberOfWorkers = 5
    fixTimeForEachTask = 60
    sourceFile = open("source.txt","r")
else:
    numberOfWorkers = 2
    fixTimeForEachTask = 0
    sourceFile = open("testData.txt","r")
    alphabet = ["A","B","C","D","E","F"]

conditions = []

instructionLines = sourceFile.readlines()
for instruction in instructionLines:
    newCondition = [instruction[5], instruction[36]]
    conditions.append(newCondition)

avaliableLetters = list(alphabet)

print "\n"

workers = [[None, 0] for x in range(numberOfWorkers)]
time = -1

def allWorkersIdle():
    allIdle = True
    for worker in workers:
        if worker[0] != None:
            allIdle = False
    return allIdle

def WorkerStatus():
    statusText = ""
    for worker in workers:
        workerIndex = workers.index(worker)
        letter = "."
        if worker[0] != None:
            letter = worker[0]
        statusText += letter

        if workerIndex != len(workers) -1:
            statusText += "  "
    return statusText

while not allWorkersIdle() or time == -1:
    print str(time) + "\t" + WorkerStatus()
    for worker in workers:
        if worker[1] > 0:
            worker[1] = worker[1] -1
        else:
            if worker[1] == 0:
                indicesToRemove = []
                for conditionIndex in range(0,len(conditions)):
                    if worker[0] == conditions[conditionIndex][0]:
                        indicesToRemove.append(conditionIndex)

                indicesToRemove = list(reversed(indicesToRemove))

                # remove fulfilled conditions
                for index in indicesToRemove:
                    conditions.pop(index)

                worker[0] = None

    for worker in workers:
        if worker[1] == 0:
            for letter in avaliableLetters:
                letterPossible = True
                for condition in conditions:
                    if letter == condition[1]:
                        letterPossible = False
                if letterPossible:
                    worker[0] = letter
                    avaliableLetters.pop(avaliableLetters.index(worker[0]))

                    timeNeeded = fixTimeForEachTask + alphabet.index(letter)
                    worker[1] = timeNeeded
                    break

    time = time + 1

print "\n============\nTotal Time: " + str(time) + "\n"
