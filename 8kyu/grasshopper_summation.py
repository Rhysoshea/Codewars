'''
Instructions:

Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

For example:

summation(2) -> 3 1 + 2

summation(8) -> 36 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

'''

''' Basic Solution'''
def summation(num):
    total = 0
    while num > 0:
        total = total + num
        num = num - 1
    return total


''' Mathematical solution '''
def summation(num):
    return (num*num + num)/2

print (summation(8))
