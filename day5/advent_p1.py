def checkIfSeedInRange(seed, destStart, sourceStart, rangeLength):
    if (sourceStart <= seed and seed <= sourceStart + rangeLength): # If the seed is in the range
        return (seed - sourceStart) + destStart
    else:
        return -1


with open("input.txt", "r") as f:
    data = f.readlines()

    seeds = []
    NUMBER_OF_SEEDS = 20
    successfullyConvertedSeeds = [False] * NUMBER_OF_SEEDS

    for i in range(0, len(data)):
        data[i] = data[i].rstrip("\n")
        info = data[i].split(" ")
        if (info[0] == "seeds:"):
            for j in range(1, NUMBER_OF_SEEDS + 1):
                seeds.append(int(info[j]))
        elif (info[0] == ""):
            successfullyConvertedSeeds = [False] * NUMBER_OF_SEEDS
        elif (info[0][0].isdigit()):
            for j in range(NUMBER_OF_SEEDS):
                if successfullyConvertedSeeds[j]:
                    continue
                else:
                    if checkIfSeedInRange(seeds[j], int(info[0]), int(info[1]), int(info[2])) == -1:
                        pass
                    else:
                        successfullyConvertedSeeds[j] = True
                        seeds[j] = checkIfSeedInRange(seeds[j], int(info[0]), int(info[1]), int(info[2]))
                    
    
                
    print(min(seeds))