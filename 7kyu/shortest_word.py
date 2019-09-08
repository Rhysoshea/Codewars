'''
Instructions:

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

'''

''' Solution'''

def find_short(s):
    # your code here
    arr = s.split(' ')
    l = min([len(x) for x in arr])
    return (l) # l: shortest word length
