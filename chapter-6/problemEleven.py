# write and test a function that meets these specification
# squareEach(nums) nums is a list of numbers. modifies the list by squaring each entry.

# def square(x):
#     return x*x


def squareNums(array):
    for num in array:
        num *= num
        print num
    return array

    # the test case:
print squareNums([3,9,8])
