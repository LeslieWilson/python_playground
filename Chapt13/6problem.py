# write a recursive function to print out the digets of a number in english. for example if number is 153, output should be "one five three"



"""
Leslie Wilson
6problem.py
"""
names = ['zero', 'one', 'two', 'three', 'four','five','six','seven', 'eight', 'nine']



def digit_names(n):
    """
    >>> digit_names(123)
    one two three
    >>> digit_names(45)
    four five
    """
    n_string = str(n)
    first_digit = n_string[0]
    rest = int(n_string[1:])
    if rest == '':
            return ''
    else:
        rest = int(n_string[1:])
        return first_digit + ' ' + digit_names(rest)

if __name__ == '__main__':
        import doctest
        doctest.testmod()
