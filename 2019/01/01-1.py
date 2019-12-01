source = open("input.txt", "r")
sum = 0

for line in source.readlines():
    sum += int(line) // 3 -2

print(sum)