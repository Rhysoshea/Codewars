'''
Instructions
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]
Go challenge Build Tower Advanced once you have finished this :)
'''

''' Solution '''
def tower_builder(n_floors):
    arr = [((2*i)+1)*'*' for i in range(n_floors)  ]
    # print (arr)
    return [ (int((len(arr[-1])-len(i))/2)*' ' + i + int((len(arr[-1])-len(i))/2)*' ') for i in arr ]


print (tower_builder(4))

''' Alternative Solution '''
def tower_builder(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
