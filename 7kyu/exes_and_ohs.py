'''
Instructions:

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

''' Solution'''
def xo(s):
    count = 0
    for i in s:
        if i in 'xX': count += 1
        if i in 'oO': count -= 1
    return count==0

print(xo('xOxo'))

''' Alternative Solution '''
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
