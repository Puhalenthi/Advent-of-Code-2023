import pprint
def isFiveOfKind(hand):
    return len(set(hand)) == 1

def isFourOfKind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return 4 in counts.values()

def isFullHouse(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return 3 in counts.values() and 2 in counts.values()

def isThreeOfKind(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return 3 in counts.values() and 1 in counts.values()

def isTwoPair(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return list(counts.values()).count(2) == 2

def isOnePair(hand):
    counts = {}
    for card in hand:
        counts[card] = counts.get(card, 0) + 1
    return list(counts.values()).count(2) == 1

def isHighCard(hand):
    return len(hand) == len(set(hand))

def isBiggestCard(hand1, hand2):
    cardStrength = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
    

def compareHands(hand1, hand2): # Strongest one gets returned
    cardStrength = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]

    # The following very long code will determine which is stronger
    if isFiveOfKind(hand1) and not isFiveOfKind(hand2):
        return hand1
    elif not isFiveOfKind(hand1) and isFiveOfKind(hand2):
        return hand2
    
    elif isFourOfKind(hand1) and not isFourOfKind(hand2):
        return hand1
    elif not isFourOfKind(hand1) and isFourOfKind(hand2):
        return hand2
    
    elif isFullHouse(hand1) and not isFullHouse(hand2):
        return hand1
    elif not isFullHouse(hand1) and isFullHouse(hand2):
        return hand2
    
    elif isThreeOfKind(hand1) and not isThreeOfKind(hand2):
        return hand1
    elif not isThreeOfKind(hand1) and isThreeOfKind(hand2):
        return hand2
    
    elif isTwoPair(hand1) and not isTwoPair(hand2):
        return hand1
    elif not isTwoPair(hand1) and isTwoPair(hand2):
        return hand2
    
    elif isOnePair(hand1) and not isOnePair(hand2):
        return hand1
    elif not isOnePair(hand1) and isOnePair(hand2):
        return hand2

    elif isHighCard(hand1) and not isHighCard(hand2):
        return hand1
    elif not isHighCard(hand1) and isHighCard(hand2):
        return hand2


    for card1, card2 in zip(hand1, hand2):
        if (card1.isdigit()):
            card1 = int(card1)
        if (card2.isdigit()):
            card2 = int(card2)
        if cardStrength.index(card1) < cardStrength.index(card2):
            return hand1
        elif cardStrength.index(card1) > cardStrength.index(card2):
            return hand2

with open("input.txt", "r") as f:
    lines = f.readlines()
    cards = []
    for line in lines: # Calculates the ordering of the cards
        line = line.rstrip("\n")
        data = line.split(" ")
        currCard = data[0]
        if cards == []:
            cards.append(line)
        else:
            for i in range(0, len(cards)):
                otherCard = cards[i].split(" ")[0] # Get the hand of the card we want to compare against
                if compareHands(currCard, otherCard) == otherCard:
                    cards.insert(i, line)
                    break
            else:
                cards.append(line)

    total = 0
    rank = 1
    for card in cards: # Calculates the total winnins
        total += (rank * int(card.split(" ")[1]))
        rank += 1
    
    print(total)