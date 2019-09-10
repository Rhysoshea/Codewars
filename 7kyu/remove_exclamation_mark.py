'''
Instructions:

Remove all exclamation marks from sentence except at the end.

Examples
remove("Hi!") == "Hi!"
remove("Hi!!!") == "Hi!!!"
remove("!Hi") == "Hi"
remove("!Hi!") == "Hi!"
remove("Hi! Hi!") == "Hi Hi!"
remove("Hi") == "Hi"
'''

''' Solution'''
def remove(s):
    count = 0
    for i in range(len(s)-1,0,-1):
        if s[i] == '!':
            count += 1
        else:
            break
    s = s.replace('!','') + count*'!'

    return s

print (remove(s))

''' Best Practices Solutions '''
def remove(s):
    return s.replace('!', '')+ '!'*(len(s)- len(s.rstrip('!')))

# using regex
import re

def remove(s):
    return re.sub(r'!+(?!!*$)', '', s)
