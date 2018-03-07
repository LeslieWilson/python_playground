# a year is a leap year if it is divisible by 4, unless it is a century year that is not divisible by 400. (1800 and 1900 are NOT leap years while 1600 and 2000 are.) write a program that calculates whether a year is a leap year.

def main():
    year = input("put a year in and I'll tell you if its a leap year!: ")
    if year % 4 == 0
        if str(year)[-1] == "0" and str(year)[-2] == "0" and century % 400 != 0:
            print "its not a leap year"
        else:
            print "its a leap year"
    else:
        print "not a leap giuear"

main()
