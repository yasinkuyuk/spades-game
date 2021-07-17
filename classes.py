import random

class Card:
    def __init__(self,clr=0,nm=0):
        self.colour = clr
        self.number = nm

class Player:
    def __init__(self):
        self.cards = []

class Game:
    def __init__(self):
        self.playerNumber = 4
        self.playerList = []
        self.cardList = []

    def createPlayers(self):
        for i in range(self.playerNumber):
            player = Player()
            self.playerList.append(player)
        return
    
    def createCardList(self):
        for i in range(0,4):
            for j in range(0,13):
                card = Card(i,j)
                self.cardList.append(card)
        random.shuffle(self.cardList)
        return

    def distributeCards(self):
        person = 0
        count = 0
        for card in self.cardList:
            if count == 13:
                person = person + 1

            self.playerList[person].cards.append(card)
            count = count + 1
        return

    def printPlayersCards(self,index):
        player = self.playerList[index]
        player.cards.sort(key=lambda x:x.colour)
        x = ""
        y = ""

        for card in player.cards:
            card.number = card.number + 1
            if card.colour == 0:
                x = "MACA"
            elif card.colour == 1:
                x = "KUPA"
            elif card.colour == 2:
                x = "KARO"
            else:
                x = "SINEK"

            if card.number == 1:
                y = "AS"
            elif card.number == 11:
                y = "VALE"
            elif card.number == 12:
                y="KIZ"
            elif card.number==13:
                y="PAPAZ"
            else:
                y= str(card.number)
            print(x,y)
        return