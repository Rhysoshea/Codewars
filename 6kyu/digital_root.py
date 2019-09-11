'''
Instructions
In this kata, you must create a digital root function.

A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.

Here's how it works:

digital_root(16)
=> 1 + 6
=> 7

digital_root(942)
=> 9 + 4 + 2
=> 15 ...
=> 1 + 5
=> 6

digital_root(132189)
=> 1 + 3 + 2 + 1 + 8 + 9
=> 24 ...
=> 2 + 4
=> 6

digital_root(493193)
=> 4 + 9 + 3 + 1 + 9 + 3
=> 29 ...
=> 2 + 9
=> 11 ...
=> 1 + 1
=> 2
'''


''' Solution '''
def digital_root(n):
    total = sum([int(i) for i in str(n)])
    if total > 9:
        return digital_root(str(total))
    return total

print (digital_root(5099))

''' Alternative solutions '''

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

def digital_root(n):
  return n%9 or n and 9 
