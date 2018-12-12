sourceFile = open("source.txt","r")
#treeInstructions = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
treeInstructions = list(map(int,sourceFile.readlines()[0].replace("\n","").split(" ")))

class Node:

    def __init__(self, instructions):
        numberOfChildren = instructions[0]
        numberOfMetadata = instructions[1]
        instructions = instructions[2:]

        self.parent = None
        self.metaData = []
        self.children = []

        if numberOfChildren == 0:
            endOfData = len(instructions) - numberOfMetadata
            self.readMetadata(instructions, numberOfMetadata)
            self.lengthOfChildren = 0
        else:
            self.lengthOfChildren = 0
            rangeOfChildren = range(0,numberOfChildren)

            for child in rangeOfChildren:
                childNode = Node(instructions[self.lengthOfChildren:])
                if childNode.lengthOfChildren == 0:
                    self.lengthOfChildren += 2 + len(childNode.metaData)
                else:
                    self.lengthOfChildren += childNode.getOwnLengthWithChildren()

                childNode.parent = self
                self.children.append(childNode)

            self.readMetadata(instructions[self.lengthOfChildren:], numberOfMetadata)

    def getOwnLengthWithChildren(self):
        self.ownLength = 0
        for child in self.children:
            self.ownLength += child.getOwnLengthWithChildren()
        self.ownLength += len(self.metaData) + 2
        return self.ownLength

    def readMetadata(self, instructions, size):
        metaDataRange = range(0, size)
        for dataIndex in metaDataRange:
            self.metaData.append(instructions[dataIndex])

sumOfMetadata = 0

def sumUpMetadata(node):
    global sumOfMetadata
    for dataPoint in node.metaData:
        sumOfMetadata += dataPoint
    for child in node.children:
        sumUpMetadata(child)
    return sumOfMetadata

tree = Node(treeInstructions)
sum = sumUpMetadata(tree)

print "Sum of all Metadata: " + str(sum)
