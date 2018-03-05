# many companies pay time and a half for any hours worked above 40 in a given week. write a program to input the number of ohurs worked and the hourly rate and calculate the total wages for the week


# program calculates total wages for the week based on input of hours worked and hourly rate

def main():

    hours = input("how many hours a week did you work?: ")
    rate = input("how much were you paid per hour?: ")
    wage = hours * rate

    if hours > 40:
        overtime = wage + wage/2
    else:
        overtime = wage

    return overtime
print main()
