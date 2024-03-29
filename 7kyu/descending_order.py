'''
Instructions:

Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221

'''

''' Solution'''

def Descending_Order(num):
    arr = [int(i) for i in str(num)]
    arr.sort(reverse=True)
    return int(''.join([str(i) for i in arr]))

print (Descending_Order(21445))

''' Best Practices Solution '''
def Descending_Order(num):
    return int("".join(sorted(str(num), reverse=True)))
