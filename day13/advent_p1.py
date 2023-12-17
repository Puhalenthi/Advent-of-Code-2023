def getHorizontalMirror(block): # Finds a reflection across a row of a block (return None if doesnt exist)
    for i in range(len(block) - 1):
        bad = False
        if block[i] == block[i + 1]:
            j = i
            while j >= 0 and j < len(block) - 2:
                if block[j] != block[len(block)-j]:
                    bad = True
                    j = 0
                j -= 1
            if bad:
                continue
            return i + 1
    return None

def getVerticalMirror(block):
    for i in range(len(block[0]) - 1):
        bad = False
        if [row[i] for row in block] == [row[i + 1] for row in block]:
            j = i
            while j > 0 and j < len(block[0]) - 1:
                if [row[j] for row in block] != [row[len(block[0])-j] for row in block]:
                    bad = True
                    j = 0
                j -= 1
            if bad:
                continue
            return i + 1
    return None


with open('C:\BCA ATCS\Competitions\AdventOfCode\Advent-of-Code-2023\day13\input.txt', 'r') as f:
    lines = f.readlines()
    blocks = []
    tempBlock = []
    for line in lines:
        if line == '\n':
            blocks.append(tempBlock)
            tempBlock = []
        else:
            tempBlock.append(line.strip())
    blocks.append(tempBlock)
    
    print(getHorizontalMirror(blocks[1]))
    print(getVerticalMirror(blocks[1]))

    
    # totalSum = 0
    # for block in blocks:
    #     if getHorizontalMirror(block) != None:
    #         totalSum += getHorizontalMirror(block) * 100
    #     elif getVerticalMirror(block) != None:
    #         totalSum += getVerticalMirror(block)
    # print("Answer:  " + str(totalSum))