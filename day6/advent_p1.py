with open ("input.txt", "r") as f:
    lines = f.readlines()
    data = lines[0].split()
    times = []
    total = 1
    for x in range(1, len(data)):
        times.append(int(data[x]))
    data = lines[1].split()
    distances = []
    for x in range(1, len(data)):
        distances.append(int(data[x]))
    
    for i in range(len(times)):
        possibleTimes = 0
        if times[i] % 2 == 0:
            chargeTime = times[i] // 2
            runTime = times[i] // 2
            while (chargeTime * runTime > distances[i]):
                possibleTimes += 1
                chargeTime -= 1
                runTime += 1
            possibleTimes *= 2
            possibleTimes -=1 
        else:
            chargeTime = times[i] // 2
            runTime = times[i] - chargeTime
            while (chargeTime * runTime > distances[i]):
                possibleTimes += 1
                chargeTime -= 1
                runTime += 1
            possibleTimes *= 2
        total *= possibleTimes
    print(total)