'''
Instructions:

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

'''

''' Solution'''

def sort_array(source_array):
    # Return a sorted array.
    if len(source_array) == 0:
        return source_array
    else:
        odd_array = []

        for i in range(len(source_array)):
            if source_array[i]%2 != 0:
                odd_array.append(source_array[i])
        odd_array.sort()
        j=0

        for i in range(len(source_array)):
            if source_array[i]%2 != 0:
                source_array[i] = odd_array[j]
                j+=1

        return source_array

print(sort_array([1, 5, 2, 8, 3, 4]))


''' Best practices solution '''
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
