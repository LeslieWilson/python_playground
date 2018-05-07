# write a recursive function to print out the digets of a number in english. for example if number is 153, output should be "one five three"




'''
recursive_max.py
Leslie Wilson
May 5, 2018

'''

def recursive_max(array):
    '''
    function that takes an array and returns the max value
    >>> recursive_max([1,2,3,4,5,6,7])
    7
    '''
    if len(array) == 1:
        return array[0]
    else:
        return max(array[0], recursive_max(array[1:]))

def main():
    array = [1,4,11,7,9,3]
    print recursive_max(array)

if _name__=='__main_':
    import doctest
    doctest.testmod()
    main()
#
# """
# Leslie Wilson
# 6problem.py
# """
# names = ['zero', 'one', 'two', 'three', 'four','five','six','seven', 'eight', 'nine']
#
#
#
# def digit_names(n):
#     """
#     >>> digit_names(123)
#     one two three
#     >>> digit_names(45)
#     four five
#     """
#     n_string = str(n)
#     first_digit = n_string[0]
#     rest = int(n_string[1:])
#     if rest == '':
#             return ''
#     else:
#         rest = int(n_string[1:])
#         return first_digit + ' ' + digit_names(rest)
#
# if __name__ == '__main__':
#         import doctest
#         doctest.testmod()
