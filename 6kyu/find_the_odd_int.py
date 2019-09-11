'''
Instructions
Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''


''' Solution '''
def find_it(seq):
    counter = {}
    for i in seq:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    for key, count in counter.items():
        if count % 2 != 0:
            return key
    return None

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))

''' Alternative solutions '''
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
