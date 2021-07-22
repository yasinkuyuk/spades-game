import random
from functions import *

class Card:
    def __init__(self,clr=0,nm=0):
        self.colour = clr
        self.number = nm

    def __gt__(self,second):
        if self.number == 0 and second.number != 0:
            return True
        else:
            if self.number > second.number:
                return True
            else:
                return False
    
    def __lt__(self,second):
        if second.number == 0 and self.number != 0:
            return True
        else:
            if self.number < second.number:
                return True
            else:
                return False
        
    def __eq__(self,second):
        if self.number == second.number:
            return True
        return False

class Player:
    def __init__(self,name):
        self.name = name
        self.cards = []
        self.roundsEarned = 0

class Round:
    def __init__(self,begin):
        self.beginningPlayer = begin
        self.moveCount = 0
        self.currentWinner = 0
        self.roundType = 0
        self.winningCard = Card()
        self.cardList = []

    
    def playRound(self,card,isWon,playerID):
        self.moveCount += 1
        self.cardList.append(card)
        if isWon:
            self.winningCard = card
            self.currentWinner = playerID
        return


class Game:
    def __init__(self):
        self.playerNumber = 4
        self.playerList = []
        self.cardList = []
        self.maxRound = 0
        self.bossCard = 0
        self.round = Round(0)

    def createPlayers(self,names):
        for i in range(self.playerNumber):
            player = Player(names[i])
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
                count = 0

            self.playerList[person].cards.append(card)
            count = count + 1
        return

    def printPlayersCards(self,index):
        player = self.playerList[index]
        print(player.name,"'s Cards:\n")
        player.cards.sort(key=lambda x:x.colour)
        printCards(player.cards)
        return

    def setGameRules(self,assertion,boss):
        self.maxRound = assertion
        self.bossCard = boss

    def removeCardFromList(self,playedCard,playerNumber):
        for card in self.playerList[playerNumber].cards:
            if card.colour == playedCard.colour and card.number == playedCard.number:
                self.playerList[playerNumber].cards.remove(card)
        return
    
    def playFirstRound(self,playedCard):
        self.round.roundType = playedCard.colour
        self.round.playRound(playedCard,True,0)
        self.removeCardFromList(playedCard,0)
        return

    def isColorInPlayersCards(self,colour,playerID):
        for card in self.playerList[playerID].cards:
            if card.colour == colour:
                return True
        return False
            
    def play(self,playedCard):
        if self.round.moveCount == 0:
            self.playFirstRound(playedCard)
            return True
        
        if playedCard.colour != self.round.roundType:
            if self.isColorInPlayersCards(playedCard.colour,0):
                print("You played wrong card. Please play the card with the same type!")
                return False
            else:
                if playedCard.colour != self.bossCard:
                    if self.isColorInPlayersCards(self.bossCard,0):
                        print("You played wrong card. Please play the card with boss type!")
                        return False
                    else:
                        self.round.playRound(playedCard,False,0)
                        self.removeCardFromList(playedCard,0)
                        if self.round.moveCount == 4:
                            self.playerList[self.round.currentWinner].roundsEarned += 1
                            winner = self.round.currentWinner
                            self.round = Round(winner)
                            if winner != 0:
                                self.randomPlay(winner,True)
                        return True
                else:
                    if self.round.winningCard.colour == self.bossCard:
                        if playedCard > self.round.winningCard:
                            self.round.playRound(playedCard,True,0)
                            self.removeCardFromList(playedCard,0)
                            if self.round.moveCount == 4:
                                self.playerList[self.round.currentWinner].roundsEarned += 1
                                winner = self.round.currentWinner
                                self.round = Round(winner)
                                if winner != 0:
                                    self.randomPlay(winner,True)
                            return True
                        else:
                            for card in self.playerList[0].cards:
                                if card.colour == self.bossCard and card > self.round.winningCard:
                                    print("You played the wrong card! Please increase the current winning card")
                                    return False

                            self.round.playRound(playedCard,False,0)
                            self.removeCardFromList(playedCard,0)
                            if self.round.moveCount == 4:
                                self.playerList[self.round.currentWinner].roundsEarned += 1
                                winner = self.round.currentWinner
                                self.round = Round(winner)
                                if winner != 0:
                                    self.randomPlay(winner,True)
                            return True
                            
                        
                    else:
                        self.round.playRound(playedCard,True,0)
                        self.removeCardFromList(playedCard,0)
                        if self.round.moveCount == 4:
                            self.playerList[self.round.currentWinner].roundsEarned += 1
                            winner = self.round.currentWinner
                            self.round = Round(winner)
                            if winner != 0:
                                self.randomPlay(winner,True)
                        return True
        else:
            if playedCard > self.round.winningCard:
                self.round.playRound(playedCard,True,0)
                self.removeCardFromList(playedCard,0)
                if self.round.moveCount == 4:
                    self.playerList[self.round.currentWinner].roundsEarned += 1
                    winner = self.round.currentWinner
                    self.round = Round(winner)
                    if winner != 0:
                        self.randomPlay(winner,True)
                return True
            else:
                for card in self.playerList[0].cards:
                    if card.colour == self.round.roundType and card > self.round.winningCard:
                        print("You played the wrong card! Please increase the current winning card")
                        return False
                self.round.playRound(playedCard,False,0)
                self.removeCardFromList(playedCard,0)
                if self.round.moveCount == 4:
                    self.playerList[self.round.currentWinner].roundsEarned += 1
                    winner = self.round.currentWinner
                    self.round = Round(winner)
                    if winner != 0:
                        self.randomPlay(winner,True)
                return True

    def endGame(self):
        if self.playerList[0].roundsEarned < self.maxRound:
            print("Oops! You lost the game. You had to win %d rounds, but you could %d\n" % (self.maxRound,self.playerList[0].roundsEarned))
        else:
            print("Congratulations! You won the game. You had to win %d rounds, and you won %d\n" % (self.maxRound,self.playerList[0].roundsEarned))

        for i in range(1,4):
            print("%s won %d rounds\n" % (self.playerList[i].name,self.playerList[i].roundsEarned))
        return
    
    def randomPlay(self,playerNumber,flag):
        if flag:
            index = random.randint(0, len(self.playerList[playerNumber].cards)-1)
            card = self.playerList[playerNumber].cards[index]
            self.round.playRound(card, False, playerNumber)
            self.removeCardFromList(card, playerNumber)
            self.randomPlay(playerNumber+1,False)
            return
        else:
            card = Card(self.round.roundType,-1)
            isInList = False
            for iterCard in self.playerList[playerNumber].cards:
                if iterCard.colour == self.round.roundType:
                    if iterCard > card:
                        card = iterCard
                        isInList = True
                    
            if isInList:
                isWon = True
                if self.round.winningCard.colour == self.bossCard:
                    isWon = False
                else:
                    if self.round.winningCard > card:
                        isWon = False
                        card = Card(self.round.roundType,0)
                        for iterCard in self.playerList[playerNumber].cards:
                            if iterCard.colour == self.round.roundType:
                                if card > iterCard:
                                    card = iterCard
                
                self.round.playRound(card, isWon, playerNumber)
                self.removeCardFromList(card, playerNumber)
                if self.round.moveCount == 4:
                    self.playerList[self.round.currentWinner].roundsEarned += 1
                    winner = self.round.currentWinner
                    self.round = Round(winner)
                    if winner != 0:
                        self.randomPlay(winner,True)
                else:
                    if playerNumber != 3:
                        self.randomPlay(playerNumber+1,False)
                return
            else:
                if self.isColorInPlayersCards(self.bossCard,playerNumber):
                    isWon = True
                    card = Card(self.bossCard,0)
                    for iterCard in self.playerList[playerNumber].cards:
                        if iterCard.colour == card.colour:
                            if iterCard < card:
                                card = iterCard

                    if self.round.winningCard.colour == self.bossCard:
                        isWon = False
                        if card < self.round.winningCard:
                            for iterCard in self.playerList[playerNumber].cards:
                                if iterCard.colour == card.colour:
                                    if iterCard > self.round.winningCard:
                                        card = iterCard
                                        isWon = True
                                        break
                    self.round.playRound(card, isWon, playerNumber)
                    self.removeCardFromList(card, playerNumber)
                    if self.round.moveCount == 4:
                        self.playerList[self.round.currentWinner].roundsEarned += 1
                        winner = self.round.currentWinner
                        self.round = Round(winner)
                        if winner != 0:
                            self.randomPlay(winner,True)
                    else:
                        if playerNumber != 3:
                            self.randomPlay(playerNumber+1,False)
                    return   
                else:
                    index = random.randint(0, len(self.playerList[playerNumber].cards)-1)
                    card = self.playerList[playerNumber].cards[index]
                    self.round.playRound(card, False, playerNumber)
                    self.removeCardFromList(card, playerNumber)
                    if self.round.moveCount == 4:
                        self.playerList[self.round.currentWinner].roundsEarned += 1
                        winner = self.round.currentWinner
                        self.round = Round(winner)
                        if winner != 0:
                            self.randomPlay(winner,True)
                        return
                    else:
                        if playerNumber != 3:
                            self.randomPlay(playerNumber+1,False)
                    return 
    
    def printRound(self,moveCount):
        if moveCount != 0:
            printCards(self.round.cardList)

        cardType = int(input("""Select the type of playing card: 
        0: Spades
        1: Hearths
        2: Diamonds
        3: Clovers: """))
        cardNumber = convertCardNumberToInteger(input("Type the number or name(J,Q,K,A) playing card: "))
        return cardType,cardNumber