def wordCount():
    textFile = raw_input("enter the exact location of a text file: ")
    count = 0
    characters = 0
    words = 0
    with open(textFile) as f:
        for line in f:
            count += 1
            splitLine = line.split()
            words += len(splitLine)
            for word in splitLine:
                characters += len(word)

    print count
    print words
    print characters

    print "There are %d lines, %d words and %d characters in %s." % (count, words, characters, textFile)

def test():
    print "For my test I used the example file text.txt which has 5 lines, 18 words and 54 characters it reads:\nHere is a text message\nhere is line 2\nhere is line 3\nhere is line 4\nend"
    wordCount()

test()
