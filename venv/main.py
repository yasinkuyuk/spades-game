from classes import Game,Card
import names
from functions import *

namelist = []
name = input("Please enter your name: ")
namelist.append(name)
for i in range(3):
    botname = names.get_first_name()
    namelist.append(botname)

roundCount = 13
currentRoundCount = 0
game = Game()
game.createPlayers(namelist)
game.createCardList()
game.distributeCards()

assertion = int(input("How many game you can earn"))
boss = int(input("""Select the type of the boss card: 
0: Spades
1: Hearths
2: Diamonds
3: Clovers"""))

game.setGameRules(assertion,boss)

while currentRoundCount < 13:
    cardType = int(input("""Select the type of playing card: 
    0: Spades
    1: Hearths
    2: Diamonds
    3: Clovers"""))
    cardNumber = convertCardNumberToInteger(input("Type the number or name(J,Q,K,A) playing card: "))
    card = Card(cardType,cardNumber)
    while True:
        if game.play():
            break

    currentRoundCount += 1

game.endGame()







