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