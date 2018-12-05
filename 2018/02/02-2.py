sourceFile = open("source.txt","r")
sourceIDs = sourceFile.readlines()
ids = []

def loadFromSourceFile():
    source = []
    for id in sourceIDs:
        correctedID = id.replace("\n","")
        source.append(correctedID)
    return source

ids = loadFromSourceFile()

for id in ids:
    for otherId in ids:
        if id != otherId:
            differentSymbols = 0
            index = 0
            while index < len(id):
                if id[index] != otherId[index]:
                    differentSymbols = differentSymbols +1
                index = index +1
            if differentSymbols == 1:
                print str(id) + " ~ " + str(otherId)
