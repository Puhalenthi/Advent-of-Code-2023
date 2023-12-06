import pprint
import time
start = time.time()
with open("input.txt", "r") as f:
    cards = f.readlines()
    fullWinningNumbers = []
    fullNumbersToCheck = []
    WINNING_NUMBERS_COUNT = (2, 12)
    NUMBERS_TO_CHECK = (13, 38)
    #WINNING_NUMBERS_COUNT = (2, 7)
    #NUMBERS_TO_CHECK = (8, 16)
    
    for card in cards:
        info = card.split()
        cardNumber = int(info[1][0:-1])
        nextCardIndex = cardNumber # Stores the index card that should be added if a winning number detected

        winningNumbers = []
        for i in range(WINNING_NUMBERS_COUNT[0], WINNING_NUMBERS_COUNT[1]):
            winningNumbers.append(int(info[i]))
        fullWinningNumbers.append(winningNumbers)
        numbersToCheck = []
        for i in range(NUMBERS_TO_CHECK[0], NUMBERS_TO_CHECK[1]):
            numbersToCheck.append(int(info[i]))
        fullNumbersToCheck.append(numbersToCheck)
    
    #cardsCount = {} # Stores the count of every card
    cardsCount = [1] * len(cards)
    #for i in range(len(cards)):
    #    cardsCount[i] = 1
    pprint.pprint(fullNumbersToCheck[0])
    pprint.pprint(fullWinningNumbers[0])
    for i in range(len(cards)):
        for j in range(i + 1, i + 1 + (len(set(fullNumbersToCheck[i]) & set(fullWinningNumbers[i])))):
            cardsCount[j] += cardsCount[i]

    print(sum(cardsCount))

print(time.time() - start)