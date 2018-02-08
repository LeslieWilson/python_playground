#change.py
#a program to calculate the value of some change in dollars

"""def main():
    print "Change Counter"
    print
    print "please enter the count of each coin type"
    quarters = input("Quarters: ")
    dimes = input("Dimes: ")
    nickels = input("Nickels: ")
    pennies = input("Pennies: ")
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01
    print
    print "the total value of your change is", total

main ()"""

#gt towk, hw numbers entered by user are 5,3,4,6

type(3)

#want outpt different types

#3.2
#quadratic.py
#a program that computes the real roots of a quadratic equation
#illustrates use of the math library

import math #makes math library available

def main():
    print "this program find the real solutions to a quadratic"
    print

    a, b, c = input("please enter the coefficients (a, b, c): ")

    discRoot = math.sqrt(b * b - 4 * a * c)

    #JIMS HOMEWORK

    #take input someone gives, compute all the cutes of the numbers up to that input

def main():
    print "this program computes all the cubes of the numbers up to that input"

    num = input("please input your number")

    answer = 0


    for i in range (num):
        answer += i**3

    print answer




#take the average of user entered numbers.


def main():
    print "this program takes the average of user entered numbers"

    user_input = raw_input("enter as many numbers as you want, sep by comma")

    input_list = user_input.split(',')

    number_list = map(int, input_list)

    answer = 0.0

    for i in number_list:
        answer += float(i)

    final_answer = answer/len(number_list)

    print final_answer
main()


#
