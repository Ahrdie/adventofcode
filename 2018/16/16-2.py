# Every sample has data in the order: [before, operation, after]
samples = []
currentSample = []
register = [0,0,0,0]
instructions = []

def readSamples():
    sourceFile = open("samples.txt", "r")
    samplesRaw = sourceFile.readlines()
    global currentSample, samples
    for rawSample in samplesRaw:
        if 'Before' in rawSample:
            before = rawSample.split(", ")
            before[0] = before[0][9:]
            before[3] = before[3][:1]
            currentSample.append(list(map(int, before)))
        elif 'After' in rawSample:
            after = rawSample.split(", ")
            after[0] = after[0][9:]
            after[3] = after[3][:1]
            currentSample.append(list(map(int,after)))
            samples.append(currentSample)
            currentSample = []
        elif len(rawSample) > 2:
            currentSample.append(list(map(int, rawSample.split(" "))))

def readInstructions():
    sourceFile = open("opcodes.txt", "r")
    instructionLines = sourceFile.readlines()
    for line in instructionLines:
        instructions.append(list(map(int,line.split(" "))))

def addr(inRegA, inRegB, outReg):
    register[outReg] = register[inRegA] + register[inRegB]

def addi(inRegA, inValB, outReg):
    register[outReg] = register[inRegA] + inValB

def mulr(inRegA, inRegB, outReg):
    register[outReg] = register[inRegA] * register[inRegB]

def muli(inRegA, inValB, outReg):
    register[outReg] = register[inRegA] * inValB

def banr(inRegA, inRegB, outReg):
    register[outReg] = register[inRegA] & register[inRegB]

def bani(inRegA, inValB, outReg):
    register[outReg] = register[inRegA] & inValB

def borr(inRegA, inRegB, outReg):
    register[outReg] = register[inRegA] | register[inRegB]

def bori(inRegA, inValB, outReg):
    register[outReg] = register[inRegA] | inValB

def setr(inRegA, ignored, outReg):
    register[outReg] = register[inRegA]

def seti(inValA, ignored, outReg):
    register[outReg] = inValA

def gtir(inValA, inRegB, outReg):
    if inValA > register[inRegB]:
        register[outReg] = 1
    else:
        register[outReg] = 0

def gtri(inRegA, inValB, outReg):
    if register[inRegA] > inValB:
        register[outReg] = 1
    else:
        register[outReg] = 0

def gtrr(inRegA, inRegB, outReg):
    if register[inRegA] > register[inRegB]:
        register[outReg] = 1
    else:
        register[outReg] = 0

def eqir(inValA, inRegB, outReg):
    if inValA == register[inRegB]:
        register[outReg] = 1
    else:
        register[outReg] = 0

def eqri(inRegA, inValB, outReg):
    if register[inRegA] == inValB:
        register[outReg] = 1
    else:
        register[outReg] = 0

def eqrr(inRegA, inRegB, outReg):
    if register[inRegA] == register[inRegB]:
        register[outReg] = 1
    else:
        register[outReg] = 0

operators = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
oplookup = [operators] * 16

def opsetToString(opset):
    line = ""
    for op in opset:
        line += op.__name__ + ", "
    return line

def tellopcodes():
    for opline in oplookup:
        line = str(oplookup.index(opline)) + ": "
        line += opsetToString(opline)
        print(line)

def assignOpCodesFound():
    global register
    for sample in samples:
        #print("Sample " + str(samples.index(sample)) + ": + str(sample))
        opcodesFound = set()

        for operator in operators:
            register = sample[0].copy()
            operator(sample[1][1], sample[1][2], sample[1][3])
            if register == sample[2]:
                opcodesFound.add(operator)

        #print("Vorher: " + opsetToString(oplookup[sample[1][0]]))
        #print("Found: " + opsetToString(opcodesFound))
        oplookup[sample[1][0]] = set(oplookup[sample[1][0]]).intersection(opcodesFound)
        #print("Nachher: " + opsetToString(oplookup[sample[1][0]]) + "\n")

def evaluateFoundAssignments():
    for i in range(15):
        for keyline in oplookup:
            if len(keyline) == 1:
                for keyToClean in oplookup:
                    if keyToClean != keyline:
                        #print(opsetToString(keyToClean) + " & " + opsetToString(keyline))
                        oplookup[oplookup.index(keyToClean)] -= keyline

def executeTestProgram():
    for instruction in instructions:
        #print(instruction)
        operateInstruction = list(oplookup[instruction[0]])[0]
        operateInstruction(instruction[1],instruction[2], instruction[3])

readSamples()
assignOpCodesFound()
evaluateFoundAssignments()
readInstructions()

tellopcodes()
register = [0,0,0,0]
executeTestProgram()
print(register)

