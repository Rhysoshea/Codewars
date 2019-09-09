'''
Instructions:

Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.


'''

''' Basic Solution'''
def even_or_odd(int):
    if int%2==0:
        return "Even"
    return "Odd"

print (even_or_odd(2))
''' Best practices solution '''
