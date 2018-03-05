# a certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B,3-C,2-D,1-f, 0-F. Write a program that accepts a quiz score as an input and uses a decision structure to calculate the corresponding grade.

def main():

    score = input("what is your score? from 1-5: ")

    if score == 1:
        print "YOU GOT AN A"
    elif score == 2:
        print "YOU GOT A B"
    elif score == 3:
        print "YOU GOT A C DUMMY"
    elif score == 4:
        print "HOW COULD YOU GET A D"
    elif score == 5:
        print "GET OUT OF CLASS YOU FAILED"

main()
