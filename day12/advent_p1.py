import pprint

def checkIfValid(pattern, nums):
    count = 0
    n = 0
    if pattern.count('#') != sum(nums):
        return False
    for i in pattern:
        if i == '#':
            count += 1
        else:
            if count != 0:
                if n > len(nums)-1:
                    return False
                if count != nums[n]:
                    return False
                n += 1
                count = 0
    if (n != len(nums)):
        return False
    return True

with open('C:\BCA ATCS\Competitions\AdventOfCode\Advent-of-Code-2023\day12\input.txt', 'r') as f:
    lines = f.readlines()
    patterns = []
    numbers = []

    for line in lines:
        data = line.rstrip("\n").split(" ")
        patterns.append(data[0])
        tempNums = []
        for i in data[1].split(","):
            tempNums.append(int(i))
        numbers.append(tempNums)
    
    total = 0
    for i in range(len(patterns)):
        # Since every pattern may contain a '?', each '?' can be either a '#' or a '.'. We need to check all permuations of this.
        
        possiblePatterns = []
        # Calculate every possible combination of the pattern
        for j in range(2**patterns[i].count('?')):
            tempPattern = patterns[i]
            for k in range(patterns[i].count('?')):
                if j & (1 << k):
                    tempPattern = tempPattern.replace('?', '#', 1)
                else:
                    tempPattern = tempPattern.replace('?', '.', 1)
            possiblePatterns.append(tempPattern)
        for pp in possiblePatterns:
            if checkIfValid(pp, numbers[i]):
                total += 1
        print("Line:   " + str(i))
    
    print(total + len(patterns))