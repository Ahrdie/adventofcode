source = open("input.txt", "r")
positions = [int(i) for i in source.readline().split(",")]
pointers = range(0,len(positions), 4)

def add(positionA, positionB, targetPosition):
    #print("Changing [" + str(targetPosition) + "] to " + str(positions[positionA] + positions[positionB]))
    positions[targetPosition] = positions[positionA] + positions[positionB]

def multiply(positionA, positionB, targetPosition):
    #if targetPosition == 0:
    #    print("Changing [0] to " + str(positions[positionA] * positions[positionB]))
    positions[targetPosition] = positions[positionA] * positions[positionB]

positions[1] = 12
positions[2] = 2

for pointer in pointers:
    opcode = positions[pointer]
    #print("Pointer: " + str(pointer) + "\topcode: " + str(opcode))
    #print(positions)
    
    if opcode == 1:
        #print("Adding")
        add(positions[pointer +1], positions[pointer +2], positions[pointer +3])
    elif opcode == 2:
        #print("Multi")
        multiply(positions[pointer +1], positions[pointer +2], positions[pointer +3])
    elif opcode == 99:
        print("End reached")
        break
    else:
        print("Unknown opcode: " + str(opcode))

print("Position 0: " + str(positions[0]))