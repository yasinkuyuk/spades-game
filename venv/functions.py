spade = 0
heart = 1
diamond = 2
clover = 3

def printCards(cards):
    x = ""
    y = ""
    for card in cards:
        card.number = card.number + 1
        if card.colour == spade:
            x = "Spade"
        elif card.colour == heart:
            x = "Heart"
        elif card.colour == diamond:
            x = "Diamond"
        else:
            x = "Clover"

        if card.number == 1:
            y = "Ace"
        elif card.number == 11:
            y = "Jack"
        elif card.number == 12:
            y = "Queen"
        elif card.number == 13:
            y = "King"
        else:
            y = str(card.number)
        print("%s of %s's" % (y, x))
    return

def convertCardNumberToInteger(stringNumber):
    if stringNumber.lower() == 'a':
        return 0
    elif stringNumber.lower() =='j':
        return 10
    elif stringNumber.lower() == 'q':
        return 11
    elif stringNumber.lower() == 'k':
        return 12
    return int(stringNumber)
