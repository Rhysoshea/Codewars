'''
Instructions:

In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Example:

make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0
Notes:

The number can be negative already, in which case no change is required.
Zero (0) is not checked for any specific sign. Negative zeros make no mathematical sense.

'''

''' Basic Solution'''
def make_negative( number ):
    if number < 0:
        return number
    elif number > 0:
        return number*-1
    else:
        return 0


''' Best practices solution '''
def make_negative( number ):
    return -abs(number)

print (make_negative(0))
