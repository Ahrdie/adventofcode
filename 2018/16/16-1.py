# Every sample has data in the order: [before, operation, after]
samples = []
currentSample = []
register = [3,2,3,4]

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

like3opCodes = 0
def countOpCodesFound():
    for sample in samples:
        print("Sample " + str(sample))
        global like3opCodes, register
        opcodesFound = 0

        # TODO change to CBV instead of CBR
        register = sample[0].copy()
        addr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            print("behaves like addr")
            opcodesFound+=1

        register = sample[0].copy()
        addi(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            print("behaves like addi")
            opcodesFound+=1

        print(sample[0])
        register = sample[0].copy()
        print(register)
        mulr(sample[1][1], sample[1][2], sample[1][3])
        print(register)
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like mulr")
            
        register = sample[0].copy()
        muli(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like muli")
            
        register = sample[0].copy()
        banr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like banr")

        
        register = sample[0].copy()
        bani(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like bani")
        

        register = sample[0].copy()
        borr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like borr")
        
        register = sample[0].copy()
        bori(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like bori")
        
        register = sample[0].copy()
        setr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like setr")
        
        register = sample[0].copy()
        seti(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like seti")
        
        register = sample[0].copy()
        gtri(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like gtri")
        
        register = sample[0].copy()
        gtir(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like gtir")
        
        register = sample[0].copy()
        gtrr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like gtrr")
        
        register = sample[0].copy()
        eqri(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like eqri")
        
        register = sample[0].copy()
        eqir(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like eqir")
        
        register = sample[0].copy()
        eqrr(sample[1][1], sample[1][2], sample[1][3])
        if register == sample[2]:
            opcodesFound+=1
            print("behaves like eqrr")

        # Evaluation
        if opcodesFound >= 3:
            like3opCodes += 1
            print("Behaves like 3 or more opcodes. " + str(like3opCodes))
        print("Found: " + str(opcodesFound) + "\n")

readSamples()
countOpCodesFound()
print("3 or more: " + str(like3opCodes))