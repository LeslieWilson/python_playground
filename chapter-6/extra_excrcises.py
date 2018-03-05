# make a function that takes a number and multiplies it by two


def main(x):
    return x * 2
main(3)

# make a function that takes a string and says hello to it

def hi(name):
    print "hello" + name

hi("dave")

# write a function that takes three numbers and adds them together

def main(a,b,c):
    return a+b+c
main(3,4,5)

# function that takes an array of numbers and gives total

def array(sum):
    sum = 0
    for number in array:
        sum += number
    return sum

array(3,4,5)


# take an array of strings and print out each string

def array(strings):
    for string in strings:
        print string

    array("hello", "goodbye")

# make a function that takes an argument that multiplies it by two , and you need something that does that to an array

# take an array in a function of numbers and loop through it and pultiply each number by two

# take an array, multiply each word in the array by the number passed into the num function

def mult(x):
    x * 2

def arrayMult(numbers):
    for number in numbers:
        mult(number)
    return numbers


print arrayMult([2,5])
