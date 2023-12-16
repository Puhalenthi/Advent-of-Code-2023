from collections import deque

def solve(useStack = True):
    with open('input.txt', 'r') as f:
        data = f.readlines()
        lines = [line.strip() for line in data]
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
        maxFound = 0
        startings = []
        for i in range(MAX_ROW):
            startings.append([(i, 0), RIGHT])
            startings.append([(i, MAX_COL), LEFT])
        for i in range(MAX_COL):
            startings.append([(0, i), DOWN])
            startings.append([(MAX_ROW, i), UP])
        
        while len(startings) != 0:
            energized = []
            visited = []
            if useStack:
                ds = [startings.pop()]
            else:
                ds = deque(startings.pop())
            
            while len(ds) != 0:
                if useStack:
                    item = ds.pop()
                else:
                    item = ds.popleft()
                if item in visited:
                    continue
                x, y = item[0]
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
            print(len(energized))
            maxFound = max(maxFound, len(energized))
        print("\nMAX:" + str(maxFound))

solve(useStack=True)