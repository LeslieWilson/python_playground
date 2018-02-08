
#discuss what is happening here



def main():
    celsius = input("What is the celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "the temperature is", fahrenheit,"degrees Fahrenheit."

main()


#def main () starts defining the function

#celsius = is assigning the variable (or value), "input" is waiting for user input in response to the prompt

#fahrenheit = is assigning the value for the variable fahrenheit

#print is displaying the answer, concatonating it within the sentence




#Second example


def main():
    print "this prog computes the average of two scores"

    score1, score2 = input("enter two scores separated by a comma: ")
    average = (score1 + score2)

    print "the average of the scores is:", average

main()



##2.6


for i in [0,1,2,3]:
    print i

for odd in [1,3,5,7,9]:
    print odd * odd





#2.7

#chapt2ex.py

def main():
    print "this program calculates the future value of a 10-year investment"

    apr = input("enter the annualized interest rate: ")
    principal = input("Enter the inital principal: ")

    for i in range (10):
        principal = principal * (1 + apr)

    """except EOFError:
        print ("error: EOF or empty")

        check = " "
    print check"""
    print "the amount in 10 years is: ", principal

main()
#why didin't this wk? I tried adding this: https://www.quora.com/How-does-one-fix-a-python-EOF-error-when-using-raw_input

##it works now

#2.8, excercises

#1. list and describe the six steps in software development process:
#formulate requirements, (see what the problem is ) Determine specifications (describe what the thing you're making will do, be able to talk about what the inputs and outputs will be and how they relate to each other. Create a design, which means, formulating how the program gets worked out, how it will look and act etc. Implement the design, which is writing code for it. Debug it- self explainatory, it means testing. Finally, maintain it, which means, continue developing in response to feedback

#2. done

#JIMS HOMEASSIGNMENTS

#first

def main():
    print "this is the temperature converted from celsius to fahrenheit"
    celsius = input("What is the celsius temperature? ")
    fahrenheit = 9.0 / 5.0 * celsius + 32
    print "the temperature is", fahrenheit,"degrees Fahrenheit."

main()

#Second

def main():
    print "this program calculates the future value of a 10-year investment"

    apr = input("enter the annualized interest rate: ")
    principal = input("Enter the inital principal: ")
    years = input("enter the number of years you have")

    for i in range (years):
        principal = principal * (1 + apr)

    """except EOFError:
        print ("error: EOF or empty")

        check = " "
    print check"""
    print "the amount in" years "is: ", principal
