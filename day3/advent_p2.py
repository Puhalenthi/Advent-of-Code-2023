import pprint
with open("input.txt", "r") as f:
    lines = f.readlines()
    starGears = {} # Dictionary that holds the number that are next to stars {star_coord: [num1...]}
    currNum = ""
    starFound = ()
    for l in range(len(lines)):
        for i in range(len(lines[l])):
            try:
                if lines[l][i].isdigit():
                    if (l > 0 and lines[l-1][i] == "*"): # up
                        starFound = (l-1, i)
                    if (i > 0 and lines[l][i-1] == "*"): # left
                        starFound = (l, i-1)
                    if (l < len(lines)-1 and lines[l+1][i] == "*"): #down
                        starFound = (l+1, i)
                    if (i < len(lines[l])-1 and lines[l][i+1] == "*"): # right
                        starFound = (l, i+1)
                    if (l > 0 and i > 0 and lines[l-1][i-1] == "*"): # up left
                        starFound = (l-1, i-1)
                    if (l < len(lines)-1 and i > 0 and lines[l+1][i-1] == "*"): # down left
                        starFound = (l+1, i-1)
                    if (l > 0 and i < len(lines[l])-1 and lines[l-1][i+1] == "*"): # up right
                        starFound = (l-1, i+1)
                    if (l < len(lines)-1 and i < len(lines[l])-1 and lines[l+1][i+1] == "*"): # down right
                        starFound = (l+1, i+1)
                    currNum += lines[l][i]
                else:
                    if starFound != ():
                        if starFound not in starGears:
                            starGears[starFound] = [currNum]
                        else:
                            starGears[starFound].append(currNum)
                    currNum = ""
                    starFound = ()
                    
            except:
                pass
    total = 0
    for star in starGears:
        starTotal = 1
        if (len(starGears[star]) == 2): # If there are two numbers next to a star
            for num in starGears[star]:
                starTotal *= int(num)
            total += starTotal
    
    print(total)