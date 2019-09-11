'''
Instructions
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

##Examples :

iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

'''


''' Solution '''
def iq_test(numbers):
    even_count = 0
    odd_count = 0
    even_index = 0
    odd_index = 0
    for i, num in enumerate([int(j) for j in numbers.split(' ')]):
        if num % 2 == 0:
            even_count += 1
            even_index = i
        else:
            odd_count += 1
            odd_index = i

    if even_count > odd_count:
        return odd_index+1

    return even_index+1

print (iq_test("30 6 0 20 14 34 36 12 4 8 18 34 20 20 48 6 20 6 37 28 30 38 28 36 0 32"))

''' Best Practice solution '''
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
