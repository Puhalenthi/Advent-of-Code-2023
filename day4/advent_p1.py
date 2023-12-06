import pprint
with open("input.txt", "r") as f:
    cards = f.readlines()
    WINNING_NUMBERS_COUNT = (2, 12)
    NUMBERS_TO_CHECK = (13, 38)
    total = 0
    for card in cards:
        cardTotal = 0
        info = card.split()
        winningNumbers = []
        for i in range(WINNING_NUMBERS_COUNT[0], WINNING_NUMBERS_COUNT[1]):
            winningNumbers.append(int(info[i]))
        numbersToCheck = []
        for i in range(NUMBERS_TO_CHECK[0], NUMBERS_TO_CHECK[1]):
            numbersToCheck.append(int(info[i]))
        
        for number in numbersToCheck:
            if number in winningNumbers:
                if cardTotal == 0:
                    cardTotal = 1
                else:
                    cardTotal *= 2
        total += cardTotal
    print(total)