def euler1 (a,b,max):
    count = 0
    for number in xrange(0,max):
        # look at list so can do things to each element


        if number % a == 0 or number % b == 0:
            count += number

            print(number)

    return(count)


print(euler1(3,5,10))

# given a string, go through another string (compare) and take out only the letters from the frist string! take out only letters in string 2 that aren't in string1

def pract1 (string1,string2):

    for letter2 in string2:
        isletter2Instring1 = False

        for letter1 in string1:
            print(letter1,letter2,letter1 == letter2)
            if letter1 == letter2:
                isletter2Instring1 = True
        if isletter2Instring1 == False:
            print(letter2)

pract1("cat","happy")

def prac2 (string3, string4):

    for letter3 in string3:
        isletter3Instring2 = False

        for letter3 in string3:
            print(letter3,letter4)
            if letter3 == letter4:
                isletter3Instring2= True
        if isletter3Instring3 == False:
            print(letter3)

pract2("the", "boat")
