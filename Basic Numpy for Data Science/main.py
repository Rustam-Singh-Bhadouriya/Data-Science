import numpy as np

my_list = [1, 2, 3, 4]
# if we wanna mutiply array we can't do like this
my_list = my_list * 2
print(my_list) # Output = [1, 2, 3, 4, 1, 2, 3, 4]

# and in numpy you can multiply it!

array = np.array([1, 2, 3, 4])
array *= 2
print(array) # output = 2 4 6 8

