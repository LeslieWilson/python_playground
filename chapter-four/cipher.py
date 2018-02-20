
# allow for users to input a number and a string


# have output that gives string back, shifted the input amount

def newWordchar():
    userInputNum = raw_input("enter a number: ")
    userInputStr = raw_input("enter a sentence: ")
    chars = userInputStr.split()
    indivChars = chars.split()
    print indivChars
    newWord = chr(ord(chars))
    print newWord

newWordchar()

# make input connect to behaviors in array with for loop
# make input number the same as the index each letter in alphabet moves
