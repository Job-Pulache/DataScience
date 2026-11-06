import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6], [7,8]])

suma = A+B
print("the sum of the two matrices is:", suma)

product = np.dot(A,B)
print("The product of the two matrices ", product)

determinant = np.linalg.det(A)
print("The determinant of the A is:", determinant)

inversa = np.linalg.inv(A)
print("The inverse of the A:\n", inversa)

valores_propios, vectores_propios = np.linalg.eig(A)
print("The eigenvalues of A:\n", valores_propios)
print("The eigenvectors of A:\n", vectores_propios)

B = np.array([1,2])
x = np.linalg.solve(A,B)
print("The solution of the system AX = B is:\n", x)

