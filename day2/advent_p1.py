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
                bad = True if (int(values[i]) > MAX_RED) else False
                break
            elif values[i+1][0:-1] == "green":
                bad = True if (int(values[i]) > MAX_GREEN) else False
                break
            elif values[i+1][0:-1] == "blue":
                bad = True if (int(values[i]) > MAX_BLUE) else False
                break
        if not bad:
            id = int(values[1][0:-1])
            idTotal += id
    
    print(idTotal)