
"""
Leslie Wilson
flashcard.py
May 5, 2018
"""

from random import *


class Ring:
    '''
    Ring is an object that holds all the flashcards.
    '''
# initiaite the genre of flashcards in self
    def __init__(self, genre):
        self.genre = genre
# if the user decides they want to see old cards, this method opens the text file and spits out the lines that are stored there (as questions and answers)
    def testMe(self):
        userInput = input("See an old card or make a new one? (select 'o' or 'n'): " + "\n")
        if userInput == "o":
            with open(self.genre + ".txt", "r") as file:
                linestore = []
                quiz = []
                for line in file:
                    linestore.append(line)
                    # appends each line into the array linestore
                for line in linestore:
                    quiz = line.split(',')
                    # splits each line at the comma, so can give seperate question/answer quiz
                    print(line)
                    if not quiz:
                        print ("end of questions")
                        break
                    print ("..........." + "\n"+ "??QUESTION??: " + quiz[0] + "\n" + "..........." + "\n" + "           ~~hit 'a' to see the answer~~" )
                    # takes the first of two comma separated peices and shows it to user
                    userInput2 =  input('')
                    if userInput2 == "a":
                        print ("..........." + "\n"+ "!!ANSWER!!: " + quiz[1] + "..........." + "\n"+ "\n"+ "           ~~NEXT QUESTION~~")



        elif userInput == "n":
            self.makeCard()

    def makeCard(self):
        userInputQ = input("Enter Question: ")
        userInputA = input("Enter Answer: ")
        with open(self.genre + '.txt', 'a') as file:
            file.write("\n" + userInputQ + "," + userInputA )

runRing = Ring("Comp-Sci Flashcards")
runRing.testMe()


# ~~~~~objects I made to practice for making flashcard, using Zelle as a resource~~~~

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
