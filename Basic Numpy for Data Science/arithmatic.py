import numpy as np

# Scaler Arithmatic :-

array = np.array([1, 2, 3])
# addiction
print("Addiction: ", array + 1)

# substraction
print("substraction: ",array - 1)

# Multipilication
print("Multipilication: ",array * 2)

# Division
print("Division: ", array / 2)

# Power of 
print("power of 5 (you can take any): ", array ** 5)

print("____________Vectorized Math Functions___________________")

# vactor mean 1d array
array = np.array([1.76, 2.21, 3.99])
# sqrt
print("sqrt: ", np.sqrt(array))

# around mean 3.99 -> 4.00, 2.21 -> 2
print("Around: ", np.round(array))

# PI
print("PI: ", np.pi)


# EXCERSIVE

redius = np.array([1, 2, 3])
# convert these redius to area of Square

print((redius ** 2 ) * np.pi)


# ELEMENTWISE ARITHMATIC

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])