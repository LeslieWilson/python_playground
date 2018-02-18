# ZELLE, PAGE 120, PROBLEM 10

# write a program that counts the number of words in a sentence entered by the user

# this is a program that takes an input and prints out the number of words in that input

s = raw_input("please enter a sentance: ")
# this is the sentance the user puts in

count = len(s.split())
# this the number of words in the sentance

print("the number of words in the sentance is: " + str(count))

# TERMINAL OUTPUT:

# ➜  chapter-four git:(moreChapt4) ✗ python extra_excercises.py
# please enter a sentance: happy me!!
# the number of words in the sentance is: 2
