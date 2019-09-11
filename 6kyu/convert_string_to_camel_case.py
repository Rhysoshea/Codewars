'''
Instructions
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
to_camel_case("the-stealth-warrior") # returns "theStealthWarrior"

to_camel_case("The_Stealth_Warrior") # returns "TheStealthWarrior"

'''


''' Solution '''
import re
def to_camel_case(text):
    newText = re.split('-|_', text)
    return newText[0]+''.join([i.capitalize() for i in newText[1:]])

print (to_camel_case("the_stealth-warrior"))

''' Best Practice solution (python version dependent)'''

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s
print (to_camel_case("the_stealth-warrior"))
