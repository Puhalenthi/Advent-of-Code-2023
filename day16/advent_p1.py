import sys, time
from collections import deque
def visualize(energized, lines):
    idek = ''
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if (i, j) in energized:
                idek += '🟩'
            else:
                idek += '🟥'
        idek += '\n'
    print(idek)
    
    time.sleep(0.01) 
    sys.stdout.write("\r")

def solve(useStack = True):
    with open('input.txt', 'r') as f:
        data = f.readlines()
        lines = [line.strip() for line in data]
        energized = []
        MAX_ROW = len(lines) - 1
        MAX_COL = len(lines[0]) - 1
        UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
        MOVEMENTS = {
            '.' : ((UP, [UP]), (RIGHT, [RIGHT]), (DOWN, [DOWN]), (LEFT, [LEFT])),
            '\\' : ((UP, [LEFT]), (RIGHT, [DOWN]), (DOWN, [RIGHT]), (LEFT, [UP])),
            '/' : ((UP, [RIGHT]), (RIGHT, [UP]), (DOWN, [LEFT]), (LEFT, [DOWN])),
            '-' : ((UP, [LEFT, RIGHT]), (RIGHT, [RIGHT]), (DOWN, [LEFT, RIGHT]), (LEFT, [LEFT])),
            '|' : ((UP, [UP]), (RIGHT, [UP, DOWN]), (DOWN, [DOWN]), (LEFT, [UP, DOWN]))
        }
        visited = []
        if useStack:
            ds = [((0, 0), RIGHT)]
        else:
            ds = deque([((0, 0), RIGHT)])
        
        while len(ds) != 0:
            if useStack:
                item = ds.pop()
            else:
                item = ds.popleft()
            if item in visited: # 
                continue
            x, y = item[0] # Get the coordinates
            direction = item[1]
            char = lines[x][y]
            for possibleMovements in MOVEMENTS[char]:
                if direction == possibleMovements[0]:
                    for newdirection in possibleMovements[1]:
                        if not (x + newdirection[0] > MAX_ROW or x + newdirection[0] < 0 or y + newdirection[1] > MAX_COL or y + newdirection[1] < 0):
                            ds.append(((x + newdirection[0], y + newdirection[1]), newdirection))

            visited.append(item)
            if (x, y) not in energized:
                energized.append(item[0])
            #visualize(energized, lines) # Uncomment this line to see the visualization
        print(len(energized))

solve(useStack=True)