'''
Instructions:

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out, because 9**2 is 81 and 1**2 is 1.

Note: The function accepts an integer and returns an integer
'''

''' Solution'''
def square_digits(num):
    return int(''.join([str(int(i)*int(i)) for i in str(num)]))

num = 9119
print (square_digits(num))

''' Alternative Solution '''
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
