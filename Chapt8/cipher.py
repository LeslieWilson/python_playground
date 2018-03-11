# program that takes in a file and returns a file where every letter is incremented by a certain value

def main():
    # filename = raw_input("whats the filename?: ")

    userInput = "3"
    filename2 = "empty.txt"
    filename = "temps.txt"
    infile = open(filename,'r')

    line = infile.readline()


    # userInput = raw_input("put in what you want to increment it by: ")

    # filename2 = raw_input("whats filename2: ")
    # shush = open(filename2,'r+')
    with open(filename2,'w') as shush:

        while line != "":
            for x in line:
                print x
                shush.write(chr(ord(x) + int(userInput)))

            line = infile.readline()


    # shush.close()
    infile.close()

    with open(filename2,'r') as shush:
    # shush = open(filename2,'r')
        shushfile = shush.read()

    # shush.close()



    return shushfile


print main()
