'''
Instructions
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''


''' Solution '''
def countbits(n):
    return bin(n)[2:].count('1')
    # return bin(n).count('1') also acceptable as binaries begin with '0b'

print (countbits(1234))
