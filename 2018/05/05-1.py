sourceFile = open("source.txt","r")
#polymer = "dabAcCaCBAcCcaDA"
polymer = sourceFile.readlines()[0]

polymer = polymer.replace("\n","").replace(" ","")
print len(polymer)

done = False
cleanedIndex = 0

while done == False and len(polymer) < 200000:
    polymerRange = range(cleanedIndex,len(polymer))
    for characterIndex in polymerRange:
        character = polymer[characterIndex]
        nextLetterIndex = characterIndex + 1

        if (nextLetterIndex in polymerRange):
            nextLetter = polymer[nextLetterIndex]
        else:
            done = True
            break
        
        if character.capitalize() == nextLetter.capitalize() and character != nextLetter:
            print "current Length: " + str(len(polymer))
            part0 = polymer[:characterIndex]
            part1 = polymer[nextLetterIndex +1:]
            polymer = part0 + part1
            cleanedIndex = characterIndex -1
            if (cleanedIndex < 0):
                cleanedIndex = 0
            break

print "Final Polymer length: " + str(len(polymer))
