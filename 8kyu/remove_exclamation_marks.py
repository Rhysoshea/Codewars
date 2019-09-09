'''
Instructions:

Description:
Remove all exclamation marks from the end of sentence.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi! Hi"
remove("Hi") === "Hi"
'''

''' Solution'''
def remove(s):
    while s[-1] == '!':
        s = s[:-1]
    return s
    
s = "Hi! Hi!"
print (remove(s))

''' Best Practices Solution '''
def remove(s):
    return s.rstrip("!")
    # rstrip() removes trailing characters from string - default is " "
