# ZELLE, PAGE 120, PROBLEM 10

# write a program that counts the number of wordgit s in a sentence entered by the user

# this is a program that takes an input and prints out the number of words in that input

s = raw_input("please enter a sentance: ")
# this is the sentance the user puts in

count = len(s.split())
# this the number of words in the sentance

print("the number of words in the sentance is: " + str(count))

# TERMINAL OUTPUT:


# please enter a sentance: happy me!!
# the number of words in the sentance is: 2
# _______

# PROBLEM 11

# write a program that calculates the average word
# length in a sentance entered by the user
# def averageLength (s, words):
#     sum = 0
#     for word in words:
#     s = raw_input("please enter a sentance: ")
# words = s.split()
# length = len(words)
# average = sum(length)
#
# print(average)


def averageLength():
    s = raw_input("please enter a sentence: ")
    arrayofwords = s.split()
    sum = 0
    for word in arrayofwords:
        sum += len(word)
    average = sum / len(arrayofwords)
    print average

averageLength()


# average = sum(len(words)/ len(words))




# did not work, TERMINAL OUTPUT

# >>> s = raw_input("please enter a sentance: ")
# please enter a sentance: pretty
# >>> words = s.split()
# >>> average = sum(len(word)) for word in words /
  # File "<stdin>", line 1
    # average = sum(len(word)) for word in words /
