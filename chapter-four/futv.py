def main():
    print "This program calculates the future value of an n-year investment."
    principal = input("Enter the initial principal: ")
    apr = input("Enter the annualized interest rate in decimal form: ")
    years = input("Enter the total number of years the investment will build: ")
    output = " Years     Total   \n-------------------\n"
    for i in range(years + 1):
        principal = principal * (1 + apr)
        output += "   %-6d $%0.2f  \n" % (i, principal)
    print output
    print "The amount in %d years is: $%0.2f" % (years, principal)
main()
