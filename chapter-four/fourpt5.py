# example app, date conversion

# lets user input a date in one format and program
# will display date as another formulate





# input the date in mm/dd/yyy format(datStr)

dateStr = raw_input("enter a date(mm/dd/yyyy): ")

# split datStr into month, dat and year strings
monthStr, dayStr, yearStr = (dateStr.split("/"))

# convert the montStr into a month name

months = ["janurary", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

monthStr = months[int(monthStr)-1]
# output results in month, day year format
print "the converted date is: " + monthStr + " " + dayStr + ", "+yearStr

print "the converted date is: %s %s, %s" % (monthStr, dayStr, yearStr)
a
