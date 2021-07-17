import random
from functions import *

class Card:
    def __init__(self,clr=0,nm=0):
        self.colour = clr
        self.number = nm

    def __gt__(self,second):
        if self.number == 0 && second.number != 0:
            return True
        else:
            if self.number > second.number:
                return True
            else:
                return False
    
    def __lt__(self,second):
        if second.number == 0 && self.number != 0:
            return True
        else:
            if self.number < second.number:
                return True
            else:
                return False
        
    def __eq__(init,second):
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

    def removeCardFromList(self,playedCard):
        for card in self.playerList[0].cards:
            if card.colour == playedCard.colour && card.number == playedCard.number:
                self.playerList[0].cards.remove(card)
        return
    
    def playFirstRound(self,playedCard):
        self.round.roundType = playedCard.colour
        self.round.playRound(playedCard,True,0)
        self.removeCardFromList(playedCard)
        return

    def isColorInPlayersCards(self,colour):
        for card in self.playerList[0].cards:
            if card.colour == colour:
                return True
        return False
            
    def play(self,playedCard):
        if self.round.moveCount == 0:
            self.playFirstRound(playedCard)
            return True
        
        if playedCard.colour != self.round.roundType:
            if self.isColorInPlayersCards(playedCard.colour):
                print("You played wrong card. Please play the card with the same type!")
                return False
            else:
                if playedCard.colour != self.bossCard:
                    if self.isColorInPlayersCards(self.bossCard):
                        print("You played wrong card. Please play the card with boss type!")
                        return False
                    else:
                        self.round.playRound(playedCard,False,0)
                        self.removeCardFromList(playedCard)
                        if self.round.moveCount == 4:
                            self.playerList[self.round.currentWinner].roundsEarned += 1
                            winner = self.round.currentWinner
                            self.round = Round(winner)
                        return True
                else:
                    if self.round.winningCard.colour == self.bossCard:
                        if playedCard > self.round.winningCard:
                            self.round.playRound(playedCard,True,0)
                            self.removeCardFromList(playedCard)
                            if self.round.moveCount == 4:
                                self.playerList[self.round.currentWinner].roundsEarned += 1
                                winner = self.round.currentWinner
                                self.round = Round(winner)
                            return True
                        else:
                            for card in self.playerList[0].cards:
                                if card.colour == self.bossCard && card > self.round.winningCard:
                                    print("You played the wrong card! Please increase the current winning card")
                                    return False

                            self.round.playRound(playedCard,False,0)
                            self.removeCardFromList(playedCard)
                            if self.round.moveCount == 4:
                                self.playerList[self.round.currentWinner].roundsEarned += 1
                                winner = self.round.currentWinner
                                self.round = Round(winner)
                            return True
                            
                        
                    else:
                        self.round.playRound(playedCard,True,0)
                        self.removeCardFromList(playedCard)
                        if self.round.moveCount == 4:
                            self.playerList[self.round.currentWinner].roundsEarned += 1
                            winner = self.round.currentWinner
                            self.round = Round(winner)
                        return True
        else:
            if playedCard > self.round.winningCard:
                self.round.playRound(playedCard,True,0)
                self.removeCardFromList(playedCard)
                if self.round.moveCount == 4:
                    self.playerList[self.round.currentWinner].roundsEarned += 1
                    winner = self.round.currentWinner
                    self.round = Round(winner)
                return True
            else:
                for card in self.playerList[0].cards:
                    if card.colour == self.round.roundType && card > self.round.winningCard:
                        print("You played the wrong card! Please increase the current winning card")
                        return False
                self.round.playRound(playedCard,False,0)
                self.removeCardFromList(playedCard)
                if self.round.moveCount == 4:
                    self.playerList[self.round.currentWinner].roundsEarned += 1
                    winner = self.round.currentWinner
                    self.round = Round(winner)
                return True

    def endGame(self):
        if self.playerList[0].roundsEarned < self.maxRound:
            print("Oops! You lost the game. You had to win %d rounds, but you could %d\n" % (self.maxRound,self.playerList[0].roundsEarned))
        else:
            print("Congratulations! You won the game. You had to win %d rounds, and you won %d\n" % (self.maxRound,self.playerList[0].roundsEarned))

        for i in range(1,4):
                print("%s won %d rounds\n" % (self.playerList[i].name,self.playerList[i].roundsEarned))
        return









    
        


