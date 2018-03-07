# Heating and cooling degree-days are measures used by utility companies to estimate energy requirements. if the average temperature for a day is below 60, then the number of degrees below 60 is added to the heating degree-days. if the temperature is above 80, the amount over 80 is added to the cooling degree days. write a program that accepts a sequence of average daily temps and computes the running total of cooling and heating degree-days. the process should print these two totals after all the data has been processed.


# Modify the previous program to get inputs from a file.


def main():


    countCooling = 0
    countHeating = 0
    x = raw_input("enter the temperature (<0>, then enter to quit) >> ")
    while x != 0:
        x = eval(raw_input("enter the temperature (<0>, then enter to quit) >> "))

        if x >= 80:
            countHeating = countHeating + 1
        elif x <= 60:
            countCooling = countCooling +1
        else:
            print ("invalid category")

    results = [countCooling, countHeating]
    return "the number of cooling days is" + str(results[0]) + "and the number of heating days is" + str(results[1])

print main()

# here I tried to just do both problems at once. But realized I can't. 

# def main():
    # filename = raw_input("what file are the temps in? ")
    # infile = open(fileName,'r')
#
#     countCooling = 0
#     countHeating = 0
#
#     x = input ("enter the temperature: ")
#     while x >= 80:
#         countHeating = countHeating + 1
#         while x <= 60:
#             countCooling = countCooling + 1
#
#         return countCooling
#     return countHeating
#     line = infile.readline()
# print "\nthe number of cooling days is", countCooling "and the number of heating days is", countHeating
