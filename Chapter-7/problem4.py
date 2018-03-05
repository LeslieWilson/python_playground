# a certain college classifies students according to credits earned. a student with less than 7 credits is a freshman. at leats 7 credits are required to be a spohemore, 16 to be a junior and 26 to be classified as a senior. write a program that calculates class standing from the number of credits earned.

def main (credits):
    if credits < 7:
        return("freshman")
    elif credits < 16:
        return ("sophemore")
    elif credits < 26:
        return("junior")
    elif credits >27:
        return("senior")

print main(9)
