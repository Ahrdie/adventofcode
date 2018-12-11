sourceFile = open("source.txt","r")
#sourceFile = open("testData.txt","r")
instructionLines = sourceFile.readlines()

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
conditions = []

for instruction in instructionLines:
    newCondition = [instruction[5], instruction[36]]
    conditions.append(newCondition)
print conditions

lettersToRemove = []
for letter in alphabet:
    letterInConditions = False
    for condition in conditions:
        if condition[1] == letter or condition[0] == letter:
            letterInConditions = True
            break
    if not letterInConditions:
        lettersToRemove.append(letter)
lettersToRemove = reversed(lettersToRemove)
for letter in lettersToRemove:
    alphabet.pop(alphabet.index(letter))

print alphabet
correctOrder = ""
letterIndex = 0

while len(conditions) > 0:
    letter = alphabet[letterIndex]
    letterIndex += 1
    print "Trying Letter " + letter + " " + str(conditions)
    otherStepRequired = False

    # Check if other Step is required to do the letter step
    for condition in conditions:
        if letter == condition[1]:
            otherStepRequired = True
            break

    if not otherStepRequired and letter not in correctOrder:
        # Appending Letter to correctOrder
        correctOrder += letter
        print letter + " -> " + str(correctOrder)
        indicesToRemove = []

        # Get indices of conditions, that now fulfill
        for conditionIndex in range(0,len(conditions)):
            if letter == conditions[conditionIndex][0]:
                indicesToRemove.append(conditionIndex)

        indicesToRemove = list(reversed(indicesToRemove))
        print "indicesToRemove:" + str(indicesToRemove)

        # remove fulfilled conditions
        for index in indicesToRemove:
            print conditions[index]
            conditions.pop(index)
        letterIndex = 0

        # remove letter from shortendAlphabet
        indexOfLetter = alphabet.index(letter)
        alphabet.pop(indexOfLetter)

correctOrder += alphabet[0]
print(str(correctOrder) + " Rest: " + str(conditions))
