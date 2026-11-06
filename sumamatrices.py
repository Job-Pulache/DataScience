import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6], [7,8]])

suma = A+B
print("the sum of the two matrices is:", suma)

product = np.dot(A,B)
print("The product of the two matrices ", product)