import numpy as np
escalar = np.array(42)
print(type(escalar))
print(escalar)

vector = np.array([34, 56, 31, 90, 32, 23, 12])
print(vector)

matrix = np.array([[1,2,2],[3,4,5],[6,7,8]])#Matrix de doble dimensión
print(matrix)   

tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])#Tensor de triple dimensión
print(tensor)

array_arange = np.arange(10)
print(array_arange)

eye_matrix = np.eye(3)
print(eye_matrix)