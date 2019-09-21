'''
Instructions
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
'''


''' Solution '''
def move_zeros(array):
    i = 0
    j = 0
    while j != len(array):
        if str(array[i]) != 'False' and array[i] == 0:
            del array[i]
            array.append(0)
            j+=1
        else:
            i += 1
            j += 1
    return array

print (move_zeros([False,1,0.0,1,'0',2,0,1,3,"a"]))


''' Best practices solution '''
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)

''' Alternative approach '''
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
