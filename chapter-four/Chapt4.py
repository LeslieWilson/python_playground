str1 = "Hello"
str2 = 'spam'

"""print str1, str2"""

"""type(str1)"""

# why didin't this work

"""type(str2)"""




"""firstName = input ("Please enter your name: ")"""
# if you enter john into terminal, traceback error. But enter it with quotations and it will interperate it as a string literal and work. but its too burdensome for users"""
#
# to solve this problem, use raw_input, which is just like input except does not evaluate the expression the user types, handed in as a string

"""firstName = raw_input("please enter your name: ")
print "Hello", firstName"""


greet = "hello bob"
greet[0]

# ...etc, if you indicate x = 8 and print greet[x-2] you'll get b...and it does count the spaces

# a contiguois sequence of characters or a substring can be taken out also, by slicing. <string>[<start>:<end>], start and end are int valued expressions.start produces substring starting at position givn by start and running up to but not including position end.if either expression is missing, the start and end of the string are the assumed defaults. greet[:]just hands back the entire string. greet[5: ] hands back ' bob'

# concatenation builds a string by "gluing" two strings together. len tells how many characters are in a string.

# username.py
    # simple string processing program to generate usernames

def main():
    print "this program generates computer usernames"
    print

    # get users first and last names

    first = raw_input("please enter your first name (all lowercase): ")
    last = raw_input("please enter your last name (a;; lowercase): ")

    # concatenate first initial with 7 chars of the last name
    uname = first[0] + last[:7]

    # output the username

    print "your username is: " , uname

main ()

# indexing, slicing and concatenating are combined
