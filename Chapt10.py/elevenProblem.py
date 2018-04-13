
from random import *


class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


    def getrank(self):
        if self.rank == 1:
            return "ace"
        elif self.rank == 11:
            return "joker"
        elif self.rank == 12:
            return "queen"
        elif self.rank == 13:
            return "king"
        else:
            return " %d" % (self.rank)

    def getSuit(self):
        if self.suit == "d":
            return  "diamonds"
        elif self.suit == "c":
            return "clubs"
        elif self.suit == "h":
            return "hearts"
        elif self.suit == "s":
            return "spades"


    def BJValue(self):
        if self.rank == 1:
            return "bj value 1"
        elif self.rank == 11:
            return "bj value 10"
        elif self.rank == 12:
            return "bj value 10"
        elif self.rank == 13:
            return "bj value 10"
        else:
            return "your bj val is %d" % (self.rank)

    def __str__(self):

        return "%s of %s |" % (self.getrank() , self.getSuit())

card = Card(randrange(1,13), choice(["s","d","c","h"]))

def randomCard():
    array = []

    input = raw_input("put your number in: ")
    for i in range(int(input)):
        card = Card(randrange(1,13),
        choice(["s","d","c","h"]))
        array.append(card)
    return array

# x = randomCard()
#
# for card in x:
#     print(card)
    # print(card.BJValue())








card.BJValue()
card.getrank()
card.getSuit()
