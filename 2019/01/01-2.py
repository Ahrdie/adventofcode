source = open("input.txt", "r")
total = 0

def calculateWeight( weight ):
    fuel = calculateFuel(weight)
    if fuel > 0:
        sum = fuel + calculateWeight(fuel)
        return sum
    else:
        return max(0, fuel)


def calculateFuel ( weight ):
    return weight // 3 -2

for line in source.readlines():
    total += calculateWeight(int(line))

print(total)