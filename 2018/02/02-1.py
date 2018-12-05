sourceFile = open("source.txt","r")
sourceIDs = sourceFile.readlines()
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
ids = []
exactlyTwo = 0
exactlyThree = 0

def loadFromSourceFile():
    source = []
    for id in sourceIDs:
        correctedID = id.replace("\n","")
        source.append(correctedID)
    return source

ids = loadFromSourceFile()

for id in ids:
    twoCounted = False
    threeCounted = False
    for letter in alphabet:
        countOfLetter = id.count(letter)
        if countOfLetter == 2 and twoCounted == False:
            exactlyTwo = exactlyTwo +1
            twoCounted = True
        elif countOfLetter == 3 and threeCounted == False:
            exactlyThree = exactlyThree +1
            threeCounted = True

print exactlyTwo * exactlyThree
