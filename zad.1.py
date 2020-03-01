import numpy as np
import pandas as pd
with open('ok_matrix.txt', 'r') as file:
    data = file.read()
matrix_size = data[0]
# print(matrix_size)
data = data[1:]
data = data.split()
# print(data)
data = np.array(data)
# data = data.resize(1,1)
print(data)
# define matrix A using Numpy arrays
A_conflicting = np.array([[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]])
 
 #define matrix B
B_conflicting = np.array([1, 1, 0]) 
A_inconsistent = np.array([[1, 0, 0],
    [0, 1, -1],
    [0, 0, 0]])

B_inconsistent = [4, 1, 5]

A = np.array([[1, 2, 3],
 [-1, 2, 4],
 [2, 1, 1]])

B = [7, 6, 13]

#for i in range()
    


try:
    # linalg.solve is the function of NumPy to solve a system of linear scalar equations
    print ("Solutions:\n",np.linalg.solve(A, B) )
except np.linalg.LinAlgError as err:
    if 'Singular matrix' in str(err):
        print("Matrix is singular")
    else:
        raise

#[  6.  15. -23.]