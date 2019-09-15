'''
Instructions:

Create a function that takes a 2D array as an input, and outputs another array that contains the average values for the numbers in the nested arrays at the corresponding indexes.

Note: the function should also work with negative numbers and floats.

Examples
[ [1, 2, 3, 4], [5, 6, 7, 8] ]  ==>  [3, 4, 5, 6]

1st array: [1, 2, 3, 4]
2nd array: [5, 6, 7, 8]
            |  |  |  |
            v  v  v  v
average:   [3, 4, 5, 6]
And another one:

[ [2, 3, 9, 10, 7], [12, 6, 89, 45, 3], [9, 12, 56, 10, 34], [67, 23, 1, 88, 34] ]  ==>  [22.5, 11, 38.75, 38.25, 19.5]

1st array: [  2,   3,    9,   10,    7]
2nd array: [ 12,   6,   89,   45,    3]
3rd array: [  9,  12,   56,   10,   34]
4th array: [ 67,  23,    1,   88,   34]
              |    |     |     |     |
              v    v     v     v     v
average:   [22.5, 11, 38.75, 38.25, 19.5]

'''

''' Solution'''

def avg_array(arrs):
    avgs = [0 for i in range(len(arrs[0]))]
    for arr in arrs:
        for i in range(len(arr)):
            avgs[i] += arr[i]
    return [i/len(arrs) for i in avgs]

print(avg_array([[1, 2, 3, 4], [5, 6, 7, 8]]))

''' Best Practices Solution '''
def avg_array(arrs):
    return [sum(a)/len(a) for a in zip(*arrs)]
# the zip(*list) unpacks the arrays first so they are zipped as individual lists
