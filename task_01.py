import numpy as np

# 1.a Create a NumPy array from a list: [[1,2,3],[4,5,6]] and assign this array to A
A = np.array([[1,2,3],[4,5,6]])

# 1.b Print the shape of A
print("Shape of A:", A.shape)

# 1.c Reshape A to (3, 2) and store the result to B
B = A.reshape((3, 2))

# 1.d Print the shape of B
print("Shape of B:", B.shape)

# 1.e Transpose B to C
C = B.T

# 1.f Print the shape of C
print("Shape of C:", C.shape)

# 1.g Concatenate A and C along axis = 0, and save the result to D
D = np.concatenate((A, C), axis=0)

# 1.h Print the shape of D
print("Shape of D:", D.shape)

# 1.i Print the content of D
print("Content of D:\n", D)

# 1.j Let E be a copy of A
E = A.copy()

# 1.k Let E[0, 0] = 10
E[0, 0] = 10

# 1.l Print out the content of A and E
print("Content of A:\n", A)
print("Content of E:\n", E)