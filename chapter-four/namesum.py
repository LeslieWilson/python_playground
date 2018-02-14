def nameSum():
    name = raw_input("type a name you want the value of: ")
    letters = list(name)
    sum = 0
    for letter in letters:
        sum += ord(letter) - 96

    print "the point value of the word '%s' is: %d" % (name, sum)

def test():
    print "for an input of the word 'the' expect the output of 33"
    nameSum()

test()
