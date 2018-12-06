sourceFile = open("source.txt","r")
testData = open("testdata.txt","r")

allGuardEvents = []

for sourceLine in sourceFile:
    timestamp, message = sourceLine.replace("\n","").split("]")
    
    date, time = timestamp.replace("[","").split(" ")
    year, month, day = date.split("-")
    hour, minute = time.split(":")
    
    newEvent = {
        "year" : int(year),
        "month" : int(month),
        "day" : int(day),
        "hour" : int(hour),
        "minute" : int(minute),
        "message" : message[1:]
    }
    allGuardEvents.append(newEvent)

allGuardEvents = sorted(allGuardEvents, key=lambda k: k["minute"])
allGuardEvents = sorted(allGuardEvents, key=lambda k: k["hour"])
allGuardEvents = sorted(allGuardEvents, key=lambda k: k["day"])
allGuardEvents = sorted(allGuardEvents, key=lambda k: k["month"])
allGuardEvents = sorted(allGuardEvents, key=lambda k: k["year"])

guardTimes = {}
guardId = ""
fellAsleep = 0

for event in allGuardEvents:
    
    if event["message"].find("Guard") == 0:
        g, guardId, b, s = event["message"].split(" ")
    
    elif event["message"].find("falls") == 0:
        fellAsleep = event["minute"]
    
    elif guardId in guardTimes:
        pattern = guardTimes[guardId]
        for m in range(int(fellAsleep),int(event["minute"])):
            pattern[m] = pattern[m] +1
        guardTimes[guardId] = pattern

    else:
        pattern = [0] * 60
        for m in range(int(fellAsleep),int(event["minute"])):
            pattern[m] = pattern[m] +1
        guardTimes[guardId] = pattern

mostFrequentMinute = 0
minuteFrequency = 0
for guard in guardTimes:
    for m in guardTimes[guard]:
        if m > minuteFrequency:
            guardId = guard
            mostFrequentMinute = guardTimes[guard].index(m)
            minuteFrequency = m

print "Elf " + str(guardId) + " sleeps most frequent at minute " + str(mostFrequentMinute) + ". Code: " + str(int(guardId[1:]) * mostFrequentMinute)
