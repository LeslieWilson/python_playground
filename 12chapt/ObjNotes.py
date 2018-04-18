"""
 objects.py
"""
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


class Leslie:
    def __init__(self, mood, sleepLevels):
        self.mood = mood
        self.sleepLevels = sleepLevels
    def __str__(self):
        return "she feels {} when she has slept {} hr(s)".format(self.mood,     self.sleeplevels)

class Therapy:
    def __init__(self):
        self.possibleMoods = []
    def confess(self, mood):
        self.possibleMoods.append(mood)
        def __str__(self):
            diagnosis = "Mood : "
            for mood in self.possibleMoods:
                diagnosis += str(mood) + ", "
            diagnosis += "."
            return mood

def main():
    mood_1 = Leslie("angry", "low")
    mood_2 = Leslie("sad", "very low")
    therapy = Therapy()
    therapy.confess(mood_1)
    therapy.confess(mood_2)

    print "my mood is"
    print (therapy)

main()
