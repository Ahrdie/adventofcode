sourceFile = open("source.txt","r")
#polymer = "dabAcCaCBAcCcaDA"
polymer = sourceFile.readlines()[0]

polymer = polymer.replace("\n","").replace(" ","")
print len(polymer)
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
reducedSizes = []

def reducePolymer(inputPolymer):
    done = False
    cleanedIndex = 0
    reactingPolymer = inputPolymer

    while done == False and len(reactingPolymer) < 200000:
        polymerRange = range(cleanedIndex,len(reactingPolymer))
        for characterIndex in polymerRange:
            character = reactingPolymer[characterIndex]
            nextLetterIndex = characterIndex + 1

            if (nextLetterIndex in polymerRange):
                nextLetter = reactingPolymer[nextLetterIndex]
            else:
                done = True
                break
            
            if character.capitalize() == nextLetter.capitalize() and character != nextLetter:
                #print "current Length: " + str(len(reactingPolymer))
                part0 = reactingPolymer[:characterIndex]
                part1 = reactingPolymer[nextLetterIndex +1:]
                reactingPolymer = part0 + part1
                cleanedIndex = characterIndex -1
                if (cleanedIndex < 0):
                    cleanedIndex = 0
                break
    return len(reactingPolymer)

for letter in alphabet:
    print "removing " + letter + ".\n testing..."
    shortendPolymer = polymer.replace(letter, "").replace(letter.capitalize(), "")
    size = reducePolymer(shortendPolymer)
    print "Reacted Size: " + str(size)
    reducedSizes.append(size)

print "Letter to remove for shortest polymer:" + str(alphabet[reducedSizes.index(min(reducedSizes))])
