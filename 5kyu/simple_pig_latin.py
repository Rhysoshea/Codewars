'''
Instructions
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''


''' Solution '''
def pig_it(text):
    return ' '.join([(x[1:] + x[0] + 'ay') if x not in '!?' else x for x in text.split(' ')  ])

print (pig_it("Pig latin is cool"))
