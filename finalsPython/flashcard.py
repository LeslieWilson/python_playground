
"""
Leslie Wilson
flashcard.py
May 5, 2018
"""

import random


class Ring:
    '''
    Ring is an object that holds all the flashcards of a given genre.
    '''

    def __init__(self, genre):
        self.genre = genre

    def readCards(self):
        '''
        Takes an input from user to view old or new cards and either prompts for the answer
        until each card is read or prompts for the entry of new questions to add to the ring
        '''
        userInput = input("See an old card or make a new one? (select 'o' or 'n'): " + "\n")
        while userInput not in "o n":
            userInput = input("See an old card or make a new one? (select 'o' or 'n'): " + "\n")
        if userInput == "o":
            with open(self.genre + ".txt", "r") as file:
                linestore = []
                quiz = []
                for line in file:
                    line = line.strip()  # remove the new line characters from the end
                    linestore.append(line)
                random.shuffle(linestore)   # shuffle the array so the questions are in a random order
                    # appends each line into the array linestore
                for line in linestore:
                    quiz = line.split(',')
                    # splits each line at the comma, so can give seperate question/answer quiz
                    if not quiz:
                        print ("end of questions")
                        break
                    print ("..........." + "\n"+ "??QUESTION??: " + quiz[0] + "\n" + "..........." + "\n" + "           ~~hit 'a' to see the answer, or guess it!~~" )
                    # takes the first of two comma separated peices and shows it to user
                    self.checkAnswer(quiz[1])



        elif userInput == "n":
            self.makeCard()

    def checkAnswer(self, answer):
        '''
        Function that takes a user input as a guess and compares it to the answer
        of a given flashcard.
        '''
        guess = ""
        while guess != "a":
            guess = input("guess the answer: ")
            if guess == answer:
                print("Correct!")
                break
            if guess != "a":
                print("incorrect, type a to see the answer, or guess again!")
        print ("..........." + "\n"+ "!!ANSWER!!: " + answer + "..........." + "\n"+ "\n"+ "           ~~NEXT QUESTION~~")

    def makeCard(self):
        '''
        prompts the user for a question and answer, saves them to a file with
        comma seperated with the genre as a filename
        '''
        moreCards = "y"
        while moreCards == "y":
            userInputQ = input("Enter Question: ")
            userInputA = input("Enter Answer: ")
            with open(self.genre + '.txt', 'a') as file:
                file.write(userInputQ + "," + userInputA + "\n" )
            moreCards = input("Would you like to make another card? (y or n)")

def ChooseGenre():
    '''
    function to prompt the user for a genre of flash cards to either add to or read from
    '''
    print("pick a genre of flash card")
    genre = input()
    ring = Ring(genre)
    ring.readCards()

ChooseGenre()



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
