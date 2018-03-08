# this is an example of one that was done incorrectly, it doesn't need two for-loops it only needs one so it is spitting out the wrong answer.
#
# userStr = raw_input("put in your word, this program will remove any duplicate characters: ")
#
# array = list(userStr)
# # print array
#
#
# def main():
#
#     results = []
#     for i in range(len(array)):
#         for j in range(i+1, len(array)):
#             # print array[j]
#             if array[i] == array[j]:
#                 results.append(array[i])
#     return results
# print main()


userStr = raw_input("put in your word, this program will remove any duplicate characters: ")

array = list(userStr)

def main():

    results = []
    for i in array:
        if i not in results:
            results.append(i)


    return results
print main()
