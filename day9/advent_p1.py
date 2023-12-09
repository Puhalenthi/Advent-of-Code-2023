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
    
    for i in range(len(fullArr)): # Finds the next number of each sequence
        fullArr[i][-1].append(0)
        for j in range(len(fullArr[i])-2, -1, -1):
            fullArr[i][j].append(fullArr[i][j][-1] + fullArr[i][j+1][-1])

    total = 0 # This will calculate the final total value
    for i in range(len(fullArr)):
        total += fullArr[i][0][-1]

    print(total)