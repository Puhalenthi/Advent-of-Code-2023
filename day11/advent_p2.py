with open('C:\BCA ATCS\Competitions\AdventOfCode\Advent-of-Code-2023\day11\input.txt', 'r') as f:
    lines = f.read().split('\n')
    rowsWithoutGalaxies = []
    columnsWithoutGalaxies = []
    GALAXIE_EXPANSION = 999999 # How many rows/columns to add to the grid when there are no galaxies in a row/column
    for i, line in enumerate(lines): # Checks every row
        if '#' not in line:
            rowsWithoutGalaxies.append(i)
    for i in range(len(lines[0])): # Checks every column
        for j in range(len(lines)):
            if lines[j][i] == '#':
                break
            if j == len(lines) - 1:
                columnsWithoutGalaxies.append(i)
    galaxies = []
    for i in range(len(lines)): # Get the positions of all galaxies
        for j in range(len(lines[i])):
            if lines[i][j] == '#':
                galaxies.append((i, j))
    
    # Find the distance between each different pair of galaxies (if the closest path passes through rows and columns without galaxies, then add 1 to the distance)
    totalDistance = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            distance = abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
            for k in range(min(galaxies[i][0], galaxies[j][0]) + 1, max(galaxies[i][0], galaxies[j][0])): # Check if a value in rowsWithoutGalaxies is between the two galaxies' rows
                if k in rowsWithoutGalaxies:
                    distance += GALAXIE_EXPANSION
            for k in range(min(galaxies[i][1], galaxies[j][1]) + 1, max(galaxies[i][1], galaxies[j][1])): # Check if a value in columnsWithoutGalaxies is between the two galaxies' columns
                if k in columnsWithoutGalaxies:
                    distance += GALAXIE_EXPANSION
            totalDistance += distance
    
    print(totalDistance)