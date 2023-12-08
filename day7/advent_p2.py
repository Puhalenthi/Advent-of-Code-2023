import pprint
from collections import Counter

def isFiveOfKind(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' not in hand:
        return len(set(hand)) == 1
    elif 5 in values: 
        return True
    elif 4 in values:
        return True
    elif 3 in values and 2 in values:
        return True
    return False

def isFourOfKind(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' not in hand:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        return 4 in counts.values()
    elif 4 in values:
        return True
    elif 3 in values and handDict['J'] == 1: # XXXJY
        return True
    elif handDict['J'] == 3 and len(handDict) == 3:
        return True
    elif handDict['J'] == 2 and len(handDict) == 3:
        return True
    
    return False

    

def isFullHouse(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' in hand:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        return 3 in counts.values() and 2 in counts.values()
    elif max(values) == 3 and len(handDict) == 2:
        return True
    elif handDict['J'] == 1 and len(handDict) == 3:
        return True
    return False


def isThreeOfKind(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' not in hand:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        return 3 in counts.values() and 1 in counts.values()
    elif max(values) == 2 and len(handDict) == 4:
        return True
    elif handDict['J'] == 2 and len(handDict) == 4:
        return True
    return False
    
    

def isTwoPair(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' not in hand:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        return list(counts.values()).count(2) == 2
    return False

def isOnePair(hand):
    handDict = Counter(hand)
    values = handDict.values()
    if 'J' not in hand:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        return list(counts.values()).count(2) == 1
    elif len(values) == 5:
        return True
    return False

def isHighCard(hand):
    if 'J' not in hand:
        return len(hand) == len(set(hand))
    else:
        return True

def compareHands(hand1, hand2): # Strongest one gets returned
    cardStrength = ['A', 'K', 'Q', 'T', 9, 8, 7, 6, 5, 4, 3, 2, 'J']

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
    pprint.pprint(cards)
    total = 0
    rank = 1
    for card in cards: # Calculates the total winnings
        total += (rank * int(card.split(" ")[1]))
        rank += 1
    
    print(total)