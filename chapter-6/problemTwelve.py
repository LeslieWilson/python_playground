# write and test a function to meet this specification

# sumList(nums) is a list of numbers. returns sum of the numbers in that list.

# sumList = [2,4,5,3]
#
# def sumList(a,b,c,d):
#     sum = a + b + c + d
#
# sumlist()

# def sumDiff(x,y):
# diff = x - y
# return sum, diff
#
#

def sumNums(list):
    accumulater=0
    for i in list:
        accumulater+=i
    return accumulater

# the test case:
print sumNums([27,9,8])
