# Part 1
with open("input.txt", "r") as f:
    games = f.readlines()
    idTotal = 0

    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    for game in games:
        values = game.split(" ")
        bad = False
        for i in range(2, len(values)-1, 2):
            if values[i+1][0:-1] == "red":
                if (int(values[i]) > MAX_RED):
                    bad = True
                    break
            elif values[i+1][0:-1] == "green":
                if (int(values[i]) > MAX_GREEN):
                    bad = True
                    break
            elif values[i+1][0:-1] == "blue":
                if (int(values[i]) > MAX_BLUE):
                    bad = True
                    break
        
        if not bad:
            id = int(values[1][0:-1])
            idTotal += id
    
    print(idTotal)


# Part 2
with open("input.txt", "r") as f:
    games = f.readlines()
    total = 0

    for game in games:
        values = game.split(" ")
        bad = False
        maxRed = 0
        maxGreen = 0
        maxBlue = 0
        for i in range(2, len(values)-1, 2):
            if values[i+1][0:-1] == "red" or values[i+1] == "red":
                maxRed = int(values[i]) if int(values[i]) > maxRed else maxRed
            elif values[i+1][0:-1] == "green" or values[i+1] == "green":
                maxGreen = int(values[i]) if int(values[i]) > maxGreen else maxGreen
            elif values[i+1][0:-1] == "blue" or values[i+1] == "blue":
                maxBlue = int(values[i]) if int(values[i]) > maxBlue else maxBlue
        total += maxRed * maxGreen * maxBlue
    
    print(total)