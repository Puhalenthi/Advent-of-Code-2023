def checkIfSeedInRange(seed, destStart, sourceStart, rangeLength):
    if (sourceStart <= seed and seed <= sourceStart + rangeLength): # If the seed is in the range
        return (seed - sourceStart) + destStart
    else:
        return -1

with open("input.txt", "r") as f:
    data = f.readlines()

    seeds = []
    totSeeds = 0
    temp = data[0].split()
    for i in range(1, len(temp), 2):
        seeds.append((int(temp[i]), int(temp[i]) + int(temp[i + 1])))

    mappingRanges = []
    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")
        info = data[i].split(" ")
        if info[0] == "":
            temp = []
            while len(seeds) > 0:
                startS, endS = seeds.pop()
                for startM, endM, lengthM in mappingRanges:
                    intersectingStart = max(startS, endM)
                    instersectingEnd = min(endS, endM + lengthM)
                    if intersectingStart < instersectingEnd:
                        temp.append((intersectingStart - endM + startM, instersectingEnd - endM + startM))
                        if intersectingStart > startS:
                            seeds.append((startS, intersectingStart))
                        if endS > instersectingEnd:
                            seeds.append((instersectingEnd, endS))
                        break
                else:
                    temp.append((startS, endS))
            seeds = temp
            mappingRanges = []         
        elif info[0].isdigit():
            mappingRanges.append((int(info[0]), int(info[1]), int(info[2])))
    
    print(seeds)
    print(min(seeds))