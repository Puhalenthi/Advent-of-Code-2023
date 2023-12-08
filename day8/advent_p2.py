import math
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
    
    nodesToIterate = []
    for node in nodes.keys():
        if node.endswith('A'):
            nodesToIterate.append(node)
    
    counts = []
    for i in nodesToIterate:
        count = 0
        j = 0
        currNode = i
        while not currNode.endswith('Z'):
            if j == len(path):
                j = 0
            if path[j] == 'R':
                currNode = nodes[currNode][1]
            else:
                currNode = nodes[currNode][0]
            count += 1
            j += 1
        else:
            counts.append(count)
    print(counts)

    num = 1
    for count in counts:
        num = math.lcm(num, count)
    
    print(num)