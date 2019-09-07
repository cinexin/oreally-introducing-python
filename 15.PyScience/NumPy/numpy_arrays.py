import numpy as np
b = np.array([2,4,6,8])
print("Numpy array:", b)
print("Dimensions of array:", b.ndim)
print("size of array:", b.size)
print("Number of values in each rank:", b.shape)

a = np.arange(10)
print("A range(10):%s, num of dimensions: %d, shape: %s, size: %d" %(a, a.ndim, a.shape, a.size))

b = np.arange(7,11)
print("A range(7, 11):%s, num of dimensions: %d, shape: %s, size: %d" %(b, b.ndim, b.shape, b.size))

# arange with step
print(np.arange(7, 11, 2))

# arange with floats
f = np.arange(2.0, 9.8, 0.3)
print(f)

# one last trick: dtype argument tells arange what types of values to produce
g = np.arange(10, 4 , -1.5, dtype=np.float)
print(g)

# Make an array of zeros...
a = np.zeros((3,))
print("np.zeros((3,)): %s, Dimension: %d, Shape: %s, Size: %d" %(a, a.ndim, a.shape, a.size))
# let's do a 2-dimesional one...
b = np.zeros((2,4))
print("np.zeros((2, 4)): %s, Dimension: %d, Shape: %s, Size: %d" %(b, b.ndim, b.shape, b.size))
# fill with ones....
o = np.ones((3, 5))
print(o)
# fill array with random values between 0.0 and 1.0...
r = np.random.random((3, 5))
print(r)

# Change an array's shape...
a = np.arange(10)
print(a)
a = a.reshape(2, 5)
print(a)
a = a.reshape(5, 2)
print(a)
# Assigning a tuple to shape attribute does the same:
a.shape = (2, 5)
print(a)
'''
The only restriction on a shape is that the product of the ranz sikes needs to equals the total number of values
In our case: 10
ie: 
a = a.reshape(3,4)
This is invalid!
'''


# Get elements with []
a = np.arange(10)
print("a:", a)
print("a[7]:", a[7])
print("a[-1]:", a[-1])

# Get elements with [] in a 2-d array...
a.shape = (2, 5)
print("a:", a)
print("a[1,2] =", a[1,2] )

# Getting slices from arrays...
print("a =", a)
print("a[0,2:] =", a[0,2:])
print("a[-1:3] =", a[-1,:3])

# Assigning values to slices...
a = np.arange(10)
a = a.reshape(2, 5)
print("a =", a)
a[:, 2:4] = 1000
print("a =", a)

# Multiplying arrays...
from numpy import *
a = arange(4)
print(a)
a *= 3
print("a *= 3 =", a)

a = zeros((2,5)) + 17.0
print("zeros((2,5)) + 17.0 =", a)