with open('input.txt', 'r') as f:
    lines = f.readlines()
    nodes = {}
    path = ''
    for line in lines: # Put all the data into a dictionary
        if (line == lines[0]):
            path = line.rstrip('\n')
        elif (line == '\n'):
            pass
        else:
            line = line.rstrip('\n')
            data = line.split(" = ")
            ways = data[1].split(',')
            nodes[data[0]] = (ways[0][1:], ways[1][1:-1])
    
    currNode = 'AAA'
    i = 0
    steps = 0
    while currNode != 'ZZZ':
        if i == len(path):
            i = 0
        if path[i] == 'R':
            currNode = nodes[currNode][1]
        else:
            currNode = nodes[currNode][0]
        i += 1
        steps += 1
    
    print(steps)