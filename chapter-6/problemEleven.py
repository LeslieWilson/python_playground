# write and test a function that meets these specification
# squareEach(nums) nums is a list of numbers. modifies the list by squaring each entry.

# def square(x):
#     return x*x


    def squareNums(list):
        for i in list:
            i * i
        return list

    # the test case:
    print squareNums([3,9,8])
