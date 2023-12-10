with open('input.txt', 'r') as f:
    maze = f.read().split('\n')
    UP, DOWN, RIGHT, LEFT = (-1, 0), (1, 0), (0, 1), (0, -1)
    MOVEMENTS = {
        '|': (UP, DOWN),
        '-': (LEFT, RIGHT),
        '7': (LEFT, DOWN),
        'J': (LEFT, UP),
        'L': (UP, RIGHT),
        'F': (RIGHT, DOWN),
        '.': (),
        'S': (),
    }
    x, y = None, None
    for i in range(len(maze)): # Finding the starting position
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                x, y = i, j
                break
    
    queue = [] # This uses a BFS (Breadth First Search) algorithm to find the paths
    visited = {(x, y)} # This stores the visited nodes
    if UP in MOVEMENTS[maze[x + 1][y]]: # These will add the pipes around the starting position to the queue
        queue.append(((x + 1, y), 1))
        visited.add((x + 1, y))
    if DOWN in MOVEMENTS[maze[x - 1][y]]:
        queue.append(((x - 1, y), 1))
        visited.add((x - 1, y))
    if RIGHT in MOVEMENTS[maze[x][y - 1]]:
        queue.append(((x, y - 1), 1))
        visited.add((x, y - 1))
    if LEFT in MOVEMENTS[maze[x][y + 1]]:
        queue.append(((x, y + 1), 1))
        visited.add((x, y + 1))
    
    while queue:
        (x, y), cost = queue.pop(0)
        for directions in MOVEMENTS[maze[x][y]]:
            next = (x + directions[0], y + directions[1])
            if next not in visited: # If a pipe hasn't been visited yet, it will be added to the queue with the relative cost
                queue.append((next, cost + 1))
                visited.add(next)
    print(cost)