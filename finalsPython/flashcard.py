# This will be the flashcard constructor that makes all other flashcards!..

"""
 objects.py
"""

# make a ring class, they could make the file without having to title it. make a card be a function within the ring class. ring keeps track of how many cards there are. the ring could name the card. otherwise every time you makea new card would need to put a name in for it.
from random import *


class Ring:
    def __init__(self, genre):
        # self.count = 0
        self.genre = genre

    def testMe(self):
        userInput = input("See an old card or make a new one? (select 'o' or 'n'): " + "\n")
        if userInput == "o":
            with open(self.genre + ".txt", "r") as file:
                linestore = []
                quiz = []
                for line in file:
                    linestore.append(line)
                for line in linestore:
                    quiz = line.split(',')
                    print(line)
                    if not quiz:
                        print ("end of questions")
                        break
                    print ("..........." + "\n"+ "??QUESTION??: " + quiz[0] + "\n" + "..........." + "\n" + "           ~~hit 'a' to see the answer~~" )
                    userInput2 =  input('')
                    if userInput2 == "a":
                        print ("..........." + "\n"+ "!!ANSWER!!: " + quiz[1] + "..........." + "\n"+ "\n"+ "           ~~NEXT QUESTION~~")
                    # if userInput3 == "n":
                    #     print






                # usrInput = input("you should put in a")
                # if usrInput == 'a':
                # print (linestore[1])
                    # linestore 0 is the question and linestore 1 is answer


                # go through file and find where break point is

        elif userInput == "n":
            self.makeCard()

    def makeCard(self):
        userInputQ = input("Enter Question: ")
        userInputA = input("Enter Answer: ")
        with open(self.genre + '.txt', 'a') as file:
            file.write("\n" + userInputQ + "," + userInputA )

            # self.count =+ 1



runRing = Ring("Comp-Sci Flashcards")
runRing.testMe()






# + str(round(self.count * random())



#
# + str(self.count)











# class Card:
#     def __init__(self, rank, suit):
#         self.suit = suit
#         self.rank = rank
#     def __str__(self):
#         return "{} of {}".format(self.rank,
#                                  self.suit)
# class Hand:
#     def __init__(self):
#         self.cards = []
#     def add(self, card):
#         self.cards.append(card)
#     def __str__(self):
#         result = "<Hand : "
#         for card in self.cards:
#             result += str(card) + ", "
#         result += ">"
#         return result
#
# def main():
#     card_1 = Card("Ace", "Clubs")
#     card_2 = Card("Queen", "Spades")
#     hand = Hand()
#     hand.add(card_1)
#     hand.add(card_2)
#     print("My hand is")
#     print(hand)
#
# main()


# class Leslie:
#     def __init__(self, mood, sleepLevels):
#         self.mood = mood
#         self.sleepLevels = sleepLevels
#     def __str__(self):
#         return "she feels {} when she has slept {} hr(s)".format(self.mood,     self.sleeplevels)
#
# class Therapy:
#     def __init__(self):
#         self.possibleMoods = []
#     def confess(self, mood):
#         self.possibleMoods.append(mood)
#         def __str__(self):
#             diagnosis = "Mood : "
#             for mood in self.possibleMoods:
#                 diagnosis += str(mood) + ", "
#             diagnosis += "."
#             return mood
#
# def main():
#     mood_1 = Leslie("angry", "low")
#     mood_2 = Leslie("sad", "very low")
#     therapy = Therapy()
#     therapy.confess(mood_1)
#     therapy.confess(mood_2)
#
#     print "my mood is"
#     print (therapy)
#
# main()
