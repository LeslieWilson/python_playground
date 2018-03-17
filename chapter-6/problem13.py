# write and test a function to meet this specification
# to Numbers(strList) strList is a list of strings, each of which represents a number. Modifies each entry in the list by coverting it to a number


def mainList(strList):
    listNotString= []
    for string in strList:
        print string
        notString = int(string)
        listNotString.append(notString)
        print type(string)
    return listNotString

print mainList(["4","1"])
