import pprint
with open('C:\BCA ATCS\Competitions\AdventOfCode\Advent-of-Code-2023\day9\input.txt', 'r') as f:
    lines = f.readlines()
    fullArr = []
    for line in lines:
        line = line.rstrip('\n')
        tempArr = [[int(x) for x in line.split()]]
        fullArr.append(tempArr)
    
    for i in range(len(fullArr)): # This creates the array of all values and the steps it takes to get to 0
        done = False
        while not done:
            tempArr = []
            for j in range(1, len(fullArr[i][-1])):
                tempArr.append(fullArr[i][-1][j] - fullArr[i][-1][j-1])
            fullArr[i].append(tempArr)
            for x in tempArr:
                if x != 0:
                    break
            else:
                done = True
    
    for i in range(len(fullArr)): # Gets the next values of each of the patterns
        fullArr[i][-1].insert(0, 0)
        for j in range(len(fullArr[i])-2, -1, -1):
            fullArr[i][j].insert(0, fullArr[i][j][0] - fullArr[i][j+1][0])

    total = 0
    for i in range(len(fullArr)):
        total += fullArr[i][0][0]
    
    print(total)