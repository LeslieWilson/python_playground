"""
Leslie Wilson
April 14 2018
elevenproblem.py
"""

# Python Chapter 11, Problem 11:

# write an automated censor program, that reads in the text from a file and creates a new file where all of the four-letter words have been replaced by "***". you can ignore punctuation, and you may assume  that no words in the gile are split across ,ultiple lines.


import string

def main ():

    # this takes a file, opens it and reads it, gets all the chars to group together as words, makes them all lowercase, puts them into an array.

    path = 'fname.txt'
    text = open(path,'r').read()
    text = string.lower(text)
    words = text.split()
    newText = []

    # array loops through every word in words, if word is length is not 4, it puts it into the newText array, if it is equal to 4, it also puts it into the array but, replaces it with ***.

    print words
    for word in words:
        if len(word) != 4:
            newText.append(word)
        elif len(word) == 4:
            newText.append(word.replace(word, "****"))
            # for ch in word:
            #     word = string.replace(word,ch,'*')
            #     Replace wo

    print newText

    text = open("new_path.txt", "w")
    for word in newText:
        text.write(word)

    text.close()


main()
