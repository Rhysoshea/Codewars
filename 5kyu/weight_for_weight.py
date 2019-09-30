'''
Instructions
My friend John and I are members of the "Fat to Fit Club (FFC)". John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99. Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: "100 180 90 56 65 74 68 86 99"

When two numbers have the same "weight", let us class them as if they were strings and not numbers: 100 is before 180 because its "weight" (1) is less than the one of 180 (9) and 180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
Don't modify the input
For C: The result is freed.
'''


''' Solution '''
def order_weight(strng):
    arr = strng.split(' ')
    weights = [sum([int(j) for j in i]) for i in strng.split(' ')]

    map = {}
    for i, weight in enumerate(weights):
        if weight in map:
            map[weight] += ' ' + arr[i]
        else:
            map[weight] = arr[i]

    for i in map:
        map[i] = ' '.join(sorted(map[i].split(' ')))

    s = set()
    for item in weights:
        s.add(item)
    s = sorted(s)
    # print (s)

    return ' '.join([map[i] for i in s])

print (order_weight("2000 10003 1234000 44444444 9999 11 11 22 123"))

''' Best practices solution '''
def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))
# this solution first splits the string and sorts, so we have the strings in correct string order but not correct weight order
# then the digits are summed and sorted again, this puts the strings in correct weight order and, because they were already in the correct string order, any weights that were identical will be in correct string order too 
