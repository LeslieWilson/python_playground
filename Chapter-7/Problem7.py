#ababysitter charges 2.50 an hour until 9:00pm when the rate drops to 1.75 an hour.(the kids are in bed). write a program that accepts a starting time and ending time in hours and min and calculates the total babysitting bill. you may assume that the starting and ending times are in a single 24 hour period. Partil hours should be appropriately prorated.

#

def main(start_time,end_time):
# function takes start and end time passed in
    if start_time[0] < 21:
# if the start time hour is before 9:00pm
        if end_time[0] > 21:
# if the end time hours is after 9:00pm
            hours_before21 = 21 - start_time[0]
            hours_after21 = end_time[0] - 21
# new variable hours_before21 represents 9:00pm minus the hour you started, which are the hours at rate 2.50
            min_before21 = -start_time[1]
            min_after21 = end_time[1]
# new variable min_before21 represents the min you didin't spend working at 2.50


        else:
# if the end time hours are before 9:00pm
            hours_before21 = end_time[0] - start_time[0]
# the ending time (if before 9:00pm)subtracting the starting time
            min_before21 = end_time[1] - start_time[1]
# the ending times min minus the  starting times min
            hours_after21 = 0
# none of the hours are being spent after 9:00pm
            min_after21 = 0
# none of the min are being spent after 9:00pm

    else:
        # if the start time hours are after 9:00pm

        hours_after21 = end_time[0] - start_time[0]
        # hours spent after 9:00

        min_after21 = end_time[1] - start_time[1]
        # minutes spent after 9:00

        hours_before21 = 0
        # none of the hours are being spent before 9:00pm

        min_before21 = 0
        # none of the mnutes are being spent before 9:00pm

    total_money = wages(2.50,hours_before21,min_before21) + wages(1.75,hours_after21,min_after21)

    return total_money

def wages(hourly, hours, min):
    salary = hourly * hours + hourly/60 * min
# if before 9, wage = 2.50, if wage after 9, wage = 1.75
    return salary
print main([13,0],[23,0])
