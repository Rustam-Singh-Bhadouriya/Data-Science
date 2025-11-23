import numpy as np


"""
NOTE
 : -> Select Whole!
 and in start it like array[: 4]
 then : -> 0
 and in end point array[1 :]
 : -> its len - 1 

 and some middle
 array[:: 2]
 mean start with 0 and that the last print after two
 
"""

array3D = np.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']], 
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']], 
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', '_']]])

array2D = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12], 
                   [13, 14, 15, 16]])

# print(array2D)
# for sclicing = [start:end:step]

print(array2D[1]) # Its will print [5, 6, 7, 8]
print("_____________________________________") # For readability
print(array2D[1: 3]) # start = 1 and end = 3
# output = [[ 5  6  7  8], [ 9 10 11 12]]

print("_____________________________________")

print(array2D[0: 3: 2]) # Start = 0, end = 3 and step = 2
# mean it will print 1 row after 1 row
# so output = [[ 1  2  3  4], [ 9 10 11 12]]

print("_____________________________________")

# and if you select whole and step things with -1 it will reverse!
print(array2D[:: -1]) # mean start with 0 and put up with last and step comes from down
# output = [[13 14 15 16],[ 9 10 11 12],[ 5  6  7  8],[ 1  2  3  4]]
print("_____________________________________")

# now lets see Colums
print(array2D[:, 0]) # mean : -> select whole rows and 0 meant for show all 0th colums
# output = [1 5 9 13]
print("_____________________________________")

print(array2D[:, 0:3]) # it meant in whole daimentional print each row's 3 values
print("_____________________________________")

print(array2D[:, 0:3:2]) # it will print data after a data
print("_____________________________________")




