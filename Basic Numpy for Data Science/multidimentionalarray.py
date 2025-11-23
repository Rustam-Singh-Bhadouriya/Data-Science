import numpy as np
# there are many D arrays

# 0D array
array0D = np.array('A')
print(array0D.ndim) # to see dimensional of array
print(array0D.shape) # to see row and coloms and len of list

# 1D array
array1D = np.array(['A', 'B', 'C'])
print(array1D.ndim)
print(array1D.shape) 

# 2D array
array2D = np.array([['A', 'B', 'C'], 
                   ['D', 'E', 'F'], 
                   ['G', 'H', 'I']])

print(array2D.ndim)
print(array2D.shape) 

# 3D array

array3D = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], 
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

# THIS HUGE LARGE BEAST IS 3D ARRAYS   
# we need a sequence for it  mean each list have 3 element so any have 2 it will give error!
# and if you have no data to put up here use _ or space like ' ' for good!

print(array3D.ndim)
print(array3D.shape) 
print(array3D[0][0][0])
print(array3D[0, 0, 0])

"""
CHAIN INDEXING  
it works like array[][][] for 3d

`array[daimention][list_index][data_index]`
like
array[0][0][0]
mean 0th diamention 0th list = ['A', 'B', 'C']
and 0th index of data = 'A'
answer is 'A' so this called chain indexing

theres is any way to write chain indexing
array[0, 0, 0] it will work same! and this is faster then other!

"""

# creating word with string concatulation

word = array3D[0, 0, 0] + array3D[1, 0, 0] + array3D[2, 0, 0]
print(word)

DEV = array3D[0, 1, 0] + array3D[0, 1, 1] + array3D[2, 1, 0]
print(DEV)