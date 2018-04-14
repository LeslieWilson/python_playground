# write an automated censor program, that reads in the text from a file and creates a new file where all of the four-letter words have been replaced by "***". you can ignore punctuation, and you may assume  that no words in the gile are split across ,ultiple lines.
import string

def main ():
    path = 'fname.txt'
    text = open(path,'r').read()
    text = string.lower(text)
    words = text.split()
    newText = []
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
main()



# import fname
#
# def main ():
#
#     print ("this program analyzes word frequency in a file")
#     print ("and prints a report on the n most frequent words. \n")
#
#     # get sequence of words from the file.
#
#     fname = input("file to analyze:")
#     text = open(fname, 'r').read()
#     text = string.lower(text)
#     for ch in ('!$@%^@&^&$%&#^(*)'):
#         text = string.replace (text,ch,'****')
#     words = string.split(text)
#
#     # construcct a dictionary of word counts.
#
#     counts = {}
#     for w in words:
#         counts [w] = counts.get(w,0) +1
#
#         # output analysis of n most frequent words
#         n = input ("output analysis of n most frequent words.")
#         items = counts.items()
#         items.sort(compareItems)
#         for i in range (n):
#             print ("%-10s%5d") % items [i]
#
# if __name__ == '__main__': main()
