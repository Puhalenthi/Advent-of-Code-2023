import pprint, copy, time, os
def findRocks(platform):
    rocks = []
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                rocks.append((i, j))
    return rocks

def movePlatform(DIRECTION, platform, rocks):
    for i, rock in enumerate(rocks):
        if (rock[0] + DIRECTION[0] < 0 or rock[0] + DIRECTION[0] >= len(platform) or rock[1] + DIRECTION[1] < 0 or rock[1] + DIRECTION[1] >= len(platform[0])):
            continue # If the rock is on the edge of the platform, it can't move
        if (platform[rock[0] + DIRECTION[0]][rock[1] + DIRECTION[1]] == '.'):
            platform[rock[0] + DIRECTION[0]][rock[1] + DIRECTION[1]] = 'O' # Moves the rock
            platform[rock[0]][rock[1]] = '.' # Removes the rock from its previous location
            rocks[i] = (rock[0] + DIRECTION[0], rock[1] + DIRECTION[1]) # Updates the rock's location
    return platform, rocks

with open('C:\BCA ATCS\Competitions\AdventOfCode\Advent-of-Code-2023\day14\input.txt', 'r') as f:
    lines = f.readlines()
    platform = []
    UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
    MOVEMENTS = (UP, LEFT, DOWN, RIGHT)
    for line in lines:
        line = line.strip()
        platform.append([*line])
    rocks = findRocks(platform) # Finds the location of all rocks
    
    prevPlatform = []
    cycles = 0
    i = 0
    cyclePrevPlatform = copy.deepcopy(platform)
    while cyclePrevPlatform != platform or cycles < 1000000000:
        prevPlatform = []
        while prevPlatform != platform:
            prevPlatform = copy.deepcopy(platform)
            platform, rocks = movePlatform(MOVEMENTS[cycles % len(MOVEMENTS)], platform, rocks)
        if i == 4:
            if cyclePrevPlatform == platform:
                break
            cyclePrevPlatform = copy.deepcopy(platform)
            i = 0
        cycles += 1
        i += 1
    
    loadSum = 0
    numRows = len(platform)
    for line in platform:
        loadSum += line.count('O') * numRows
        numRows -= 1
    
    print('Answer:  ' + str(loadSum))