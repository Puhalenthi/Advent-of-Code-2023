with open("input.txt", "r") as f:
    lines = f.readlines()
    currNum = ""
    done = False
    total = 0
    isAddable = False
    for l in range(len(lines)):
        for i in range(len(lines[l])):
            try:
                if lines[l][i].isdigit():
                    currNum += lines[l][i]
                    if (l > 0 and not lines[l-1][i].isdigit() and not lines[l-1][i] == "."): # up
                        isAddable = True
                    elif (i > 0 and not lines[l][i-1].isdigit() and not lines[l][i-1] == "."): # left
                        isAddable = True
                    elif (l < len(lines)-1 and not lines[l+1][i].isdigit() and not lines[l+1][i] == "."): #down
                        isAddable = True
                    elif (i < len(lines[l])-1 and not lines[l][i+1].isdigit() and not lines[l][i+1] == "."): # right
                        isAddable = True
                    elif (l > 0 and i > 0 and not lines[l-1][i-1].isdigit() and not lines[l-1][i-1] == "."): # up left
                        isAddable = True
                    elif (l < len(lines)-1 and i > 0 and not lines[l+1][i-1].isdigit() and not lines[l+1][i-1] == "."): # down left
                        isAddable = True
                    elif (l > 0 and i < len(lines[l])-1 and not lines[l-1][i+1].isdigit() and not lines[l-1][i+1] == "."): # up right
                        isAddable = True
                    elif (l < len(lines)-1 and i < len(lines[l])-1 and not lines[l+1][i+1].isdigit() and not lines[l+1][i+1] == "."): # down right
                        isAddable = True
                    if (i == len(lines[l])-1):
                        total += int(currNum)
                        currNum = ""
                        isAddable = False
                else:
                    if (isAddable):
                        total += int(currNum)
                        isAddable = False
                    currNum = ""
            except:
                pass
    print(total)