'''open text.txt - count the amount of characters and the total amount of words and print it to the console.'''

# example, pg 109 ZELLE
# printfile.py
# prints file to screen

def main():
        fname = raw_input("enter filename: ")
        infile = open(fname,'r')
        data = infile.read()
        text(data)
        charNum(data)

'''
this function takes the data and splits it into individual words, and prints the amount of words there are
'''
def text(data):
    wordcount = len(data.split())
    print("the number of words in the sentance is: " + str(wordcount))

'''
this takes the data and splits the individual characters apart and counts them
'''
def charNum(data):
    charCount = data.split()
    sum = 0
    for characters in charCount:
        sum += len(characters)

    print "the number of chars in the file: " + str(sum)


main()
